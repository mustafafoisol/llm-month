"""Day 03 — top-k semantic retrieval over the persisted snippet index."""
import pickle
from pathlib import Path

import numpy as np
from sentence_transformers import SentenceTransformer

INDEX_PATH = Path(__file__).parent / "index.pkl"
MODEL_NAME = "all-MiniLM-L6-v2"

_model: SentenceTransformer | None = None
_index: list[dict] | None = None


def _load() -> tuple[SentenceTransformer, list[dict]]:
    global _model, _index
    if _model is None:
        _model = SentenceTransformer(MODEL_NAME)
    if _index is None:
        with open(INDEX_PATH, "rb") as f:
            _index = pickle.load(f)
    return _model, _index


def retrieve(question: str, k: int = 3) -> list[dict]:
    """Return the top-k snippets most similar to *question*, with scores."""
    model, index = _load()

    query_vec = model.encode(question)
    query_norm = query_vec / (np.linalg.norm(query_vec) + 1e-10)

    scores = []
    for entry in index:
        vec = entry["vector"]
        norm = vec / (np.linalg.norm(vec) + 1e-10)
        scores.append(float(np.dot(query_norm, norm)))

    ranked = sorted(
        ({"text": index[i]["text"], "score": scores[i]} for i in range(len(scores))),
        key=lambda x: x["score"],
        reverse=True,
    )
    return ranked[:k]


if __name__ == "__main__":
    questions = [
        "What is a token in an LLM?",
        "How does cosine similarity work?",
        "What is RAG and why does it reduce hallucinations?",
        "Which vector databases are popular?",
        "How does Ragas evaluate a RAG pipeline?",
    ]

    for q in questions:
        print(f"\nQ: {q}")
        for rank, hit in enumerate(retrieve(q, k=3), 1):
            print(f"  {rank}. [{hit['score']:.4f}] {hit['text']}")
