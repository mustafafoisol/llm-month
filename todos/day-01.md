# Day 01 — Launchpad
Sunday, May 31, 2026 · Project 0 of 5

> **Activate your venv first.** Run `source .venv/bin/activate` (Windows: `.venv\Scripts\activate`) before installing or running anything today — your prompt should show `(.venv)`. Do all work inside the venv.

## Today's goal
Set up an isolated virtual environment and get it calling an LLM and computing embeddings.

## Learn first (~30 min)
Why virtual environments isolate dependencies; tokens & context window; embeddings & cosine similarity.

## Tasks
- [x] Create the repo `llm-month/` and a `.env` file for keys (gitignored, never committed).
- [x] Create the virtual environment: `py -3.13 -m venv .venv`.
- [x] ACTIVATE it: `.venv\Scripts\activate`. Your prompt should now show `(.venv)`. From here on, never install or run anything unless the venv is active.
- [x] With the venv active, install deps: `google-genai`, `groq`, `sentence-transformers`, `numpy`, `python-dotenv`, `scikit-learn`. Then `pip freeze > requirements.txt`.
- [x] Get FREE, no-credit-card API keys: Google AI Studio (Gemini) AND Groq. No install, no card. (Embeddings run via the `sentence-transformers` pip package — a CPU library, NOT a model server like Ollama.)
- [x] Write `hello_llm.py`: call a free hosted model (Gemini or Groq), stream the response, print it.
- [x] Write `embed_demo.py`: with `sentence-transformers`, embed 3 sentences (two related, one unrelated), print vector dimension, compute pairwise cosine similarity.
- [x] Confirm related sentences score higher; first git commit.

## Files you'll create / touch
- `src/project0_launchpad/hello_llm.py`
- `src/project0_launchpad/embed_demo.py`
- `.env (gitignored)`
- `requirements.txt`

## Definition of done
Inside the activated venv: `python hello_llm.py` prints an answer from a free hosted model AND `python embed_demo.py` shows related sentences scoring higher than unrelated ones.

## If you get stuck (the 30-minute rule)
Gemini signup slow? Use Groq or Cerebras — all free, no card. Cosine math confusing? Use `sklearn.metrics.pairwise.cosine_similarity`.

## Notes / scratchpad
_Fill this in as you work: decisions made, blockers hit, useful links._



## End of day
- [x] Ran inside the **activated venv** (`(.venv)` visible) and `python ...` works
- [ ] Committed to git with a real message
- [x] Checked off today's tasks above and updated PROGRESS.md
