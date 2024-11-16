import re
from app.schemas.Ingredients import Ingredients
from app.schemas.Recipe import Recipe
from app.utils.genai_config import model


class RecipeGenerator:

    def get_recipe(ingredient_list: Ingredients):
        raw_response = model.generate_content(", ".join(ingredient_list.ingredients))
        return RecipeGenerator.post_process(raw_response)

    def post_process(raw_response: str):
        text = raw_response.text
        return Recipe(recipe=text)