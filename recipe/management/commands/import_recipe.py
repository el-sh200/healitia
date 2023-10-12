import json
from recipe.models import Recipe, Ingredient, Cuisine
from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help = 'import recipe'

    def handle(self, *args, **options):

        with open('recipe.json') as file:
            data = json.load(file)

        for recipe_data in data:
            try:
                recipe, created = Recipe.objects.get_or_create(
                    title=recipe_data['title'],
                    description=recipe_data['summary'],
                    ready_time=recipe_data['readyInMinutes'],
                    servings=recipe_data['servings'],
                )
                if created:
                    all_ingredient = recipe_data['extendedIngredients']
                    ingre_list = []
                    for ingre in all_ingredient:
                        ing_instance, created = Ingredient.objects.get_or_create(name=ingre['name'])
                        ingre_list.append(ing_instance)

                    all_cuisine = recipe_data['cuisines']
                    cuisines_list = []
                    for cui in all_cuisine:
                        cui_instance, created = Cuisine.objects.get_or_create(name=cui)
                        all_cuisine.append(cui_instance)

                    recipe.save()

                    for j in cuisines_list:
                        recipe.cuisines.add(j)

                print('added')
            except Exception as e:
                print(e)
