from typing import List
from pydantic import BaseModel


class Ingredients(BaseModel):
    ingredients: List[str]

    def __init__(self, **kwargs):
        kwargs["ingredients"] = [
            ingredient.strip() for ingredient in kwargs["ingredients"].split(",")
        ]
        super().__init__(**kwargs)

    class Config:
        arbitrary_types_allowed = True


class QuantifiedIngredents(BaseModel):
    ingredient: str
    quantity: str

    class Config:
        arbitrary_types_allowed = True
