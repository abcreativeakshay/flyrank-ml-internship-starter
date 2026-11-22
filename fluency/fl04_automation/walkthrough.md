# FL-04 — Automation workflow walkthrough

**What this is:** a small, real automation that turns a folder of loose notes
into one dated Markdown digest: counts by category plus every action line,
in one place. It runs as a plain Python script (`digest.py`) — a *scripted
workflow*, i.e. the free path. It is deliberately **not** built on a paid
no-code tool (Zapier/Make/n8n Cloud would add a subscription, an account,
and a vendor between me and a 60-line problem). The same script can be
scheduled with cron or Task Scheduler at zero cost.

Author: Akshay Biradar · First built and run: 22–23 Nov 2026 · Runtime: Python 3.12, stdlib only.

## Step diagram

```
  incoming/*.md, *.txt          (drop notes in, any time)
          |
          v
  [1] SCAN      list .md/.txt files in the incoming folder, sorted
          |
          v
  [2] READ      read each note as UTF-8 (bad bytes replaced, never crash)
          |
          v
  [3] CLASSIFY  keyword rules, first match wins:
                kaggle -> report -> content -> other (default)
          |
          v
  [4] EXTRACT   action lines only when explicitly marked:
                TODO: / ACTION: / NEXT STEP: / - [ ] checkbox
          |
          v
  [5] WRITE     one dated digest .md: counts table, all-actions list,
                per-note sections (title, category, word count, actions)
          |
          v
  runs/run_NN_digest.md  +  runs/run_log.md / run_log.json
```

## Configuration — every rule and "prompt" used

There is no LLM and no hidden prompt in this workflow; the entire
configuration is the rule block at the top of `digest.py`, reproduced here
exactly as run:

```python
CLASSIFICATION_RULES = {
    "kaggle":  ["kaggle", "leaderboard", "submission", "rank ",
                "competition", "notebook", "public lb", "private lb"],
    "report":  ["report", "pbl", "jury", "annexure", "paper",
                "documentation", "dashboard", "streamlit"],
    "content": ["linkedin", "post draft", "social",
                "content idea", "caption"],
}
DEFAULT_CATEGORY = "other"   # first matching category wins, in dict order

ACTION_PATTERN   = lines starting (optionally after "- " or "[ ]") with
                   TODO / ACTION / NEXT STEP followed by ":" or "-"
CHECKBOX_PATTERN = Markdown task lines "- [ ] ..."
```

Command used for every run:

```
python digest.py --incoming incoming --output runs/run_NN_digest.md
```

Inputs are my real working notes: current Kaggle scores (Name That LLM
v60 = 0.538, CASMI closed at 0.478, Soil Grain Size v34 = 18.155, Aura EMG
v13d = 0.54970), a DMDW report task, a LinkedIn post draft idea, an Aura
finals note, and a Tirupati trip note. Per-run input snapshots are kept in
`runs/run_NN_inputs/` with SHA-256 prefixes in `runs/run_log.json`, so any
run can be reproduced exactly.

## The five runs

All five runs were executed back-to-back on 22 Nov 2026; each script run
itself took ~0.05 s (measured in `run_log.json`).

| Run | What changed | Notes | Actions | Counts (kaggle/report/content/other) | Output |
|---:|---|---:|---:|---|---|
| 1 | Baseline: 3 notes created | 3 | 5 | 2 / 1 / 0 / 0 | `runs/run_01_digest.md` |
| 2 | Added `aura_emg_finals.md` | 4 | 6 | 3 / 1 / 0 / 0 | `runs/run_02_digest.md` |
| 3 | Edited LinkedIn note: +1 line, +1 `NEXT STEP` action | 4 | 7 | 3 / 1 / 0 / 0 | `runs/run_03_digest.md` |
| 4 | Added `tirupati_trip.md` (no rule keywords) | 5 | 8 | 3 / 1 / 0 / 1 | `runs/run_04_digest.md` |
| 5 | Edited Kaggle note: +1 strategy line, +1 `NEXT STEP` | 5 | 9 | 3 / 1 / 0 / 1 | `runs/run_05_digest.md` |

The changes behaved exactly as designed: every added note moved the counts,
every added marked line moved the action total by exactly one, and the
keyword-free trip note fell through to `other`.

## Time saved — honest arithmetic

Measured, not guessed, where possible:

- **Automated:** one run ≈ 0.05 s of compute; realistically ~30 s of my
  time to run it and skim the digest for sanity.
- **Manual equivalent** (my estimate, stated as one): opening and reading
  5 short notes ≈ 5 × 90 s = 7.5 min; copying action lines into one list
  ≈ 3 min; writing and formatting the counts summary ≈ 4 min.
  Total ≈ **14–15 min per digest**.
- **Saving ≈ 14 min per digest.** At one digest a day, 5 days a week,
  that is roughly **70 min/week**.
- **Setup cost:** ~45 min to write, test and document the script.
  Break-even after about **3–4 digests**; everything after that is profit.
  I am not claiming the 0.05 s figure as "time saved" — the honest saving
  is my ~14 minutes, not the computer's.

## Known failure points (several observed in these very runs)

1. **Priority-order misclassification — observed.** `linkedin_draft_idea.md`
   is classified **kaggle** in all five runs, because it mentions Kaggle
   scores and "leaderboards", and `kaggle` rules are checked before
   `content`. That is why `content` stays at 0 throughout. First-match
   rules cannot handle multi-topic notes; a hit-count or weighted rule
   would be the next iteration.
2. **Substring false positives.** Matching is substring-based: "rank "
   fires on any ranked list, "paper" would fire on "paperwork". Keywords
   were chosen against my own notes, not against the world.
3. **Unmarked actions are invisible.** Only `TODO:` / `ACTION:` /
   `NEXT STEP:` / `- [ ]` lines are extracted. A sentence like "I should
   email the guide tomorrow" is missed by design — explicit markers are
   the price of auditable extraction.
4. **No deduplication or prioritisation.** The same action written in two
   notes appears twice; deadlines inside action text are not parsed,
   sorted or escalated.
5. **Format limits.** Only `.md` / `.txt` files are read; PDFs, images of
   handwritten notes, and voice memos are ignored silently. Non-UTF-8
   bytes are replaced rather than reported.
6. **No delivery step.** The workflow writes a file; it does not send it
   anywhere. Wiring it to WhatsApp/email is a separate, deliberate step —
   and the point where a scripted workflow like this one would grow into
   an agent (see the FL-05 explainer).
