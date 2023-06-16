from django.urls import path

from .views import RecipeView
from . import views


urlpatterns = [
    path('newRecipes/', RecipeView.as_view(), name='New_recipe'),
    path('addRecpies/', views.add_recipe, name='add-recipe'),
    path('seeRecpies/', views.see_recipes, name='see-recipe'),
    path('delete/<int:id>/', views.delete_recipes, name='delete-recipes'),
    path('favorite/<int:id>', views.favorite_recipes, name='favorite-recipes'),
    path('seefavorite/', views.see_favorite_recipes, name='see-favorite-recipes'),
    path('deleteFavorite/<int:id>', views.delete_favorite_recipes, name='delete-favorite-recipes'),
    path('fastdeleteFavorite/<int:id>', views.fast_delete_favorite_recipes, name='fast-delete-favorite-recipes')


]
