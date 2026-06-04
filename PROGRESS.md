# PROGRESS

Update this as you go. Tick a day when its **definition of done** is met.
This whole plan is designed to run for **$0** — no credit card, no cloud bill.

## Goals

- [x] **G0 — Launchpad** (Day 1)
- [x] **G1 — Mini-RAG** (Days 2–5)
- [ ] **G2 — DocChat** (Days 6–12)
- [ ] **G3 — DocChat Pro** (Days 13–19)
- [ ] **G4 — Served free** (Days 20–26)
- [ ] **G5 — Capstone** (Days 27–30)

## Daily log

| ✓ | Day | Date | Project | Focus | Notes |
|---|-----|------|---------|-------|-------|
| [x] | 01 | Sun May 31 | Launchpad | Launchpad | venv (Python 3.13), hello_llm.py (Groq fallback), embed_demo.py — all passing |
| [x] | 02 | Mon Jun 1 | Mini-RAG | Build the mini-RAG from scratch | corpus.py (30 snippets), build_index.py -> index.pkl (30x384) — round-trips OK |
| [x] | 03 | Tue Jun 2 | Mini-RAG | Build the mini-RAG from scratch | retrieve.py — top-k cosine similarity, 5 test questions all correct |
| [x] | 04 | Wed Jun 3 | Mini-RAG | Build the mini-RAG from scratch | rag.py — grounded answers via Groq, 'I don't know' for out-of-corpus |
| [x] | 05 | Thu Jun 4 | Mini-RAG | Build the mini-RAG from scratch | Streamlit app — question box, retrieved chunks + scores; G1 complete |
| [x] | 06 | Fri Jun 5 | DocChat | Cited RAG over PDFs + reranking | load_docs.py — 47 pages from 3 arxiv PDFs (attention, rag, dpr); clean text + page numbers |
| [ ] | 07 | Sat Jun 6 | DocChat | Cited RAG over PDFs + reranking | |
| [ ] | 08 | Sun Jun 7 | DocChat | Cited RAG over PDFs + reranking | |
| [ ] | 09 | Mon Jun 8 | DocChat | Cited RAG over PDFs + reranking | |
| [ ] | 10 | Tue Jun 9 | DocChat | Cited RAG over PDFs + reranking | |
| [ ] | 11 | Wed Jun 10 | DocChat | Cited RAG over PDFs + reranking | |
| [ ] | 12 | Thu Jun 11 | DocChat | Cited RAG over PDFs + reranking | |
| [ ] | 13 | Fri Jun 12 | DocChat Pro | Conversational agent + eval suite | |
| [ ] | 14 | Sat Jun 13 | DocChat Pro | Conversational agent + eval suite | |
| [ ] | 15 | Sun Jun 14 | DocChat Pro | Conversational agent + eval suite | |
| [ ] | 16 | Mon Jun 15 | DocChat Pro | Conversational agent + eval suite | |
| [ ] | 17 | Tue Jun 16 | DocChat Pro | Conversational agent + eval suite | |
| [ ] | 18 | Wed Jun 17 | DocChat Pro | Conversational agent + eval suite | |
| [ ] | 19 | Thu Jun 18 | DocChat Pro | Conversational agent + eval suite | |
| [ ] | 20 | Fri Jun 19 | Serve free | Free serving: gateway, guardrails, observability | |
| [ ] | 21 | Sat Jun 20 | Serve free | Free serving: gateway, guardrails, observability | |
| [ ] | 22 | Sun Jun 21 | Serve free | Free serving: gateway, guardrails, observability | |
| [ ] | 23 | Mon Jun 22 | Serve free | Free serving: gateway, guardrails, observability | |
| [ ] | 24 | Tue Jun 23 | Serve free | Free serving: gateway, guardrails, observability | |
| [ ] | 25 | Wed Jun 24 | Serve free | Free serving: gateway, guardrails, observability | |
| [ ] | 26 | Thu Jun 25 | Serve free | Free serving: gateway, guardrails, observability | |
| [ ] | 27 | Fri Jun 26 | Capstone | Polished, documented capstone | |
| [ ] | 28 | Sat Jun 27 | Capstone | Polished, documented capstone | |
| [ ] | 29 | Sun Jun 28 | Capstone | Polished, documented capstone | |
| [ ] | 30 | Mon Jun 29 | Capstone | Polished, documented capstone | |

## Checkpoints
- [x] **Day 5:** mini-RAG works by hand
- [ ] **Day 12:** cited answers over real PDFs with reranking
- [ ] **Day 19:** conversational agent with recorded eval scores
- [ ] **Day 26:** served on the free stack with gateway, guardrails, observability + cost logging
- [ ] **Day 30:** capstone shipped + documented
