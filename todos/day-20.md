# Day 20 — Serve it for free
Friday, June 19, 2026 · Project 4 of 5

> **Activate your venv first.** Run `source .venv/bin/activate` (Windows: `.venv\Scripts\activate`) before installing or running anything today — your prompt should show `(.venv)`. Do all work inside the venv.

## Today's goal
Put your app behind a model gateway so you can swap LLM providers freely — the core thing Bedrock does, using only free hosted tiers.

## Learn first (~30 min)
Why a gateway/abstraction layer; OpenAI-compatible APIs (Groq works with the openai SDK + a base URL); free-tier rate limits.

## Tasks
- [ ] Confirm free API keys for two providers (e.g. Gemini + Groq; Cerebras optional as a third).
- [ ] Write a single `llm(prompt, backend=...)` function that routes to either provider behind one interface, switchable with one config value.
- [ ] Run your RAG app through the gateway against both providers and note quality, speed, and rate-limit differences.

## Files you'll create / touch
- `src/project4_serving/gateway.py`

## Definition of done
Your app answers via at least two interchangeable FREE hosted backends through one function.

## If you get stuck (the 30-minute rule)
If one provider's signup or limits annoy you, swap in Cerebras or an OpenRouter free model — the gateway makes it a one-line change.

## Notes / scratchpad
_Fill this in as you work: decisions made, blockers hit, useful links._



## End of day
- [ ] Ran inside the **activated venv** (`(.venv)` visible) and `python ...` works
- [ ] Committed to git with a real message
- [ ] Checked off today's tasks above and updated PROGRESS.md
