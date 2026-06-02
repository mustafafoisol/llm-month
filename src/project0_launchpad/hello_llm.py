"""Day 01 — call a free hosted LLM (Gemini primary, Groq fallback) and stream the response."""
import os
from dotenv import load_dotenv

load_dotenv()


def call_gemini(prompt: str) -> None:
    from google import genai
    client = genai.Client(api_key=os.environ["GEMINI_API_KEY"])
    print("=== Gemini 2.0 Flash (streaming) ===")
    for chunk in client.models.generate_content_stream(
        model="gemini-2.0-flash", contents=prompt
    ):
        print(chunk.text, end="", flush=True)
    print()


def call_groq(prompt: str) -> None:
    from groq import Groq
    client = Groq(api_key=os.environ["GROQ_API_KEY"])
    print("=== Groq / llama-3.1-8b-instant (streaming) ===")
    stream = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[{"role": "user", "content": prompt}],
        stream=True,
    )
    for chunk in stream:
        delta = chunk.choices[0].delta.content or ""
        print(delta, end="", flush=True)
    print()


if __name__ == "__main__":
    prompt = "In 3 sentences, explain what a large language model is and why it matters."

    gemini_key = os.environ.get("GEMINI_API_KEY", "")
    groq_key = os.environ.get("GROQ_API_KEY", "")

    if not gemini_key and not groq_key:
        raise EnvironmentError(
            "Set GEMINI_API_KEY or GROQ_API_KEY in your .env file.\n"
            "Get them free (no card) at:\n"
            "  Gemini: https://aistudio.google.com/apikey\n"
            "  Groq:   https://console.groq.com/keys"
        )

    if gemini_key:
        try:
            call_gemini(prompt)
        except Exception as e:
            if groq_key and ("quota" in str(e).lower() or "429" in str(e)):
                print(f"[Gemini unavailable: {type(e).__name__}] Falling back to Groq...\n")
                call_groq(prompt)
            else:
                raise
    else:
        call_groq(prompt)
