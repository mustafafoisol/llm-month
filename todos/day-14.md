# Day 14 — DocChat Pro (agent + eval)
Saturday, June 13, 2026 · Project 3 of 5

> **Activate your venv first.** Run `source .venv/bin/activate` (Windows: `.venv\Scripts\activate`) before installing or running anything today — your prompt should show `(.venv)`. Do all work inside the venv.

## Today's goal
Make it conversational with memory and query rewriting.

## Learn first (~30 min)
Chat history; condensing a follow-up into a standalone question.

## Tasks
- [ ] Add conversation memory (message history).
- [ ] Add a query-rewriting step that turns a follow-up + history into a standalone search query.
- [ ] Test a 3-turn conversation with a pronoun follow-up like 'what about its limits?'.

## Files you'll create / touch
- `src/project3_docchat_pro/conversational.py`

## Definition of done
Follow-up questions retrieve the right context because they're rewritten into standalone queries.

## If you get stuck (the 30-minute rule)
Manually concatenate history into the query if the memory abstraction trips you up.

## Notes / scratchpad
_Fill this in as you work: decisions made, blockers hit, useful links._



## End of day
- [ ] Ran inside the **activated venv** (`(.venv)` visible) and `python ...` works
- [ ] Committed to git with a real message
- [ ] Checked off today's tasks above and updated PROGRESS.md
