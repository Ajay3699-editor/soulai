# llmcore.py

import google.generativeai as genai

# Gemini API key
API_KEY = "AIzaSyBrVmvZXwJla5NL2dw8ujo727Ffqpi4KlQ"
genai.configure(api_key=API_KEY)

# Load the Gemini model
model = genai.GenerativeModel("gemini-1.5-flash-latest")

# Function to generate response
def get_response(prompt: str) -> str:
    try:
        response = model.generate_content(prompt)
        return response.text.strip()
    except Exception as e:
        return f"Error: {str(e)}"
