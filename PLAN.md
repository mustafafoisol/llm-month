# LLM Engineering — 30-Day Project-Based Plan (Free Stack)

**Start:** Sunday, May 31, 2026 → **End:** Monday, June 29, 2026
**Shape:** 5 escalating projects + 1 capstone, all growing inside this one repo.
**Cost:** Designed to run end-to-end for **$0** — no credit card, no cloud bill.

This is the master plan. Each day has its own task file in [`todos/`](./todos). Track overall
progress in [`PROGRESS.md`](./PROGRESS.md). Claude Code reads [`CLAUDE.md`](./CLAUDE.md) for context.

---

## The 6 goals (your scoreboard)

| Goal | What you ship | Days |
|------|---------------|------|
| **G0 — Launchpad** | Env that calls an LLM + computes embeddings | 1 |
| **G1 — Mini-RAG** | Semantic search + grounded answers, no framework | 2–5 |
| **G2 — DocChat** | RAG over real PDFs via a vector DB, with reranking | 6–12 |
| **G3 — DocChat Pro** | Conversational RAG agent (LangChain/LangGraph) + eval suite | 13–19 |
| **G4 — Served free** | Same app on a free serving stack: gateway, guardrails, observability | 20–26 |
| **G5 — Capstone** | One polished, deployed, documented, demo-ready app | 27–30 |

---

## Ground rules (what keeps this fool-proof)

1. **Always work inside the venv.** Day 1 creates `.venv`. Before installing or running ANYTHING — every day, every new terminal — activate it: `source .venv/bin/activate` (Windows: `.venv\Scripts\activate`). Your prompt should show `(.venv)`. Never install into the system Python.
2. **One repo, grown daily.** Never start from a blank folder. By Day 30 this repo *is* your capstone.
3. **Ship something runnable every day.** If `python ...` doesn't run (inside the venv) at end of day, the day isn't done.
4. **Commit daily** with a real message — your git history is proof of work.
5. **The 30-minute rule.** Stuck for 30 min? Use that day's documented Fallback and keep moving.
6. **Daily rhythm (~2–3 hrs):** ~30 min learning the concept, the rest building. Building is the point.
7. **Defaults are pre-decided** (below) so you never lose a day choosing tools.

### Default stack (all free)
- **Python 3.11+** in a virtualenv; secrets in `.env` (gitignored)
- **LLM (chat):** free hosted API tiers — **Gemini**, **Groq**, or **Cerebras** (no credit card, no install)
- **Embeddings + reranker:** `sentence-transformers` (a pip package that runs on your CPU — free, offline, not a model server)
- **Vector DB:** Chroma (local). Optional free managed feel: Supabase pgvector or Qdrant via Docker
- **Framework:** LangChain + LangGraph (introduced Week 3, not before)
- **Guardrails:** Guardrails AI / NeMo Guardrails (+ optional Llama Guard on Groq's free tier)
- **Eval / observability:** Ragas + Langfuse (self-host via Docker or free cloud tier)
- **UI:** Streamlit
- **No cloud account required.** Week 4 teaches Bedrock's concepts using free, self-hostable tools.
- **Free-tier tip:** hosted tiers rate-limit (Gemini ~1,500 req/day, Groq ~30 req/min, Cerebras generous daily tokens). Keep eval sets small, let Day 26's retry/fallback logic absorb 429s, and stack a second provider when you hit a wall.

---

## Project map

### Project 0 — Launchpad (Day 1)
Environment works end-to-end. → [day-01](./todos/day-01.md)

### Project 1 — Mini-RAG from scratch (Days 2–5)
Build retrieval + grounded answering by hand so you understand what the tools later hide.
→ [day-02](./todos/day-02.md) → [day-05](./todos/day-05.md)

### Project 2 — DocChat: RAG over real PDFs (Days 6–12)
Real ingestion, chunking, a vector DB, hybrid search, reranking, cited answers.
→ [day-06](./todos/day-06.md) → [day-12](./todos/day-12.md)

### Project 3 — DocChat Pro: agent + evaluation (Days 13–19)
LangChain/LCEL, memory, query rewriting, LangGraph, a tool, and an eval suite with tracing.
→ [day-13](./todos/day-13.md) → [day-19](./todos/day-19.md)

### Project 4 — Serve it for free (Days 20–26)
The same production concepts as AWS Bedrock — a model gateway, managed-style RAG, guardrails,
observability, cost-awareness, reliability — using a **completely free** stack
(free hosted API tiers + Chroma/pgvector + Guardrails AI + Langfuse).
→ [day-20](./todos/day-20.md) → [day-26](./todos/day-26.md)

### Project 5 — Capstone (Days 27–30)
Integrate, polish, deploy, document, demo.
→ [day-27](./todos/day-27.md) → [day-30](./todos/day-30.md)

---

## Weekly checkpoints (are you on track?)

- **End of Day 5:** RAG works by hand. *If not, finish it before starting Project 2.*
- **End of Day 12:** Cited answers over real PDFs with reranking.
- **End of Day 19:** Conversational agent with recorded eval scores.
- **End of Day 26:** Served on the free stack with gateway, guardrails, observability + cost logging.
- **End of Day 30:** Capstone shipped and documented.

## What actually makes you hireable
The code is table stakes. What lands the job is being able to say **why** — why that chunk size,
why a reranker, why RAG instead of fine-tuning, when a paid managed service (like Bedrock) is worth
its cost vs a self-hosted stack. Capture every such decision in your README as you make it.
That's your interview, pre-written.

> Optional, later: if you specifically want "deployed on AWS" experience, you can port Week 4 to
> Bedrock — but set an AWS Budget alert first, and use **S3 Vectors** (not OpenSearch Serverless,
> which bills ~$350/month even idle) for any Knowledge Base.
