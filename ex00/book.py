from datetime import datetime
from recipe import Recipe


class Book:
    def __init__(self, name: str):
        try:
            assert type(name) is str, 'name has to be a string'
        except Exception as e:
            print(e)
        else:
            self.name = name
            self.creation_date = self.last_update = datetime.now()
            self.recipes_list = {"starter": [], "lunch": [], "dessert": []}

    def get_recipe_by_name(self, name):
        """Prints a recipe with the name `name` and returns the instance"""
        try:
            assert type(name) is str, 'name has to be a string'
        except Exception as e:
            print(e)
        else:
            for rtype, lst in self.recipes_list.items():
                for recipe in lst:
                    if recipe.name == name:
                        result = recipe
                        print(result)
                        return result
            return None

    def get_recipes_by_types(self, recipe_type):
        """Get all recipe names for a given recipe_type"""
        try:
            assert type(recipe_type) is str, 'recipe_type has to be a string'
            assert recipe_type in self.recipes_list,\
                "recipe_type can only be 'starter', 'lunch', or 'dessert'"
        except Exception as e:
            print(e)
            return []
        else:
            return self.recipes_list[recipe_type]

    def add_recipe(self, recipe):
        """Add a recipe to the book and update last_update"""
        try:
            assert type(recipe) is Recipe,\
                'recipe has to be an instance of the Recipe class'
        except Exception as e:
            print(e)
        else:
            rtype = recipe.recipe_type
            self.recipes_list[rtype].append(recipe)
            self.last_update = datetime.now()
