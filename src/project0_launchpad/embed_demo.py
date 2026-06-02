"""Day 01 — embed 3 sentences with sentence-transformers and show cosine similarities."""
import numpy as np
from sentence_transformers import SentenceTransformer


def cosine_similarity(a: np.ndarray, b: np.ndarray) -> float:
    return float(np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b)))


if __name__ == "__main__":
    sentences = [
        "Large language models are trained on massive text corpora.",   # related to #2
        "GPT and Gemini are examples of modern language models.",       # related to #1
        "The Eiffel Tower is located in Paris, France.",                # unrelated
    ]

    model = SentenceTransformer("all-MiniLM-L6-v2")
    embeddings = model.encode(sentences, normalize_embeddings=False)

    print(f"Model: all-MiniLM-L6-v2 | Vector dimension: {embeddings.shape[1]}\n")

    pairs = [
        (0, 1, "related  "),
        (0, 2, "unrelated"),
        (1, 2, "unrelated"),
    ]

    for i, j, label in pairs:
        sim = cosine_similarity(embeddings[i], embeddings[j])
        print(f"[{label}]  S{i+1} <-> S{j+1}  similarity = {sim:.4f}")
        print(f"          '{sentences[i][:60]}'")
        print(f"          '{sentences[j][:60]}'")
        print()

    sim_related = cosine_similarity(embeddings[0], embeddings[1])
    sim_unrelated_01 = cosine_similarity(embeddings[0], embeddings[2])
    sim_unrelated_12 = cosine_similarity(embeddings[1], embeddings[2])

    assert sim_related > sim_unrelated_01, "Expected related pair to score higher than unrelated"
    assert sim_related > sim_unrelated_12, "Expected related pair to score higher than unrelated"
    print("PASS: related sentences scored higher than unrelated ones.")
