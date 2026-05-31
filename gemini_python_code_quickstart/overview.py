import os
from pathlib import Path
from dotenv import load_dotenv
from google import genai

# Load environment variables from the .env file in the parent directory
env_path = Path(__file__).resolve().parent.parent / '.env'
load_dotenv(dotenv_path=env_path)

# The google-genai SDK expects GEMINI_API_KEY, but the .env defines GOOGLE_API_KEY.
if "GOOGLE_API_KEY" in os.environ and "GEMINI_API_KEY" not in os.environ:
    os.environ["GEMINI_API_KEY"] = os.environ["GOOGLE_API_KEY"]

client = genai.Client()

response = client.models.generate_content(
    model="gemini-3.5-flash",
    contents="Explain how AI works in a few words",
)

print(response.text)


