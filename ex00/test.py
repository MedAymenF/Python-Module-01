#!/usr/bin/env python3

from book import Book
from recipe import Recipe

om = Recipe('Omelette', 1, 5, ['Eggs', 'Cooking oil'], 'La ghla 3la mskin',
            'starter')
dinner = Recipe('Chicken', 4, 60, ['Chicken breast', 'Vegetables'],
                'sdar >> fkhad', 'lunch')
recipe_book = Book('Paleo')
print(recipe_book.creation_date)
print(recipe_book.last_update)
print('-' * 25)
print(recipe_book.get_recipes_by_types('starter'))
print('-' * 25)
recipe_book.get_recipe_by_name('Omelette')
print('-' * 25)
recipe_book.add_recipe(dinner)
recipe_book.add_recipe(om)
print(recipe_book.last_update)
print('-' * 25)
recipe_book.get_recipe_by_name('Chicken')
print('-' * 25)
print(recipe_book.get_recipes_by_types('starter')[0])
