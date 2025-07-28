from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from llmcore import get_response
from sentimentcore import analyze_sentiment

app = FastAPI()

# Allow requests from any origin
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Prompt(BaseModel):
    prompt: str

@app.post("/ask")
def ask_question(payload: Prompt):
    prompt = payload.prompt.strip()

    if not prompt:
        return {"error": "Prompt cannot be empty."}

    try:
        response = get_response(prompt)
        sentiment = analyze_sentiment(response)
        return {"response": response, "sentiment": sentiment}
    except Exception as e:
        return {"error": str(e)}

@app.get("/")
def home():
    return {"message": "Backend is running!"}
