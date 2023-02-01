from email.policy import default
import json
from typing import Union
from fastapi import APIRouter, Body, requests
import openai

router = APIRouter(
    prefix="/tweet",
    responses={404: {"description": "Not found"}},
)


@router.post("/")
async def generate(sentPrompt: str = Body(embed=True)):
    response = openai.Completion.create(
    engine="text-davinci-002",
    prompt=sentPrompt,
    temperature=1,
    max_tokens=2000,
    top_p=1,
    frequency_penalty=2,
    presence_penalty=2
)
    return response
