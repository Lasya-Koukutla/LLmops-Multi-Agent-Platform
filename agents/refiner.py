from google import genai
from dotenv import load_dotenv
import os

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)

def refine_prompt(prompt):
    """
    Refine the user's prompt using Gemini.
    """

    response = client.models.generate_content(
        model="gemini-3.6-flash",
        contents=f"""
You are an expert Prompt Engineer.

Your job is to rewrite the user's prompt to make it clearer,
more detailed, and more effective for an AI model.

Rules:
- Keep the original meaning.
- Improve clarity.
- Add missing context if appropriate.
- Do not answer the prompt.
- Only return the improved prompt.

User Prompt:
{prompt}
"""
    )

    return response.text