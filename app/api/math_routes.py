from typing import List
from fastapi import APIRouter, Body
from pydantic import BaseModel

from app.models import AdditionArgs

router = APIRouter(
    prefix= "/math",
    responses= {404: {"description": "Not found"}},
)

## FastAPI requires embed=True option to be passed to Body() if 
# - destructuring Body attributes inline AND 
# - no class is unrolled as a prior argument
@router.post("/addition/{num_1}")
async def addition(num_1: int, num_2: int = Body(embed=True)):
    return num_1 + num_2