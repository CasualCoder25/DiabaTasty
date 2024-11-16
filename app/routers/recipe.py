from fastapi import APIRouter, HTTPException
from app.schemas.Ingredients import Ingredients
from app.schemas.Recipe import Recipe
from app.utils.recipe_generator import RecipeGenerator

router = APIRouter()

@router.post("/get-recipe/", response_model=Recipe)
async def get_items(ingredients: str):
    try:
        ingredient_list = Ingredients(ingredients=ingredients)
        return RecipeGenerator.get_recipe(ingredient_list)
    except Exception as e:
        return HTTPException(status_code=404, detail="Invalid Request")
