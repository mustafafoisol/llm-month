# Day 08 — DocChat (RAG over real PDFs)
Sunday, June 7, 2026 · Project 2 of 5

> **Activate your venv first.** Run `source .venv/bin/activate` (Windows: `.venv\Scripts\activate`) before installing or running anything today — your prompt should show `(.venv)`. Do all work inside the venv.

## Today's goal
Stand up Chroma and ingest your chunks.

## Learn first (~30 min)
Vector DBs, collections, persistence.

## Tasks
- [ ] Install and initialise Chroma with a persistent directory.
- [ ] Embed and add all chunks with their metadata and stable ids.
- [ ] Confirm the collection count and that it persists across restarts.

## Files you'll create / touch
- `src/project2_docchat/ingest.py`
- `src/project2_docchat/chroma_db/`

## Definition of done
Chroma holds all your chunks and you can reopen it without re-ingesting.

## If you get stuck (the 30-minute rule)
Use Chroma in-memory and re-ingest each run if persistence misbehaves.

## Notes / scratchpad
_Fill this in as you work: decisions made, blockers hit, useful links._



## End of day
- [ ] Ran inside the **activated venv** (`(.venv)` visible) and `python ...` works
- [ ] Committed to git with a real message
- [ ] Checked off today's tasks above and updated PROGRESS.md
