from fastapi import FastAPI
from pydantic import BaseModel
from .chat import chat

app = FastAPI()

class Query(BaseModel):
    text: str

@app.post("/ask")
def ask(query: Query):
    response = chat(query.text)
    return {"response": response}
