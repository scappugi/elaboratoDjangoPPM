from django.urls import path
from .views import HomePageView
from . import views

urlpatterns = [
    path("", HomePageView.as_view(), name="home"),
    path('HomeRecipes/', views.seeAllRecipes, name='home_recipes'),
    path('HomeSearchingRecpies/', views.seeSearchRecipes, name='home_researching_recipes')
]
