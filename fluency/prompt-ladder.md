# The Prompt Ladder

**Task:** Write a LinkedIn post about my recent Kaggle results.
**My voice rule:** simple real words, no self-praise (no "proud", "thrilled", "excited to announce"), no project-detail name-dropping, only scores I have actually verified.
**Real numbers I gave the prompt (verified from the Kaggle CLI):** Name That LLM 0.538 (new best), CASMI 0.478, Aura EMG 0.550, Soil Grain Size 18.155.

Each rung shows the prompt, a real output I got by running that prompt, and four short notes.

---

## Baseline — the weak prompt

**Prompt:** "Write a LinkedIn post about my Kaggle results."

**Output excerpt:**
> 🚀 Thrilled to announce my incredible journey across FOUR Kaggle competitions! From molecules to LLMs, I'm pushing the boundaries of machine learning and achieving remarkable scores. This is just the beginning — watch this space! 💪 #MachineLearning #AI #DataScience #Kaggle

**What changed:** Nothing yet — this is the starting point.
**Why:** I wanted to see what the model does with zero guidance.
**What improved:** Nothing. It produced *something* in five seconds.
**What still fails:** Everything that matters — hype words, emoji, no real numbers, and it sounds like everyone else's post. This is exactly the voice I do not want.

---

## Version 1 — give it the real numbers

**Prompt:** "Write a LinkedIn post about my Kaggle results. Use these scores: Name That LLM 0.538, CASMI 0.478, Aura EMG 0.550, Soil Grain Size 18.155."

**Output excerpt:**
> Proud to share my latest Kaggle results! 🎯 Name That LLM: 0.538 · CASMI: 0.478 · Aura EMG: 0.550 · Soil Grain Size: 18.155. Grateful for everything these competitions are teaching me. Onwards and upwards!

**What changed:** I added the actual data instead of letting the model invent a "journey".
**Why:** A post with no numbers says nothing. The scores are the whole point.
**What improved:** The post is now factual and specific — a reader learns something real.
**What still fails:** "Proud to share", "Onwards and upwards", the emoji. Still press-release voice.

---

## Version 2 — ban the hype words

**Prompt:** "Write a LinkedIn post about my Kaggle results: Name That LLM 0.538, CASMI 0.478, Aura EMG 0.550, Soil Grain Size 18.155. Do not use the words proud, thrilled, excited, announce, journey, or grateful. No emojis."

**Output excerpt:**
> My Kaggle scores this week: Name That LLM — 0.538 (a new best for me). CASMI — 0.478. Aura EMG — 0.550. Soil Grain Size — 18.155. Four competitions, four very different problems. Still a long way from the top of any of these leaderboards.

**What changed:** I banned the specific words that made it sound like a press release.
**Why:** "Write in a simple voice" is vague; a banned-word list is an instruction the model can actually follow.
**What improved:** It reads like a person now. The last line is honest, which I like.
**What still fails:** It is a plain list. There is no lesson or story, so there is no reason for anyone to stop scrolling.

---

## Version 3 — add the lesson, not just the scores

**Prompt:** "Write a LinkedIn post about my Kaggle results: Name That LLM 0.538 (new best), CASMI 0.478, Aura EMG 0.550, Soil Grain Size 18.155. No hype words (proud, thrilled, excited, announce, journey, grateful), no emojis. Include one honest lesson: my biggest gains came from fixing my validation, not from bigger models."

**Output excerpt:**
> Small update from my Kaggle work. Name That LLM moved to 0.538 this week, my best so far. CASMI is at 0.478, Aura EMG at 0.550, Soil at 18.155. The honest lesson from all four: my scores moved when I fixed how I validate, not when I tried bigger models. A leaky split makes everything look good and teaches you nothing.

**What changed:** I gave it one true lesson to build the post around.
**Why:** Scores alone are a list. A lesson gives a reader something to take away, and it is the part people actually reply to.
**What improved:** The post now has a point of view, and the lesson is genuinely what happened.
**What still fails:** It runs a bit long and reads as one block. LinkedIn posts need air — short lines, breaks.

---

## Version 4 — fix the format for the feed

**Prompt:** "Rewrite this as a LinkedIn post with short lines and line breaks, under 100 words: scores Name That LLM 0.538 (new best), CASMI 0.478, Aura EMG 0.550, Soil 18.155; lesson: gains came from fixing validation, not bigger models. Simple real words, no hype words, no emojis, no hashtags except #Kaggle at the end."

**Output excerpt:**
> Kaggle update.
>
> Name That LLM: 0.538 — my best so far.
> CASMI: 0.478. Aura EMG: 0.550. Soil: 18.155.
>
> What actually moved my scores was not a bigger model.
> It was fixing my validation so it stopped lying to me.
>
> #Kaggle

**What changed:** Format instructions — short lines, line breaks, a word limit, one hashtag.
**Why:** How a post looks on a phone decides whether it gets read at all.
**What improved:** Scannable in two seconds, still honest, still in my voice.
**What still fails:** "Kaggle update." as an opener is flat. The first line has to earn the second line.

---

## Version 5 — fix the hook

**Prompt:** "LinkedIn post, under 100 words, short lines. Start with the lesson as the first line, then the scores. Lesson: my validation was lying to me, fixing it moved my scores more than any model change. Scores: Name That LLM 0.538 (new best), CASMI 0.478, Aura EMG 0.550, Soil Grain Size 18.155. Simple real words. No hype words, no emojis, end with #Kaggle only."

**Output excerpt:**
> My validation was lying to me.
>
> Fixing it moved my Kaggle scores more than any model I tried.
>
> This week: Name That LLM 0.538 (new best), CASMI 0.478, Aura EMG 0.550, Soil 18.155.
>
> Still far from the top. But at least now I know the numbers are real.
>
> #Kaggle

**What changed:** The hook is now the lesson, stated plainly, in the first line.
**Why:** The first line is the only guaranteed read. It should be the most interesting true thing, not a label like "update".
**What improved:** This is the first version I would actually post without rewriting it myself.
**What still fails:** "at least now I know the numbers are real" is slightly dramatic. Minor — I would soften that one line by hand and post the rest as-is.

---

## Final reusable prompt template

```
Write a LinkedIn post for me.
- Start with the lesson as the first line, stated plainly.
- Then the facts, one per line: <competition: score, competition: score>.
- Lesson to use: <one honest lesson from this week's work>.
- Under 100 words. Short lines, line breaks between sections.
- Simple real words, the way a student would actually talk.
- Never use: proud, thrilled, excited, announce, journey, grateful, delve.
- No emojis. No self-praise. No project-detail name-dropping.
- End with #Kaggle only.
- Only use the numbers I gave you — never invent or round a score.
```

**What the ladder taught me:** each rung fixed exactly one problem — data, tone, substance, format, hook — and the fixes only worked because each instruction was specific enough to check in the output.
