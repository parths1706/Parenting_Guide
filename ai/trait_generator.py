from ai.llm_client import ask_llm

def generate_traits(data):
    age = data.get("age", 0)
    country = data.get("country")
    gender = data.get("gender")
    india_info = data.get("india_info", {})

    # Decide description mode
    if age < 3:
        if country == "India":
            trait_type = "future personality tendencies (based on birth chart)"
        else:
            trait_type = "early temperament and natural responses"
    else:
        trait_type = "personality traits"

    prompt = f"""
You are a **child psychology expert** with cultural awareness.

Your task:
Generate **8–12 short bullet points** describing a child’s {trait_type}.

STRICT RULES:
- Age < 3 → DO NOT claim fixed personality
- India + Age < 3 → Describe FUTURE tendencies only
- Astrology is GUIDANCE, not fate
- Use gentle, positive, parent-friendly language
- Avoid words like “will definitely”, “guaranteed”, “fixed”
- NO explanations, NO headings
- Output ONLY a bullet list

Child Context:
- Country: {country}
- Age: {age}
- Gender: {gender}
"""

    # India-specific astrology logic
    if country == "India":
        prompt += f"""
Birth Details (for astrological guidance only):
- Date of Birth: {india_info.get("birth_date")}
- Time of Birth: {india_info.get("birth_time")}
- Zodiac Sign (if known): {india_info.get("horoscope", "Not provided")}

Astrology Instructions:
- Use traditional Indian astrological interpretation lightly
- Focus on emotional nature, learning inclination, social energy, discipline tendency
- Frame everything as *potential that may develop with nurturing*
"""

    response = ask_llm(prompt)

    # Clean bullets safely
    traits = [
        line.strip().lstrip("•-").strip()
        for line in response.split("\n")
        if line.strip()
    ]

    return traits
