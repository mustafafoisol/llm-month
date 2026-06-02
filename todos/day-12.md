# Day 12 — DocChat (RAG over real PDFs)
Thursday, June 11, 2026 · Project 2 of 5

> **Activate your venv first.** Run `source .venv/bin/activate` (Windows: `.venv\Scripts\activate`) before installing or running anything today — your prompt should show `(.venv)`. Do all work inside the venv.

## Today's goal
Wire the full pipeline into a cited UI and document. (Goal G2 done.)

## Learn first (~30 min)
Presenting citations (source + page) to the user.

## Tasks
- [ ] Streamlit app: question -> cited answer (answer + source + page) with expandable raw chunks.
- [ ] Connect the full pipeline: load -> chunk -> Chroma -> hybrid -> rerank -> answer.
- [ ] Write the README and tick Goal G2 in PROGRESS.md.

## Files you'll create / touch
- `src/project2_docchat/app.py`
- `src/project2_docchat/README.md`

## Definition of done
Cited answers over your PDFs, you can show reranking's impact, and explain why retrieval is the bottleneck.

## If you get stuck (the 30-minute rule)
Drop the expander UI and just print citations inline if you're short on time.

## Notes / scratchpad
_Fill this in as you work: decisions made, blockers hit, useful links._



## End of day
- [ ] Ran inside the **activated venv** (`(.venv)` visible) and `python ...` works
- [ ] Committed to git with a real message
- [ ] Checked off today's tasks above and updated PROGRESS.md
