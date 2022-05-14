

from fastapi import APIRouter
import openai

router = APIRouter(
    prefix="/tweet",
    responses={404: {"description": "Not found"}},
)

@router.post("/")
def home():
    return (
    openai.Completion.create(
    engine="text-davinci-002",
    prompt="Say this is a test",
    max_tokens=5))

