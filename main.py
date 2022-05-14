from fastapi import FastAPI
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
import secret
import os
import openai

openai.api_key = secret.api_key

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/")
def home():
    return (
    openai.Completion.create(
    engine="text-davinci-002",
    prompt="Say this is a test",
    max_tokens=5))

