# Day 08 — DocChat (RAG over real PDFs)
Sunday, June 7, 2026 · Project 2 of 5

> **Activate your venv first.** Run `source .venv/bin/activate` (Windows: `.venv\Scripts\activate`) before installing or running anything today — your prompt should show `(.venv)`. Do all work inside the venv.

## Today's goal
Stand up Chroma and ingest your chunks.

## Learn first (~30 min)
Vector DBs, collections, persistence.

## Tasks
- [x] Install and initialise Chroma with a persistent directory.
- [x] Embed and add all chunks with their metadata and stable ids.
- [x] Confirm the collection count and that it persists across restarts.

## Files you'll create / touch
- `src/project2_docchat/ingest.py`
- `src/project2_docchat/chroma_db/`

## Definition of done
Chroma holds all your chunks and you can reopen it without re-ingesting.

## If you get stuck (the 30-minute rule)
Use Chroma in-memory and re-ingest each run if persistence misbehaves.

## Notes / scratchpad
- chromadb 1.5.9; PersistentClient at chroma_db/ (gitignored).
- Collection 'docchat': 363 chunks, IDs like `attention.pdf:p1:c0`.
- get_collection() is idempotent — skips re-ingest if count > 0.
- Sanity query for 'attention mechanism' returns attention.pdf pages as expected.
- HF_TOKEN warning is harmless; model is cached locally after first download.



## End of day
- [x] Ran inside the **activated venv** (`(.venv)` visible) and `python ...` works
- [x] Committed to git with a real message
- [x] Checked off today's tasks above and updated PROGRESS.md
