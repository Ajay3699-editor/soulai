from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from llmcore import get_response
from sentimentcore import analyze_sentiment  # ✅ import this

app = FastAPI()

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
    prompt = payload.prompt
    response = get_response(prompt)
    sentiment = analyze_sentiment(response)  # ✅ Analyze LLM response sentiment
    return {"response": response, "sentiment": sentiment}

@app.get("/")
def home():
    return {"message": "Backend is running!"}
