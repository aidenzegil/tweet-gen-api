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
# async def generate(thread: str = Body(embed=True), numberOfThreads: int = Body(embed=True)):
#     final_prompt = json.dumps({"Continue " + {thread} + "in " + {str(numberOfThreads)} + "point. The points can be a maximum of 280 characters. Points that approach this maximum are preferred."})
#     response = openai.Completion.create(
#     engine="text-davinci-002",
#     prompt= final_prompt,
#     temperature=1,
#     max_tokens= (numberOfThreads * 70),
#     top_p=1,
#     frequency_penalty=1.5,
#     presence_penalty=1.5
# )
async def generate():
    return ("-Did you know that the globe is divided into 24 time zones? \n-Or that there are 196 countries in the world? \n-How about that Antarctica is almost twice the size of Australia?")
