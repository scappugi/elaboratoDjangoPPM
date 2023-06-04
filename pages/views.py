from django.shortcuts import render
from django.views.generic import TemplateView

from pages.forms import SearchForm
from recipes.models import Recipe


class HomePageView(TemplateView):
    template_name = "HomePage.html"


def seeAllRecipes(request):
    dati_ricette_queryset = Recipe.objects.all()  # recupera tutti gli oggetti
    return render(request, 'HomeWithRecipes.html', {'dati_ricette_queryset': dati_ricette_queryset})


def seeSearchRecipes(request):
    results = []
    form = SearchForm(request.POST)
    if form.is_valid():
        search_query = form.cleaned_data['search_query']
        results = Recipe.objects.filter(recipesDifficult__icontains=search_query)

    return render(request, 'HomeWithRecipesSearched.html', {'form': form, 'results': results})
