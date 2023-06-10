from django.contrib.auth.decorators import login_required, user_passes_test
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import TemplateView
from django.db.models import Q

from pages.forms import SearchForm
from recipes.models import Recipe


class HomePageView(TemplateView):
    template_name = "HomePage.html"


def seeAllRecipes(request):
    dati_ricette_queryset = Recipe.objects.all()  # recupera tutti gli oggetti
    return render(request, 'HomeWithRecipes.html', {'dati_ricette_queryset': dati_ricette_queryset})


def seeSearchRecipes(request):
    search_post = request.GET.get('search')

    if search_post and search_post.strip():
        posts = Recipe.objects.filter(Q(recipesName__icontains=search_post) | Q(description__icontains=search_post))
    else:
        return HttpResponseRedirect('/HomeRecipes/')

    return render(request, 'HomeWithRecipesSearched.html', {'data_query': posts})


def check_login(user):
    return True


@user_passes_test(check_login)
def seeRecipe(request, id):
    recipe = Recipe.objects.get(id=id)
    is_favorite = False
    if request.user.is_authenticated:
        is_favorite = recipe in request.user.favorite_recipe.all()
    context = {
        'recipe': recipe,
        'is_favorite': is_favorite
    }
    return render(request, 'see_selected_recipes.html', context)

