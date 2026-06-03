# Project 1 — Mini-RAG (from scratch)

**Days 2–5.** Build a retrieval-augmented generation pipeline by hand — no LangChain, no vector DB framework.

## Goal

Ask a question, get an answer grounded in 30 LLM engineering snippets with sources shown; out-of-corpus questions say "I don't know".

## Architecture

```
corpus.py (30 snippets)
    |
    v
build_index.py  -->  index.pkl  (384-dim vectors, pickled)
                          |
                          v
                    retrieve.py  (cosine similarity, top-k)
                          |
                          v
                      rag.py  (prompt builder + LLM call)
                          |
                          v
                      app.py  (Streamlit UI)
```

## How to run

```bash
# Activate venv (Windows)
.venv\Scripts\activate

# One-time: build the index (already done if index.pkl exists)
cd src/project1_mini_rag
py -3.13 build_index.py

# Launch the UI
streamlit run app.py
```

Open the browser tab Streamlit prints. Type a question, hit **Ask**.

## What I learned

- **Embeddings by hand** — `SentenceTransformer.encode()` gives a 384-dim float32 vector per snippet; a plain pickle is enough for 30 entries.
- **Cosine similarity without a library** — L2-normalise both vectors, then `np.dot` gives the cosine score directly.
- **Grounded prompting** — prepending retrieved snippets as numbered context and instructing the LLM to answer *only* from that context reliably produces "I don't know" for out-of-corpus questions.
- **Gemini → Groq fallback** — catching quota/429 errors and retrying on a second free API keeps the pipeline running without any paid tier.
- **Streamlit caching** — `@st.cache_resource` loads the 80 MB embedding model once and reuses it across reruns, keeping the UI snappy after the first query.

## Definition of done

`streamlit run app.py` works end-to-end: in-corpus questions get grounded answers with source scores; out-of-corpus questions return "I don't know".
