"""Day 02 — embed the corpus in batch and persist to index.pkl; reload and verify."""
import pickle
from pathlib import Path

import numpy as np
from sentence_transformers import SentenceTransformer

from corpus import SNIPPETS

INDEX_PATH = Path(__file__).parent / "index.pkl"
MODEL_NAME = "all-MiniLM-L6-v2"


def build_and_save() -> None:
    print(f"Embedding {len(SNIPPETS)} snippets with {MODEL_NAME} ...")
    model = SentenceTransformer(MODEL_NAME)
    vectors = model.encode(SNIPPETS, batch_size=32, show_progress_bar=True)

    index = [{"text": text, "vector": vec} for text, vec in zip(SNIPPETS, vectors)]

    with open(INDEX_PATH, "wb") as f:
        pickle.dump(index, f)
    print(f"Saved {len(index)} entries to {INDEX_PATH}")


def load_and_verify() -> None:
    with open(INDEX_PATH, "rb") as f:
        index = pickle.load(f)

    count = len(index)
    dim = len(index[0]["vector"])
    print(f"\nReloaded index: {count} entries, vector dimension = {dim}")
    assert count == len(SNIPPETS), f"Expected {len(SNIPPETS)} entries, got {count}"
    assert isinstance(index[0]["vector"], np.ndarray), "Vectors should be numpy arrays"
    print("PASS: index round-trips correctly.")


if __name__ == "__main__":
    build_and_save()
    load_and_verify()
