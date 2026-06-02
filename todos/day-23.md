# Day 23 — Serve it for free
Monday, June 22, 2026 · Project 4 of 5

> **Activate your venv first.** Run `source .venv/bin/activate` (Windows: `.venv\Scripts\activate`) before installing or running anything today — your prompt should show `(.venv)`. Do all work inside the venv.

## Today's goal
Add input/output guardrails — the free, open-source replacement for Bedrock Guardrails.

## Learn first (~30 min)
Content/topic filtering, PII redaction, jailbreak/safety classification.

## Tasks
- [ ] Add Guardrails AI (or NeMo Guardrails) to validate/structure outputs and block a disallowed topic.
- [ ] Add PII detection + redaction (Guardrails validators or Microsoft Presidio — both run locally, free).
- [ ] Optional: classify unsafe input/output with Llama Guard hosted on Groq's free tier (no local model needed).
- [ ] Test that a disallowed prompt is blocked and a PII-containing prompt is redacted.

## Files you'll create / touch
- `src/project4_serving/guardrails.py`

## Definition of done
Guardrails demonstrably block a disallowed topic and redact PII.

## If you get stuck (the 30-minute rule)
A focused regex PII redactor plus a simple topic-refusal check is enough to learn the pattern.

## Notes / scratchpad
_Fill this in as you work: decisions made, blockers hit, useful links._



## End of day
- [ ] Ran inside the **activated venv** (`(.venv)` visible) and `python ...` works
- [ ] Committed to git with a real message
- [ ] Checked off today's tasks above and updated PROGRESS.md
