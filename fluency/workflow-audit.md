# FL-01 — Workflow Audit

**Akshay Biradar** · B.Tech Computer Science, MIT ADT University, Pune (2024–2028) · AI Engineer at Peakso (remote)

This is an audit of the work I actually do every week, where my time goes, and where AI genuinely helps me versus where it creates risk if I stop checking.

## My recurring workflows

| Workflow | Current tools | Time cost | Pain point | Where AI helps | Risk / check needed |
|---|---|---|---|---|---|
| Kaggle competition iteration (CASMI, Name That LLM, Soil Grain Size, Aura EMG) | Kaggle CLI and notebooks, GitHub repos per competition, PROGRESS.md logs | The biggest block of my week — often several hours a day during active phases | Keeping track of what I tried, what scored, and what failed across four competitions at once; re-checking leaderboard scores by hand | Summarising experiment history, drafting notebook variants, comparing validation vs leaderboard results, keeping PROGRESS.md current | AI must never report a score it has not verified from the Kaggle CLI itself. A plausible-sounding number is worse than no number. Every score gets checked against `kaggle competitions submissions` before I trust it |
| Coursework reports and papers | Word / LaTeX, my own report template, source documents from my team | 1–3 days per report when done fully by hand | Formatting to a fixed institutional format (page limits, section order, tables of contents) eats more time than the actual content | Converting and reformatting existing text into the required format, restoring tables/figures, building a paper version from a report | Wording must not change when I say "format only". I verify paragraph by paragraph that the text is mine, and I never let AI invent results, enrolment numbers, or team roles |
| LinkedIn writing (1 post per week) | Notes on my phone, LinkedIn directly | 30–45 minutes per post, mostly rewriting | My first drafts sound like a press release. I want simple, real words and no self-praise, and getting there takes many passes | Turning a rough note and my real numbers into a short post in my voice, cutting hype words | AI drifts towards bragging language ("proud", "thrilled", big claims). I read every post aloud and delete anything I would not say to a friend |
| Internship outreach | LinkedIn, a tracker sheet of companies and HR contacts | A few hours per round of research and messages | Researching which companies in Pune actually take interns at my stage, and writing connection messages that do not sound copy-pasted | Building researched company lists with honest flags (who has no Pune intern route), drafting connection requests and DMs for my approval | Nothing gets sent without my approval. For outreach I position myself only as a B.Tech student — no job title — and AI has to respect that boundary every time |
| Project building (COGNIVA, Kaagaz AI, dashboards) | VS Code, Streamlit, Hugging Face + Gemini APIs, GitHub | Ongoing — this is my Peakso work and my semester projects | Boilerplate, debugging, and documentation take time away from the actual design decisions | Writing and debugging code, generating first drafts of documentation, explaining errors | I review code before it ships. AI-written code that I cannot explain is a liability in a viva or a code review, so I read it line by line for anything important |

## Three target tasks with success definitions

### 1. Kaggle score tracking and experiment logging
**Task:** After every submission, record the verified score, rank, and what changed versus the previous version in PROGRESS.md.
**Success definition:** 100% of my submissions logged with a score taken from the Kaggle CLI output (not from memory or expectation), within the same day as the submission. Zero invented or "expected" scores in the log.

### 2. Report reformatting without wording changes
**Task:** Convert a finished report into a required journal or institutional format (for example, SN Computer Science format) with only formatting changes.
**Success definition:** A paragraph-level comparison shows 0 wording changes outside the sections the format itself forces (for example, a declarations section), the document hits the required page/keyword limits, and any LaTeX version compiles exactly as sent.

### 3. Weekly LinkedIn post in my voice
**Task:** One post per week from my real, current results.
**Success definition:** The post is under 120 words, uses only scores I have verified that week, contains no self-praise words and no project-detail name-dropping, and I can read it aloud without it sounding like someone else wrote it.

## Open item — my own accounts

The Claude Project setup for this workflow and my Anthropic Academy enrolment are **to be completed in my own Claude/Academy accounts**. They need my personal login, so they are still open as of writing this audit — I am not claiming they are done. Everything above describes workflows I already run today with the tools listed.
