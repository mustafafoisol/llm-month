from pypdf import PdfReader
from pathlib import Path

DATA_DIR = Path(__file__).parent / "data"


def load_pdf(path: Path) -> list[dict]:
    reader = PdfReader(path)
    pages = []
    for i, page in enumerate(reader.pages, start=1):
        text = page.extract_text() or ""
        pages.append({"source": path.name, "page": i, "text": text})
    return pages


def load_all(data_dir: Path = DATA_DIR) -> list[dict]:
    docs = []
    for pdf in sorted(data_dir.glob("*.pdf")):
        docs.extend(load_pdf(pdf))
    return docs


if __name__ == "__main__":
    import sys
    sys.stdout.reconfigure(encoding="utf-8")
    docs = load_all()
    sources = {d["source"] for d in docs}
    print(f"Loaded {len(docs)} pages from {len(sources)} PDFs\n")
    for doc in docs:
        snippet = doc["text"][:150].replace("\n", " ")
        flag = " *** EMPTY ***" if not doc["text"].strip() else ""
        print(f"[{doc['source']} p.{doc['page']}] {len(doc['text'])} chars{flag}")
        print(f"  {snippet}")
