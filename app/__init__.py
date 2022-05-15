from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import openai

## Secrets
import secret

## Routers
import app.api.tweet_gen_routes as tweet_gen 
import app.api.math_routes as math


openai.api_key = secret.api_key

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(tweet_gen.router)
app.include_router(math.router)