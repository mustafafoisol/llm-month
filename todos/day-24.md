# Day 24 — Serve it for free
Tuesday, June 23, 2026 · Project 4 of 5

> **Activate your venv first.** Run `source .venv/bin/activate` (Windows: `.venv\Scripts\activate`) before installing or running anything today — your prompt should show `(.venv)`. Do all work inside the venv.

## Today's goal
See inside your app with tracing — the free replacement for LangSmith/CloudWatch.

## Learn first (~30 min)
Tracing spans; why observability is non-negotiable for LLM apps.

## Tasks
- [ ] Run Langfuse locally via Docker (or use its free cloud tier) and get keys.
- [ ] Instrument your app to log traces: retrieval -> prompt -> model -> output.
- [ ] Inspect a few traces and find one slow or low-quality step.

## Files you'll create / touch
- `src/project4_serving/tracing.py`

## Definition of done
Traces for your queries show up in Langfuse and you can inspect a full request end to end.

## If you get stuck (the 30-minute rule)
Structured JSONL logging + a tiny viewer script works if Docker/Langfuse fights you.

## Notes / scratchpad
_Fill this in as you work: decisions made, blockers hit, useful links._



## End of day
- [ ] Ran inside the **activated venv** (`(.venv)` visible) and `python ...` works
- [ ] Committed to git with a real message
- [ ] Checked off today's tasks above and updated PROGRESS.md
