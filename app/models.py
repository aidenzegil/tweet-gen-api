from pydantic import BaseModel, Field


class AdditionArgs(BaseModel):
    num_1: int = Field(
        default=None, title="The first number to add"
    )
    num_2: int = Field(
        default=None, title="The second number to add"
    )