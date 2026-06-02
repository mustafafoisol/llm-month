"""Day 04 — grounded answer generation: retrieve context, prompt the LLM, return answer + sources."""
import os
from dotenv import load_dotenv

from retrieve import retrieve

load_dotenv()

SYSTEM_PROMPT = (
    "You are a precise assistant. "
    "Answer the user's question using ONLY the context snippets provided below. "
    "If the answer cannot be found in the context, reply with exactly: I don't know. "
    "Do not add information from outside the context."
)


def _build_prompt(question: str, snippets: list[dict]) -> str:
    context = "\n\n".join(
        f"[{i+1}] {s['text']}" for i, s in enumerate(snippets)
    )
    return f"Context:\n{context}\n\nQuestion: {question}"


def _call_gemini(system: str, user: str) -> str:
    from google import genai
    client = genai.Client(api_key=os.environ["GEMINI_API_KEY"])
    response = client.models.generate_content(
        model="gemini-2.0-flash",
        contents=f"{system}\n\n{user}",
    )
    return response.text.strip()


def _call_groq(system: str, user: str) -> str:
    from groq import Groq
    client = Groq(api_key=os.environ["GROQ_API_KEY"])
    resp = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {"role": "system", "content": system},
            {"role": "user", "content": user},
        ],
        temperature=0.0,
    )
    return resp.choices[0].message.content.strip()


def _generate(system: str, user: str) -> str:
    gemini_key = os.environ.get("GEMINI_API_KEY", "")
    groq_key = os.environ.get("GROQ_API_KEY", "")

    if not gemini_key and not groq_key:
        raise EnvironmentError("Set GEMINI_API_KEY or GROQ_API_KEY in .env")

    if gemini_key:
        try:
            return _call_gemini(system, user)
        except Exception as e:
            if groq_key and ("quota" in str(e).lower() or "429" in str(e)):
                print(f"[Gemini unavailable: {type(e).__name__}] Falling back to Groq...\n")
                return _call_groq(system, user)
            raise
    return _call_groq(system, user)


def answer(question: str, k: int = 3) -> dict:
    """Return {'answer': str, 'sources': list[dict]} grounded in the top-k retrieved snippets."""
    sources = retrieve(question, k=k)
    user_prompt = _build_prompt(question, sources)
    reply = _generate(SYSTEM_PROMPT, user_prompt)
    return {"answer": reply, "sources": sources}


if __name__ == "__main__":
    questions = [
        # In-corpus questions
        "What is a token in an LLM?",
        "How does cosine similarity work?",
        "What is RAG and why does it reduce hallucinations?",
        "Which vector databases are popular?",
        "How does Ragas evaluate a RAG pipeline?",
        # Out-of-corpus questions — should get 'I don't know'
        "What is the capital of France?",
        "Who won the 2022 FIFA World Cup?",
    ]

    for q in questions:
        result = answer(q)
        print(f"\nQ: {q}")
        print(f"A: {result['answer']}")
        print("Sources:")
        for s in result["sources"]:
            print(f"  [{s['score']:.4f}] {s['text'][:80]}...")
        print("-" * 60)
