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
        You are generating **short trait labels** for a child profile.

        Your task:
        Return **8–12 VERY SHORT trait words or phrases**
        (1–3 words max each) that can be used as **editable chips/tokens** in a UI.

        STRICT FORMAT RULES:
        - EACH line must be a single trait label
        - NO sentences
        - NO explanations
        - NO punctuation at the end
        - NO emojis
        - Think like tags, not text

        CONTENT RULES:
        - Age < 3 → traits must be temperament or early tendencies
        - Do NOT state fixed personality for Age < 3
        - India + Age < 3 → include gentle astrology-influenced future tendencies
        - Astrology is guidance, NOT fate
        - Use positive, parent-friendly language
        - Avoid absolute words (never, always, guaranteed)

        Child Context:
        - Country: {country}
        - Age: {age}
        - Gender: {gender}
        """

    # India-specific astrology logic
    if country == "India":
         prompt += f"""
Birth Context (for guidance only):
- Birth Date: {india_info.get("birth_date")}
- Birth Time: {india_info.get("birth_time")}
- Zodiac Sign: {india_info.get("horoscope", "Unknown")}

Astrology Guidance:
- Influence emotional nature, learning style, social energy
- Frame traits as tendencies that may develop with nurturing
"""

    response = ask_llm(prompt)

    # Clean bullets safely
    traits = [
        line.strip().lstrip("•-").strip()
        for line in response.split("\n")
        if line.strip()
    ]

    return traits
