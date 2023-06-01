from django.urls import path

from .views import RecipeView
from . import views

urlpatterns = [
    path('newRecipes/', RecipeView.as_view(), name='New_recipe'),
    path('addRecpies/', views.add_recipe, name='add-recipe'),
    path('seeRecpies/', views.see_recipes, name='see-recipe'),

]
