import os
from dotenv import load_dotenv
from fastapi import Depends, FastAPI
from pydantic import BaseModel
from .ai.gemini import Gemini
from .auth.throttling import apply_rate_limit
from .auth.dependencies import get_user_identifier

app = FastAPI()

load_dotenv()

def load_system_prompt():
    with open("src/prompts/system_prompt.md", "r") as f:
        return f.read()

system_prompt = load_system_prompt()
gemini_api_key = os.getenv("GEMINI_API_KEY")

if not gemini_api_key:
    raise ValueError("GEMINI_API_KEY environment variable not set.")

ai_platform = Gemini(api_key=gemini_api_key, system_prompt=system_prompt)


# Pydantic Models
class ChatRequest(BaseModel):
    prompt: str # JSON

class ChatResponse(BaseModel):
    response: str

# Endpoints
@app.get("/")
async def root():
    return {"message": "API is running"}

@app.post("/chat", response_model=ChatResponse)
async def chat(request: ChatRequest, user_id: str =
               Depends(get_user_identifier)):
    apply_rate_limit(user_id)
    response_text = ai_platform.chat(request.prompt)
    return ChatResponse(response=response_text)

