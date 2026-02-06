import os
from groq import Groq
from dotenv import load_dotenv

load_dotenv()  # 👈 VERY IMPORTANT

def ask_llm(prompt: str):
    api_key = os.getenv("GROQ_API_KEY")

    if not api_key:
        return "⚠️ AI service is temporarily unavailable. Please try again later."

    client = Groq(api_key=api_key)

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role": "user", "content": prompt}]
    )

    return response.choices[0].message.content