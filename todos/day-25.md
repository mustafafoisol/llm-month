# Day 25 — Serve it for free
Wednesday, June 24, 2026 · Project 4 of 5

> **Activate your venv first.** Run `source .venv/bin/activate` (Windows: `.venv\Scripts\activate`) before installing or running anything today — your prompt should show `(.venv)`. Do all work inside the venv.

## Today's goal
Measure tokens, latency, and what this WOULD cost at scale — cost discipline without a bill.

## Learn first (~30 min)
Token accounting; estimating cost even when you're running for free.

## Tasks
- [ ] Log input/output tokens and response time per query (free, since you're local / free-tier).
- [ ] Build a small estimator: 'at $X per 1M tokens on a paid API/Bedrock, 1,000 queries would cost ~$Y'.
- [ ] Identify your most expensive step and apply one optimization (smaller model for routing, prompt trimming, or caching).

## Files you'll create / touch
- `src/project4_serving/cost_report.py`

## Definition of done
A per-query tokens/latency log plus a cost-at-scale estimate table.

## If you get stuck (the 30-minute rule)
If your free provider doesn't return token usage, count tokens with a tokenizer library to estimate.

## Notes / scratchpad
_Fill this in as you work: decisions made, blockers hit, useful links._



## End of day
- [ ] Ran inside the **activated venv** (`(.venv)` visible) and `python ...` works
- [ ] Committed to git with a real message
- [ ] Checked off today's tasks above and updated PROGRESS.md
