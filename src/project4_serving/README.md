# Project 4 — Serve it for free

**Days 20-26.** A completely free, self-hostable serving stack that teaches the same
production concepts as AWS Bedrock (model gateway, managed-style RAG, guardrails,
observability, cost-awareness, reliability) at $0 — no credit card, no surprise bills.

## Goal
Run the app on a free stack (free hosted API tiers + Chroma/pgvector + Guardrails AI + Langfuse)
and add the production concerns employers test for.

## Definition of done
Answers served through a swappable model gateway, guardrails that demonstrably fire, traces in
Langfuse, a tokens/latency/cost report, and provider fallback on failure.

## Free stack used here
- **Chat models:** free hosted API tiers (Gemini, Groq, Cerebras) — no install, no card
- **Vector store:** Chroma (or Supabase free pgvector / Qdrant via Docker)
- **Guardrails:** Guardrails AI / NeMo Guardrails (+ optional Llama Guard on Groq's free tier)
- **Observability:** Langfuse (self-hosted via Docker, or free cloud tier)

See the matching `todos/day-20.md` ... `day-26.md` for the daily breakdown.
