# Day 07 — DocChat (RAG over real PDFs)
Saturday, June 6, 2026 · Project 2 of 5

> **Activate your venv first.** Run `source .venv/bin/activate` (Windows: `.venv\Scripts\activate`) before installing or running anything today — your prompt should show `(.venv)`. Do all work inside the venv.

## Today's goal
Chunk the documents thoughtfully.

## Learn first (~30 min)
Recursive chunking, overlap, and how chunk size changes retrieval.

## Tasks
- [x] Implement recursive character chunking with overlap.
- [x] Try 3 chunk sizes (e.g. ~300 / 600 / 1000 chars) and print sample chunks to compare.
- [x] Attach metadata (source filename, page) to every chunk.

## Files you'll create / touch
- `src/project2_docchat/chunk.py`

## Definition of done
Documents are split into chunks carrying metadata, and you can articulate the size tradeoff.

## If you get stuck (the 30-minute rule)
Use LangChain's `RecursiveCharacterTextSplitter` as a utility — fine to borrow even before framework week.

## Notes / scratchpad
- Hand-rolled recursive splitter (~50 lines): tries \n\n → \n → space → char-level.
- Results: 300→780 chunks (avg 307), 600→363 chunks (avg 629), 1000→223 chunks (avg 1055).
- Chose 600/100: fits 2–3 complete sentences, clean embedding signal, ~363 chunks is fast enough for Chroma.
- Tradeoff: small chunks = precise but context-poor; large chunks = richer context but diluted embedding.



## End of day
- [x] Ran inside the **activated venv** (`(.venv)` visible) and `python ...` works
- [x] Committed to git with a real message
- [x] Checked off today's tasks above and updated PROGRESS.md
