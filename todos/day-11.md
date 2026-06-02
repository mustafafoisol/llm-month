# Day 11 — DocChat (RAG over real PDFs)
Wednesday, June 10, 2026 · Project 2 of 5

> **Activate your venv first.** Run `source .venv/bin/activate` (Windows: `.venv\Scripts\activate`) before installing or running anything today — your prompt should show `(.venv)`. Do all work inside the venv.

## Today's goal
Add a reranker.

## Learn first (~30 min)
Cross-encoder reranking; the retrieve-then-rerank pattern.

## Tasks
- [ ] Add a cross-encoder reranker over your top-N candidates, then take top-k after reranking.
- [ ] Compare answers before vs after reranking on 5 questions.
- [ ] Write down exactly what improved.

## Files you'll create / touch
- `src/project2_docchat/rerank.py`

## Definition of done
Reranking visibly changes ordering and you've documented improvement on at least one question.

## If you get stuck (the 30-minute rule)
Use a small sentence-transformers cross-encoder or a hosted reranker; if it's slow, rerank fewer candidates.

## Notes / scratchpad
_Fill this in as you work: decisions made, blockers hit, useful links._



## End of day
- [ ] Ran inside the **activated venv** (`(.venv)` visible) and `python ...` works
- [ ] Committed to git with a real message
- [ ] Checked off today's tasks above and updated PROGRESS.md
