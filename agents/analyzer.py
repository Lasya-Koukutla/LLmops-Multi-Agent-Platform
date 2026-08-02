def analyze_prompt(prompt):
    """
    Analyze the user's prompt and identify its category.
    """

    prompt_lower = prompt.lower()

    if any(word in prompt_lower for word in ["python", "java", "c++", "code", "program"]):
        return "Programming"

    elif any(word in prompt_lower for word in ["summarize", "summary"]):
        return "Summarization"

    elif any(word in prompt_lower for word in ["translate", "translation"]):
        return "Translation"

    elif any(word in prompt_lower for word in ["calculate", "solve", "equation", "math"]):
        return "Mathematics"

    elif any(word in prompt_lower for word in ["essay", "story", "poem"]):
        return "Creative Writing"

    else:
        return "General Knowledge"