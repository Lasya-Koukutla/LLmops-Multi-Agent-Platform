from dotenv import load_dotenv
from google import genai
import os

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)

print("Models supporting generateContent:")
print("----------------------------------")

found = False

for model in client.models.list():
    if "generateContent" in model.supported_actions:
        print(model.name)
        found = True

if not found:
    print("No generateContent model is available.")