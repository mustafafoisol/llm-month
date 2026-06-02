# Day 09 — DocChat (RAG over real PDFs)
Monday, June 8, 2026 · Project 2 of 5

> **Activate your venv first.** Run `source .venv/bin/activate` (Windows: `.venv\Scripts\activate`) before installing or running anything today — your prompt should show `(.venv)`. Do all work inside the venv.

## Today's goal
Build the query path with metadata filtering.

## Learn first (~30 min)
Querying a vector store; filtering by metadata.

## Tasks
- [ ] Write `search(query, k)` that queries Chroma and returns chunks + metadata + distances.
- [ ] Add a metadata filter (e.g. restrict to one source document).
- [ ] Test several queries and verify the filter actually narrows results.

## Files you'll create / touch
- `src/project2_docchat/search.py`

## Definition of done
Queries return relevant chunks, and a filtered query is restricted to the chosen source.

## If you get stuck (the 30-minute rule)
If the filter syntax confuses you, ship unfiltered search first and add filtering later.

## Notes / scratchpad
_Fill this in as you work: decisions made, blockers hit, useful links._



## End of day
- [ ] Ran inside the **activated venv** (`(.venv)` visible) and `python ...` works
- [ ] Committed to git with a real message
- [ ] Checked off today's tasks above and updated PROGRESS.md
