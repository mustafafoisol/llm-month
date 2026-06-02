# Day 03 — Mini-RAG (from scratch)
Tuesday, June 2, 2026 · Project 1 of 5

> **Activate your venv first.** Run `source .venv/bin/activate` (Windows: `.venv\Scripts\activate`) before installing or running anything today — your prompt should show `(.venv)`. Do all work inside the venv.

## Today's goal
Implement top-k retrieval over your corpus.

## Learn first (~30 min)
Nearest-neighbour search by cosine similarity; what 'top-k' means.

## Tasks
- [x] Write `retrieve(question, k=3)`: embed the query, score it against every snippet, return the top-k with their scores.
- [x] Test with 5 questions and eyeball whether the right snippet comes back on top.
- [x] Print the scores so you can see the separation between good and bad matches.

## Files you'll create / touch
- `src/project1_mini_rag/retrieve.py`

## Definition of done
`retrieve()` returns sensible top-3 snippets for each of your 5 test questions.

## If you get stuck (the 30-minute rule)
A brute-force loop over all 30 snippets is totally fine — no vector index needed at this scale.

## Notes / scratchpad
_Fill this in as you work: decisions made, blockers hit, useful links._



## End of day
- [x] Ran inside the **activated venv** (`(.venv)` visible) and `python ...` works
- [ ] Committed to git with a real message
- [x] Checked off today's tasks above and updated PROGRESS.md
