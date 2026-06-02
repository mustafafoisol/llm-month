# Day 10 — DocChat (RAG over real PDFs)
Tuesday, June 9, 2026 · Project 2 of 5

> **Activate your venv first.** Run `source .venv/bin/activate` (Windows: `.venv\Scripts\activate`) before installing or running anything today — your prompt should show `(.venv)`. Do all work inside the venv.

## Today's goal
Add hybrid (semantic + keyword) search.

## Learn first (~30 min)
Dense vs sparse/BM25 retrieval and why combining helps.

## Tasks
- [ ] Add a keyword/BM25 retriever (e.g. `rank_bm25`).
- [ ] Merge dense + keyword results with simple score fusion or interleaving.
- [ ] Compare hybrid vs pure-semantic on 5 queries and note where keyword search helped.

## Files you'll create / touch
- `src/project2_docchat/hybrid.py`

## Definition of done
Hybrid retrieval runs and you've documented at least one query where keyword matching mattered.

## If you get stuck (the 30-minute rule)
If this eats a whole day, ship semantic + reranker only and log hybrid search as a known gap.

## Notes / scratchpad
_Fill this in as you work: decisions made, blockers hit, useful links._



## End of day
- [ ] Ran inside the **activated venv** (`(.venv)` visible) and `python ...` works
- [ ] Committed to git with a real message
- [ ] Checked off today's tasks above and updated PROGRESS.md
