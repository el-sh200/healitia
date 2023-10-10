from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Recipe, FavoriteRecipe
from .serializers import RecipeSerializer, FavoriteRecipeSerializer


class RecipeListAPIView(APIView):
    def get(self, request, format=None):
        recipes = Recipe.objects.all()
        serializer = RecipeSerializer(recipes, context={'request': self.request}, many=True)
        return Response(serializer.data)


class RecipeDetailAPIView(APIView):
    def get(self, request, pk, format=None):
        try:
            recipe = Recipe.objects.get(pk=pk)
        except Recipe.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = RecipeSerializer(recipe, context={'request': self.request})
        return Response(serializer.data)


class FavoriteRecipeListAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = self.request.user
        favorite_recipes = FavoriteRecipe.objects.filter(user=user)
        favorite_recipe_ids = favorite_recipes.values_list('recipe_id', flat=True)
        recipes = Recipe.objects.filter(pk__in=favorite_recipe_ids)
        serializer = RecipeSerializer(recipes, context={'request': self.request}, many=True)
        return Response(serializer.data)


class FavoriteRecipeDetailAPIView(APIView):
    permission_classes = [IsAuthenticated]


    def post(self, request, recipe_id):
        return self.toggle_favorite(request, recipe_id, is_favorite=True)

    def delete(self, request, recipe_id):
        return self.toggle_favorite(request, recipe_id, is_favorite=False)

    def toggle_favorite(self, request, recipe_id, is_favorite):
        recipe = get_object_or_404(Recipe, pk=recipe_id)
        user = request.user

        try:
            favorite = FavoriteRecipe.objects.get(user=user, recipe=recipe)
            if not is_favorite:
                favorite.delete()
                return Response({"message": f"{recipe.title} removed from favorites."},
                                status=status.HTTP_204_NO_CONTENT)
            return Response({"message": f"{recipe.title} is already saved as a favorite."}, status=status.HTTP_200_OK)
        except FavoriteRecipe.DoesNotExist:
            if is_favorite:
                FavoriteRecipe.objects.create(user=user, recipe=recipe)
                return Response({"message": f"{recipe.title} saved as a favorite."}, status=status.HTTP_201_CREATED)
            return Response({"message": f"{recipe.title} is not in your favorites."}, status=status.HTTP_200_OK)
