from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from .forms import RecipeForm
from django.http import HttpResponseRedirect
from recipes.models import Recipe


class RecipeView(TemplateView):
    template_name = 'new_recipes.html'


@login_required
def add_recipe(request):
    submitted = False
    if request.method == "POST":
        form = RecipeForm(request.POST)
        if form.is_valid():
            set_user = form.save(commit=False)
            set_user.users = request.user
            set_user.save()
            submitted = True
            return HttpResponseRedirect('/recipes/addRecpies/')

    else:
        form = RecipeForm
        if 'submitted' in request.GET:
            submitted = True

    form = RecipeForm
    return render(request, 'new_recipes.html', {'form': form})


@login_required
def see_recipes(request):
    username = request.user.username  # recupero username

    try:
        dati_utente_queryset = Recipe.objects.filter(users__username=username)
        return render(request, 'see_recipes.html', {'dati_utente_queryset': dati_utente_queryset})

    except ObjectDoesNotExist:
        error_message = f"Recipes object not found for username: {username}"
        return render(request, 'see_recipes.html', {'error_message': error_message})

