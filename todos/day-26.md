# Day 26 — Serve it for free
Thursday, June 25, 2026 · Project 4 of 5

> **Activate your venv first.** Run `source .venv/bin/activate` (Windows: `.venv\Scripts\activate`) before installing or running anything today — your prompt should show `(.venv)`. Do all work inside the venv.

## Today's goal
Make the app robust: retries, multi-provider fallback, and rejecting ungrounded answers. (Goal G4 done.)

## Learn first (~30 min)
Graceful failure; using your gateway for provider fallback; output validation.

## Tasks
- [ ] Add retries with backoff on errors and rate limits (free tiers DO rate-limit, so this matters).
- [ ] Use your Day-20 gateway to fall back to a second backend when the first fails or 429s.
- [ ] Validate output: flag/reject answers not grounded in the retrieved context. Tick Goal G4 in PROGRESS.md.

## Files you'll create / touch
- `src/project4_serving/reliability.py`

## Definition of done
The app survives an induced failure (kill the primary backend) by falling back, and flags an ungrounded answer.

## If you get stuck (the 30-minute rule)
A minimal try/except plus one fallback backend is enough to satisfy this.

## Notes / scratchpad
_Fill this in as you work: decisions made, blockers hit, useful links._



## End of day
- [ ] Ran inside the **activated venv** (`(.venv)` visible) and `python ...` works
- [ ] Committed to git with a real message
- [ ] Checked off today's tasks above and updated PROGRESS.md
