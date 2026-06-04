# Day 06 — DocChat (RAG over real PDFs)
Friday, June 5, 2026 · Project 2 of 5

> **Activate your venv first.** Run `source .venv/bin/activate` (Windows: `.venv\Scripts\activate`) before installing or running anything today — your prompt should show `(.venv)`. Do all work inside the venv.

## Today's goal
Ingest real PDFs: load and extract text with page numbers.

## Learn first (~30 min)
Document loaders; common text-extraction quirks.

## Tasks
- [x] Pick 3–5 real, text-based PDFs (docs, papers, manuals). Put them in `data/`.
- [x] Extract text per page and keep the page number with each piece.
- [x] Inspect the output for garbage characters and note any extraction issues.

## Files you'll create / touch
- `src/project2_docchat/load_docs.py`
- `src/project2_docchat/data/`

## Definition of done
Reasonably clean text plus page numbers extracted from every PDF.

## If you get stuck (the 30-minute rule)
Use `pypdf`. If a PDF is scanned (image-only), swap it for a text-based one — OCR is out of scope this week.

## Notes / scratchpad
- Used `pypdf 6.12.2` — straightforward, no issues on text-based PDFs.
- PDFs: attention.pdf (15p), dpr.pdf (13p), rag.pdf (19p) = 47 pages total.
- All pages have readable text; no empty or garbage pages detected.
- Windows console needs `PYTHONIOENCODING=utf-8` (or `sys.stdout.reconfigure`) to handle Unicode chars like ∗ in math papers.



## End of day
- [x] Ran inside the **activated venv** (`(.venv)` visible) and `python ...` works
- [x] Committed to git with a real message
- [x] Checked off today's tasks above and updated PROGRESS.md
