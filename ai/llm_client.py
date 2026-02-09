import os
from groq import Groq
from dotenv import load_dotenv

load_dotenv()  # OK for local dev

def ask_llm(prompt: str) -> str:
    api_key = os.getenv("GROQ_API_KEY")

    # If key is missing, fail gracefully
    if not api_key:
        return "⚠️ AI service is temporarily unavailable. Please try again later."

    try:
        client = Groq(api_key=api_key)

        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[{"role": "user", "content": prompt}]
        )

        return response.choices[0].message.content

    except Exception:
        return "We couldn’t generate insights right now. Please try again in a moment 💜"
