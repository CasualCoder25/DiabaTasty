from typing import List
from pydantic import BaseModel
from app.schemas.Ingredients import QuantifiedIngredents


class Recipe(BaseModel):
    recipe: str

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    class Config:
        arbitrary_types_allowed = True

    