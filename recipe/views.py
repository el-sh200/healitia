from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Recipe
from .serializers import RecipeSerializer


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
