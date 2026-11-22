# Frame It as Cases

## Voice card

- I write plain. Short sentences, real words, no buzzword stuffing.
- Numbers over adjectives: if I can't measure it, I say what it does instead of calling it "powerful" or "cutting-edge".
- I name the tools and the data honestly, including what didn't work.
- If a result came from held-out data or a public leaderboard, I say so — that's what makes it believable.

## Case 1 — COGNIVA

- **Problem:** Dementia and Alzheimer's patients in India are cared for mostly by family members, often in Hindi or Marathi, and most care apps assume an English-speaking user who can type and navigate menus.
- **What I built:** With the Peakso team, a multilingual (English, Hindi, Marathi) voice-first dementia-care companion and clinical care platform for patients, family caregivers and healthcare providers, running a hybrid Hugging Face + Google Gemini AI pipeline. Voice-first because the person using it may not be able to type.
- **Evidence:** A working live demo is public at dementia-care-companion.peaksotech.workers.dev — anyone can open it and try the voice flow in three languages.
- **What it proves:** I can build AI for users who are not like me — older, non-English-speaking, low-tech-confidence — and still ship it to a live URL.

## Case 2 — Kaagaz AI

- **Problem:** Indian businesses drown in paper and scans — GST invoices, KYC documents, claims, bank statements — and someone has to type the fields into a system by hand, in Hindi, Marathi or English.
- **What I built:** A document-to-data platform: upload a PDF, scan or phone photo of an Indian document, and Gemini extracts the structured fields, with India-specific validation on top — GSTIN format checks, invoice-math reconciliation, and duplicate detection.
- **Evidence:** The validation layer is the honest part of this case: extraction alone is a demo, but checking a GSTIN and reconciling invoice totals against the extracted line items is what makes the output usable without re-typing it.
- **What it proves:** I think about the checks around a model, not just the model — an AI output you can't trust is just faster typing errors.

## Case 3 — FlyRank ML Capstone

- **Problem:** Given search-intelligence data for many client sites, rank the content pages most likely to be declining, so a team knows what to refresh first — and prove the ranking is real, not leakage.
- **What I built:** A full ML pipeline on the FlyRank starter repo: research question and lane framing, a data contract, a transparent points-based baseline, then a Random Forest model, a validation audit, and a weekly action playbook.
- **Evidence:** On a client-holdout split (whole clients held out, so the model can't memorise a site), the Random Forest scored **Precision@50 of 0.68 and AUC 0.747**, against **0.24** for the hand-rule baseline. The trend columns in the data are leakage and were never used as features — the validation audit is in the repo for anyone to check.
- **What it proves:** I evaluate like a sceptic. The score I report is the one from the split designed to make my model look worse, not better.

## Case 4 — DMDW: Healthcare Data Warehouse and Dashboards

- **Problem:** Hospital data sits in operational tables that are fine for running a hospital and useless for answering questions like "which departments are busiest, and what happens next month?"
- **What I built:** A healthcare data warehouse with dashboards on top — Snowflake as the warehouse, Streamlit for the dashboard apps — covering the warehouse design, OLAP-style analysis and the jury project work built on it.
- **Evidence:** Working dashboard apps, built end to end: data modelled in the warehouse, queries behind every chart, and a front end a non-technical viewer can actually use.
- **What it proves:** I can do the data engineering underneath the AI — schemas, warehouses and dashboards, not just notebooks.

## Before / after

**Before (generic AI-sounding line):**

> "Leveraging cutting-edge artificial intelligence and state-of-the-art machine learning algorithms, I developed a powerful, innovative solution that revolutionises content optimisation and delivers unparalleled insights."

**After (my edit):**

> "I built a model that ranks which web pages are declining. On clients the model had never seen, 34 of its top 50 picks were right — the hand-written rule it replaced got 12."
