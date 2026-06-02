# Day 02 — Mini-RAG (from scratch)
Monday, June 1, 2026 · Project 1 of 5

> **Activate your venv first.** Run `source .venv/bin/activate` (Windows: `.venv\Scripts\activate`) before installing or running anything today — your prompt should show `(.venv)`. Do all work inside the venv.

## Today's goal
Build and persist a small embedded corpus you can search.

## Learn first (~30 min)
Why semantic search beats keyword search; batching embeddings.

## Tasks
- [x] Gather ~30 short text snippets you care about (notes, an FAQ, doc paragraphs) into `corpus.py` or a json file.
- [x] Write `build_index.py` to embed all snippets in a batch.
- [x] Store (text, vector) pairs and save to disk (pickle or json) so you never re-embed.
- [x] Reload the saved index and print count + vector dimension to confirm it round-trips.

## Files you'll create / touch
- `src/project1_mini_rag/corpus.py`
- `src/project1_mini_rag/build_index.py`
- `src/project1_mini_rag/index.pkl`

## Definition of done
`index.pkl` holds 30 embedded snippets and reloads correctly without re-embedding.

## If you get stuck (the 30-minute rule)
If file persistence misbehaves, keep the index in memory and rebuild each run — 30 items is cheap.

## Notes / scratchpad
_Fill this in as you work: decisions made, blockers hit, useful links._



## End of day
- [x] Ran inside the **activated venv** (`(.venv)` visible) and `python ...` works
- [ ] Committed to git with a real message
- [x] Checked off today's tasks above and updated PROGRESS.md
