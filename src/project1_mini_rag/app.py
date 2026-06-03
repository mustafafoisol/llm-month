"""Day 05 — Streamlit UI for the mini-RAG pipeline."""
import sys
from pathlib import Path

import streamlit as st

# Ensure imports resolve when running from any working directory
sys.path.insert(0, str(Path(__file__).parent))

from retrieve import _load  # triggers model/index warm-up
from rag import answer


@st.cache_resource(show_spinner="Loading embedding model...")
def _warm_up():
    """Load the sentence-transformer model and index once per session."""
    return _load()


def main():
    st.set_page_config(page_title="Mini-RAG", layout="centered")
    st.title("Mini-RAG — LLM Engineering Q&A")
    st.caption("Answers grounded in 30 LLM engineering snippets. No LangChain — built from scratch.")

    with st.sidebar:
        st.header("Settings")
        k = st.slider("Sources to retrieve (k)", min_value=1, max_value=5, value=3)
        st.markdown("---")
        st.markdown(
            "**How it works**\n\n"
            "1. Your question is embedded with `all-MiniLM-L6-v2`\n"
            "2. Cosine similarity ranks all 30 corpus snippets\n"
            "3. Top-k snippets become the LLM context\n"
            "4. Gemini (or Groq fallback) generates a grounded answer"
        )

    _warm_up()

    question = st.text_input(
        "Ask a question about LLM engineering:",
        placeholder="e.g. What is RAG?",
    )
    ask = st.button("Ask", type="primary", disabled=not question.strip())

    if ask and question.strip():
        with st.spinner("Retrieving and generating..."):
            try:
                result = answer(question.strip(), k=k)
            except Exception as exc:
                st.error(f"Error: {exc}")
                return

        st.subheader("Answer")
        st.info(result["answer"])

        with st.expander(f"Retrieved sources (top {k})"):
            for i, src in enumerate(result["sources"], 1):
                st.markdown(f"**[{i}]** Score: `{src['score']:.2f}`")
                st.write(src["text"])
                if i < len(result["sources"]):
                    st.divider()


if __name__ == "__main__":
    main()
