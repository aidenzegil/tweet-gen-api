from email.policy import default
import json
from typing import Union
from fastapi import APIRouter, Body, requests
import openai

router = APIRouter(
    prefix="/tweet",
    responses={404: {"description": "Not found"}},
)

# @router.post("/")
# def generate():
#     return (
#     openai.Completion.create(
#     engine="text-davinci-002",
#     prompt="Say this is a test",
#     max_tokens=5))


@router.post("/")
async def generate(sentPrompt: str = Body(embed=True)):
    response = openai.Completion.create(
    engine="text-davinci-002",
    prompt=sentPrompt,
    temperature=1,
    max_tokens=70,
    top_p=1,
    frequency_penalty=2,
    presence_penalty=2
)
    return response

# async def generate():
#     return ("-Did you know that the globe is divided into 24 time zones? \n-Or that there are 196 countries in the world? \n-How about that Antarctica is almost twice the size of Australia?")
