import sys
from load_docs import load_all

_SEPS = ["\n\n", "\n", " ", ""]


def _split(text: str, size: int, overlap: int, seps: list[str]) -> list[str]:
    sep, *rest = seps

    if sep == "":
        step = max(1, size - overlap)
        return [text[i : i + size] for i in range(0, len(text), step)]

    raw = [s for s in text.split(sep) if s.strip()]

    pieces: list[str] = []
    for part in raw:
        if len(part) > size and rest:
            pieces.extend(_split(part, size, overlap, rest))
        else:
            pieces.append(part)

    chunks: list[str] = []
    buf = ""
    for piece in pieces:
        candidate = (buf + sep + piece).strip() if buf else piece
        if len(candidate) <= size:
            buf = candidate
        else:
            if buf:
                chunks.append(buf)
                tail = buf[-overlap:] if overlap else ""
                buf = (tail + sep + piece).strip() if tail else piece
            else:
                chunks.append(piece)
                buf = ""
    if buf:
        chunks.append(buf)
    return chunks


def chunk_text(text: str, size: int, overlap: int) -> list[str]:
    return _split(text, size, overlap, _SEPS)


def chunk_docs(pages: list[dict], size: int, overlap: int) -> list[dict]:
    chunks = []
    for page in pages:
        for text in chunk_text(page["text"], size, overlap):
            chunks.append({"source": page["source"], "page": page["page"], "text": text})
    return chunks


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    pages = load_all()
    print(f"Loaded {len(pages)} pages from {len({p['source'] for p in pages})} PDFs\n")

    for size, overlap in [(300, 50), (600, 100), (1000, 200)]:
        chunks = chunk_docs(pages, size=size, overlap=overlap)
        avg = sum(len(c["text"]) for c in chunks) / len(chunks)
        print(f"\n{'='*60}")
        print(f"size={size}, overlap={overlap}  →  {len(chunks)} chunks, avg {avg:.0f} chars")
        print(f"{'='*60}")
        for c in chunks[:2]:
            preview = c["text"][:180].replace("\n", " ")
            print(f"  [{c['source']} p.{c['page']}] {preview}")

    chosen = chunk_docs(pages, size=600, overlap=100)
    print(f"\n>>> Chosen: size=600, overlap=100  →  {len(chosen)} chunks ready for Day 8")
