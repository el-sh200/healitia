from rest_framework import serializers
from .models import Ingredient, Cuisine, Recipe, RecipeItem, InstructionStep


class IngredientSerializer(serializers.ModelSerializer):
    cover_url = serializers.SerializerMethodField()

    class Meta:
        model = Ingredient
        exclude = ('created', 'updated')

    def get_cover_url(self, obj):
        request = self.context.get('request')
        if obj.cover:
            return request.build_absolute_uri(obj.cover.url)
        return None


class CuisineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cuisine
        exclude = ('created', 'updated')


class RecipeItemSerializer(serializers.ModelSerializer):
    ingredient_name = serializers.ReadOnlyField(source='ingredient.name')
    ingredient_image_url = serializers.SerializerMethodField()

    class Meta:
        model = RecipeItem
        exclude = ('created', 'updated', 'recipe', 'ingredient')

    def get_ingredient_image_url(self, obj):
        request = self.context.get('request')
        if obj.ingredient.cover:
            return request.build_absolute_uri(obj.ingredient.cover.url)
        return None


class InstructionStepSerializer(serializers.ModelSerializer):
    class Meta:
        model = InstructionStep
        exclude = ('created', 'updated')


class RecipeSerializer(serializers.ModelSerializer):
    recipeitem_set = RecipeItemSerializer(many=True)
    cuisines = CuisineSerializer(many=True)
    steps = InstructionStepSerializer(many=True)
    cover_url = serializers.SerializerMethodField()

    class Meta:
        model = Recipe
        exclude = ('ingredients',)

    def get_cover_url(self, obj):
        request = self.context.get('request')
        if obj.cover:
            return request.build_absolute_uri(obj.cover.url)
        return None
