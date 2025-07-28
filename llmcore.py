# llmcore.py
import google.generativeai as genai
import os

# ✅ Read API key from environment variable
API_KEY = os.getenv("GEMINI_API_KEY")

# Configure Gemini
genai.configure(api_key=API_KEY)

# Load the model
model = genai.GenerativeModel("gemini-1.5-flash-latest")

# Generate response
def get_response(prompt: str) -> str:
    try:
        response = model.generate_content(prompt)
        return response.text.strip()
    except Exception as e:
        return f"Error: {str(e)}"
