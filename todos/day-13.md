# Day 13 — DocChat Pro (agent + eval)
Friday, June 12, 2026 · Project 3 of 5

> **Activate your venv first.** Run `source .venv/bin/activate` (Windows: `.venv\Scripts\activate`) before installing or running anything today — your prompt should show `(.venv)`. Do all work inside the venv.

## Today's goal
Rebuild the retriever in LangChain using LCEL.

## Learn first (~30 min)
LangChain components and LCEL piping (retriever | prompt | model | parser).

## Tasks
- [ ] Install LangChain and wrap your Chroma store as a LangChain retriever.
- [ ] Build an LCEL chain: retriever -> prompt -> model -> output parser.
- [ ] Match the answer quality you had on Day 12.

## Files you'll create / touch
- `src/project3_docchat_pro/chain.py`

## Definition of done
The LCEL chain answers with citations at parity with your Day 12 pipeline.

## If you get stuck (the 30-minute rule)
Keep your own retriever; just adopt LangChain for the prompt -> model -> parse portion.

## Notes / scratchpad
_Fill this in as you work: decisions made, blockers hit, useful links._



## End of day
- [ ] Ran inside the **activated venv** (`(.venv)` visible) and `python ...` works
- [ ] Committed to git with a real message
- [ ] Checked off today's tasks above and updated PROGRESS.md
