# Day 04 — Mini-RAG (from scratch)
Wednesday, June 3, 2026 · Project 1 of 5

> **Activate your venv first.** Run `source .venv/bin/activate` (Windows: `.venv\Scripts\activate`) before installing or running anything today — your prompt should show `(.venv)`. Do all work inside the venv.

## Today's goal
Generate answers grounded in retrieved context, with sources.

## Learn first (~30 min)
Prompt construction; grounding ('answer only from the context'); what hallucination looks like.

## Tasks
- [x] Write `answer(question)`: retrieve k chunks, build a prompt instructing the model to answer ONLY from the context and say 'I don't know' otherwise.
- [x] Return the answer plus the source snippets that were used.
- [x] Test a question whose answer is NOT in the corpus and confirm it says it doesn't know instead of inventing one.

## Files you'll create / touch
- `src/project1_mini_rag/rag.py`

## Definition of done
Answers are grounded in your snippets, and an out-of-corpus question yields 'I don't know'.

## If you get stuck (the 30-minute rule)
If grounding is weak, tighten the system instruction and drop temperature toward 0.

## Notes / scratchpad
_Fill this in as you work: decisions made, blockers hit, useful links._



## End of day
- [x] Ran inside the **activated venv** (`(.venv)` visible) and `python ...` works
- [x] Committed to git with a real message
- [x] Checked off today's tasks above and updated PROGRESS.md
