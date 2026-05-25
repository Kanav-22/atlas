from fastapi import APIRouter
from pydantic import BaseModel
from core.agent import chat

router = APIRouter()

class ChatRequest(BaseModel):
    message: str
    history: list = []

@router.post("/chat")
def chat_endpoint(request: ChatRequest):
    response = chat(request.message, request.history)
    return {"response": response}