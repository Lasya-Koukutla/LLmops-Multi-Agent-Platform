def validate_prompt(prompt):
    if prompt is None:
        return False, "Prompt is empty."

    prompt = prompt.strip()

    if len(prompt) == 0:
        return False, "Prompt is empty."

    if len(prompt) < 5:
        return False, "Prompt is too short. Please enter at least 5 characters."

    return True, "Valid prompt."

