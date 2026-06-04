import sys
from pathlib import Path

import chromadb
from sentence_transformers import SentenceTransformer

from chunk import chunk_docs
from load_docs import load_all

CHROMA_DIR = Path(__file__).parent / "chroma_db"
COLLECTION = "docchat"
EMBED_MODEL = "all-MiniLM-L6-v2"
CHUNK_SIZE = 600
CHUNK_OVERLAP = 100


def get_collection(force: bool = False) -> chromadb.Collection:
    client = chromadb.PersistentClient(path=str(CHROMA_DIR))

    if force:
        try:
            client.delete_collection(COLLECTION)
        except Exception:
            pass

    collection = client.get_or_create_collection(COLLECTION)

    if collection.count() > 0 and not force:
        print(f"Collection '{COLLECTION}' already has {collection.count()} chunks — skipping ingest.")
        return collection

    print("Loading and chunking pages...")
    pages = load_all()
    chunks = chunk_docs(pages, size=CHUNK_SIZE, overlap=CHUNK_OVERLAP)
    print(f"  {len(pages)} pages → {len(chunks)} chunks. Embedding with {EMBED_MODEL}...")

    model = SentenceTransformer(EMBED_MODEL)
    texts = [c["text"] for c in chunks]
    embeddings = model.encode(texts, batch_size=32, show_progress_bar=True).tolist()

    ids = [f"{c['source']}:p{c['page']}:c{i}" for i, c in enumerate(chunks)]
    metadatas = [{"source": c["source"], "page": c["page"]} for c in chunks]

    collection.add(documents=texts, embeddings=embeddings, metadatas=metadatas, ids=ids)
    print(f"  Ingested {collection.count()} chunks into '{COLLECTION}'.")
    return collection


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")

    print("=== Run 1: ingest ===")
    col = get_collection()
    count = col.count()
    print(f"Collection count: {count}\n")

    print("=== Run 2: persistence check (reopen client) ===")
    client2 = chromadb.PersistentClient(path=str(CHROMA_DIR))
    col2 = client2.get_collection(COLLECTION)
    count2 = col2.count()
    print(f"Reopened collection count: {count2}")
    assert count == count2, "Persistence FAILED"
    print("Persistence check PASSED\n")

    print("=== Sanity query: 'attention mechanism' ===")
    model = SentenceTransformer(EMBED_MODEL)
    q_emb = model.encode(["attention mechanism"]).tolist()
    results = col2.query(query_embeddings=q_emb, n_results=3)
    for i, (doc, meta) in enumerate(zip(results["documents"][0], results["metadatas"][0])):
        print(f"  [{i+1}] {meta['source']} p.{meta['page']}: {doc[:120].replace(chr(10), ' ')}")
