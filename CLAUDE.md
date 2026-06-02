# CLAUDE.md — context for Claude Code

This repo is a **30-day, project-based LLM engineering bootcamp** designed to run **completely free**
(no credit card, no cloud bill). I'm building one application that grows over 30 days, covering RAG,
vector databases, LangChain/LangGraph, guardrails, and observability.

## How this repo is organised
- `PLAN.md` — the master plan (6 goals, 5 projects + capstone, ground rules, default stack).
- `todos/day-NN.md` — one task file per day: today's goal, a concept to learn, a task checklist,
  files to touch, a definition of done, and a fallback for when I'm stuck.
- `PROGRESS.md` — the running scoreboard: the 6 goals and a row per day. Keep this updated.
- `src/projectN_*/` — code for each project. The repo grows here day by day.

## How to help me each day
1. When I say "let's start day N" (or open `todos/day-NN.md`), **read that day file and the relevant
   `PLAN.md` section first** for context.
2. Help me complete that day's tasks with **runnable code** in the correct `src/projectN_*/` folder.
   Prefer small, working increments over large rewrites. **Make sure the venv is activated before any run/install.**
3. Respect the **definition of done** — don't call it finished until that's met.
4. If I'm blocked, suggest the day's **fallback** rather than rabbit-holing.
5. At end of day, help me verify the code runs, write a meaningful git commit, and check off
   completed items in `todos/day-NN.md` and `PROGRESS.md`.

## Conventions (free stack — do not introduce paid services by default)
- **Python 3.13.** The venv must be created with `py -3.13 -m venv .venv`. Never use bare `python` (resolves to 3.9 on this machine).
- **ALWAYS use the venv.** Before running or installing anything, ensure `.venv` is active (Windows: `.venv\Scripts\activate`). If you're unsure whether it's active, activate it first. Any run/install command you give me should assume — or explicitly include — venv activation. Never install into system Python.
- **Chat models:** free hosted API tiers (Gemini, Groq, Cerebras) — no install, no credit card, no local Ollama. Never assume a paid API key.
- **Embeddings + reranker:** `sentence-transformers` (CPU pip package, free). This is NOT Ollama and needs no model server.
- **Vector store:** Chroma by default; Supabase free pgvector or Qdrant via Docker are fine free options.
- **Framework:** LangChain + LangGraph (from Week 3 only).
- **Guardrails:** Guardrails AI / NeMo Guardrails (+ optional Llama Guard hosted on Groq's free tier).
- **Observability/eval:** Langfuse (self-hosted via Docker or free cloud) + Ragas.
- **UI:** Streamlit.
- Secrets live in `.env` (gitignored). **Never** write API keys or PII into code, commits, or files.
- Each `src/projectN_*/` folder has its own short README stating that project's goal + definition of done.
- Ship something runnable every day; commit daily.

## Important sequencing rules
- Project 1 (Days 2–5) is intentionally **framework-free** — build retrieval by hand. Don't pull in
  LangChain before Day 13 except as a plain text-splitter utility.
- Project 4 (Days 20–26) teaches Bedrock's *concepts* on a free, self-hostable stack — a model
  gateway, managed-style RAG, guardrails, observability, cost-awareness, reliability. Do NOT spin up
  paid cloud services (especially Bedrock Knowledge Bases on OpenSearch Serverless, which bills
  ~$350/month even idle). If I ever ask to port to real AWS later, remind me to set a budget alert
  and use S3 Vectors instead of OpenSearch Serverless.
