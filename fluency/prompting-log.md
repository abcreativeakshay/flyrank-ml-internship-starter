# FL-02 — Prompting Log

**Task:** Summarise a long project report into a one-page brief.
**Source I used:** my COGNIVA semester project report — a multilingual (English, Hindi, Marathi) voice-first dementia-care companion and clinical care platform, built with the Peakso team for dementia/Alzheimer's patients, family caregivers, and healthcare providers, using a hybrid Hugging Face + Google Gemini pipeline. The report covers the problem, the system design, the voice and language pipeline, evaluation results (including an intent/language probe and a smoke-test classifier), and limitations.
**Rule for every version:** the brief must not contain a single fact that is not in the report.

---

## Version 1 — the naive ask

**Prompt:** "Summarise this report."

**Output (excerpt):**
> This report presents an innovative AI-powered healthcare solution leveraging cutting-edge technology to revolutionise dementia care through a state-of-the-art multilingual platform…

**Note — what changed and why:** Nothing yet; this is the baseline. It produced generic filler ("innovative", "cutting-edge", "revolutionise") and almost no actual content from the report. A summary that could describe any project describes none.

## Version 2 — set the length and the reader

**Prompt:** "Summarise this report in at most 250 words, for a professor who will read it in two minutes before a viva."

**Output (excerpt):**
> COGNIVA is a voice-first companion for dementia and Alzheimer's patients that works in English, Hindi, and Marathi. Patients speak instead of typing; caregivers and doctors get a clinical view of the same data. The system uses Hugging Face models with Google Gemini in a hybrid pipeline…

**Note:** Adding a word limit and a named reader killed most of the filler. The summary now leads with what the system is and who it serves. Still missing: results and limitations — the two things a professor asks about first.

## Version 3 — force a structure

**Prompt:** "Summarise this report in at most 250 words for a professor. Use exactly four labelled parts: Problem, What we built, Results, Limitations. Only use facts from the report."

**Output (excerpt):**
> **Problem:** Dementia patients struggle with text-heavy apps, and most tools are English-only, while families here speak Hindi and Marathi. **What we built:** A voice-first companion and care platform in three languages… **Results:** … **Limitations:** …

**Note:** A fixed structure guarantees coverage — nothing important can be silently dropped. This is the single biggest improvement in the log. The results section was still vague ("performed well"), which leads to the next fix.

## Version 4 — demand the real numbers

**Prompt:** "Same four-part brief, at most 250 words. In Results, use the actual numbers from the report (probe size, intent and language accuracy, test counts). If a number is a smoke test only, say so. Never round up or invent a figure."

**Output (excerpt):**
> **Results:** On a probe of 74 cases, intent recognition was 98.6% and language handling 95.9%; 32 of 32 functional tests passed. The multimodal classifier reached a Macro-F1 of 0.500 — that figure is from a smoke test only, not a full evaluation.

**Note:** Numbers make a brief checkable, and the "say so if it's a smoke test" clause stopped the model from presenting a weak result as a strong one. That honesty clause now stays in every version.

## Version 5 — cut the sales language

**Prompt:** "Rewrite the four-part brief in plain words. Remove adjectives like innovative, seamless, robust, and cutting-edge unless the report itself uses them. Keep all numbers exactly as they are."

**Output (excerpt):**
> **What we built:** A voice-first app for dementia patients in English, Hindi, and Marathi. The patient talks; the app responds by voice and keeps a record that family caregivers and doctors can see. It uses Hugging Face models for on-device tasks and Google Gemini for harder language work.

**Note:** Stripping adjectives forced the writing onto facts and mechanism ("on-device tasks" vs "harder language work" explains the hybrid design better than "cutting-edge pipeline" did). Readability went up, length went down.

## Version 6 — fit the one-page brief format

**Prompt:** "Final version: a one-page brief. Title line, then the four labelled parts, at most 220 words total, plain words, exact numbers, honesty flags kept. End with one line: 'Full report available on request.'"

**Output (the full brief):**
> **COGNIVA — Dementia Care Companion: one-page brief**
> **Problem:** Dementia and Alzheimer's patients often cannot use text-heavy apps, and most care tools are English-only. In the families this was built for, Hindi and Marathi are the everyday languages.
> **What we built:** A voice-first companion and clinical care platform in English, Hindi, and Marathi. The patient speaks; caregivers and healthcare providers see the same record in a clinical view. The pipeline is hybrid: Hugging Face models plus Google Gemini.
> **Results:** Probe of 74 cases: intent 98.6%, language 95.9%. Functional tests: 32 of 32 passed. Classifier Macro-F1 0.500 — smoke test only.
> **Limitations:** Database rules are still permissive and need hardening; no formal usability (SUS) study has been collected yet.
> Full report available on request.

**Note:** The word budget plus the fixed structure produced a brief I could actually hand to someone. Every number in it is traceable to the report, and the weak result is labelled as weak.

---

## Final reusable template

```
Summarise the attached report into a one-page brief.
- At most 220 words, plain words, no sales adjectives.
- Exactly four labelled parts: Problem / What we built / Results / Limitations.
- In Results, use the report's exact numbers. Never invent, round up,
  or strengthen a figure. If a result is a pilot or smoke test, say so.
- Every fact must come from the report. If the report does not say it,
  leave it out.
- End with: "Full report available on request."
```

## Cross-model comparison — to complete

This section is **not done yet, on purpose**. A real cross-model comparison means running the same final prompt above on the same report in my own Claude and ChatGPT accounts and comparing what comes back. I will not write up outputs from a model I did not actually run — an invented comparison would teach me nothing and would be dishonest in a log that is specifically about checking outputs.

**Ready to use when I run it — comparison criteria:**
- **Accuracy to source:** does every number and claim match the report exactly? Any invented or rounded figures?
- **Tone:** plain words, or does it drift into sales language ("innovative", "seamless")?
- **Structure:** does it keep the four labelled parts and the word limit without being reminded?
- **Honesty flags:** does it keep the "smoke test only" label on the weak result on its own?
