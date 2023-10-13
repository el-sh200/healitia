from django.urls import path
from . import views

app_name = 'recipe'

urlpatterns = [
    path('', views.RecipeListAPIView.as_view(), name='recipe_list'),
    path('<int:pk>/', views.RecipeDetailAPIView.as_view(), name='recipe_detail'),
    path('favorite-recipes/', views.FavoriteRecipeListAPIView.as_view(), name='recipe_favorite_list'),
    path('<int:recipe_id>/favorite/', views.FavoriteRecipeDetailAPIView.as_view(), name='recipe_favorite'),
    path('<int:recipe_id>/get-single-favorite/', views.FavoriteRetrieveAPIView.as_view(), name='get_single_favorite'),
]
