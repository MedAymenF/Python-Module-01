class Recipe:
    def __init__(self, name: str, cooking_lvl: int, cooking_time: int,
                 ingredients: list, description: str, recipe_type: str):
        try:
            assert type(name) == str, 'Name should be a string'
            assert name, "name can't be empty"
        except Exception as e:
            print(e)
            exit(1)
        else:
            self.name = name

        try:
            assert type(cooking_lvl) == int, 'cooking_lvl should be an integer'
            assert 1 <= cooking_lvl <= 5,\
                'cooking_lvl should be between 1 and 5'
        except Exception as e:
            print(e)
            exit(1)
        else:
            self.cooking_lvl = cooking_lvl

        try:
            assert type(cooking_time) == int,\
                'cooking_time should be an integer'
            assert cooking_time >= 0, "cooking_time can't be negative"
        except Exception as e:
            print(e)
            exit(1)
        else:
            self.cooking_time = cooking_time

        try:
            assert type(ingredients) == list, 'ingredients should be a list'
            assert ingredients, "ingredients can't be empty"
            assert not list(filter(lambda x: type(x)
                            is not str, ingredients)),\
                'Elements of ingredients should be strings'
        except Exception as e:
            print(e)
            exit(1)
        else:
            self.ingredients = ingredients

        try:
            assert type(description) == str, 'description should be a string'
        except Exception as e:
            print(e)
            exit(1)
        else:
            self.description = description

        try:
            assert type(recipe_type) == str, 'recipe_type should be a string'
            assert recipe_type, "recipe_type can't be empty"
            assert recipe_type in ['starter', 'lunch', 'dessert'],\
                "recipe_type can only be 'starter', 'lunch', or 'dessert'"
        except Exception as e:
            print(e)
            exit(1)
        else:
            self.recipe_type = recipe_type

    def __str__(self):
        """Return the string to print with the recipe info"""
        txt = "\n".join(['Recipe for {}:'.format(self.name),
                         'Ingredients list: {}'.format(self.ingredients),
                         'To be eaten for {}.'.format(self.recipe_type),
                         'Takes {} minutes of cooking.'.format(
                            self.cooking_time),
                        '{}'.format(self.description)])
        return txt
