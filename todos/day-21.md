# Day 21 — Serve it for free
Saturday, June 20, 2026 · Project 4 of 5

> **Activate your venv first.** Run `source .venv/bin/activate` (Windows: `.venv\Scripts\activate`) before installing or running anything today — your prompt should show `(.venv)`. Do all work inside the venv.

## Today's goal
Serve your vectors from a managed-style store at $0 — the free replacement for a Bedrock Knowledge Base.

## Learn first (~30 min)
Managed vs self-hosted vector stores; pgvector; clean service APIs.

## Tasks
- [ ] Recommended (zero ops): keep Chroma but add a clean ingest+query service layer so it behaves like a managed KB (collection, upsert, query).
- [ ] Optional cloud feel, still free: spin up Supabase free tier (Postgres + pgvector) OR Qdrant via Docker, and ingest your chunks there.
- [ ] Query it and confirm parity with your Week 2 pipeline (cited chunks come back).

## Files you'll create / touch
- `src/project4_serving/rag_store.py`

## Definition of done
Your documents are served from a store with a clean managed-style API and queries return cited chunks.

## If you get stuck (the 30-minute rule)
Stick with Chroma + a thin service wrapper — that is a perfectly legitimate, fully free 'knowledge base'.

## Notes / scratchpad
_Fill this in as you work: decisions made, blockers hit, useful links._



## End of day
- [ ] Ran inside the **activated venv** (`(.venv)` visible) and `python ...` works
- [ ] Committed to git with a real message
- [ ] Checked off today's tasks above and updated PROGRESS.md
