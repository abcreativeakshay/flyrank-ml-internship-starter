# Draw the Path — Sitemap, Toolkit, Pressure Test

## Portfolio sitemap

```
Home (akshay.peakso.in)
├── Home — name, one-line claim, best proof up front
├── Cases
│   ├── COGNIVA — multilingual voice-first dementia-care platform
│   ├── Kaagaz AI — document-to-data platform for Indian documents
│   ├── FlyRank ML Capstone — search-intelligence ranking model
│   └── DMDW — healthcare data warehouse and dashboards
├── About — who I am, what I study and where I work
└── Contact — form, LinkedIn, GitHub
```

Four cases is deliberate. Each one proves a different thing: COGNIVA proves I can build for real users in real languages, Kaagaz AI proves I can build around messy Indian documents and validation rules, the FlyRank capstone proves I can evaluate a model honestly, and DMDW proves I can do the unglamorous data-warehouse work underneath the AI.

## My AI toolkit

| Tool | What I use it for |
|---|---|
| Claude | Long-form reasoning, code review, and drafting — I give it my real project facts and make it argue against my first draft. |
| ChatGPT | Quick second opinions, alternative phrasings, and fast prototyping of small code pieces. |
| Gemini | Inside my own products — COGNIVA and Kaagaz AI both run on a Hugging Face + Google Gemini pipeline for language understanding and extraction. |
| Perplexity | Research with sources — checking facts, tools and approaches before I commit to them in a project. |

The rule across all four: the tool drafts, I verify. Numbers in my work come from my own runs and held-out data, never from a chatbot's answer.

## Pressure test

**Prompt I would actually run on this sitemap:**

> "Here is my portfolio sitemap: Home, Cases (COGNIVA, Kaagaz AI, FlyRank ML capstone, DMDW), About, Contact. I am a B.Tech CS student who also works as an AI Engineer. Attack this structure. What would a hiring manager or a client fail to find in the first 60 seconds? What is missing, what is redundant, and what should the first screen prove? Be specific, don't be polite."

**Output (sample response, generated for this exercise):**

The attack came back with three points I had to take seriously. First, the sitemap buries the proof: a visitor lands on Home and has to click into Cases before seeing a single number, so the summary recommended moving the strongest measured result — the FlyRank model's 0.68 vs 0.24 Precision@50 — onto the first screen itself. Second, the four cases look equal in the tree but they are not equal in weight: COGNIVA has a live demo and the FlyRank capstone has verified scores, while Kaagaz AI and DMDW are quieter, so the structure should rank the cases instead of listing them flat. Third, Contact is a dead end with no reason to write — it needs one line saying what I am open to (internships, freelance builds, collaborations) so the visitor knows what a message would start. What I changed after this: the home page now leads with the claim plus one measured result, the cases are ordered by strength of evidence, and the contact section states what I am open to.
