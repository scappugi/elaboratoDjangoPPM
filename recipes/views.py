from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render, redirect, get_object_or_404
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
        form = RecipeForm(request.POST, request.FILES)
        if form.is_valid() :
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
    dati_utente_queryset = Recipe.objects.filter(users__username=username)
    return render(request, 'see_recipes.html', {'dati_utente_queryset': dati_utente_queryset})


@login_required
def delete_recipes(request, id):
    objject = get_object_or_404(Recipe, id=id)
    if request.method == 'POST':
        if request.user.username == objject.users.username:  # controllo sul proprietario della ricetta
            objject.delete()
        return redirect('see-recipe')
    return render(request, 'delete_recipes.html', {'object': objject})


@login_required
def favorite_recipes(request, id):  # aggiunge
    # istanza della ricetta
    recipe = Recipe.objects.get(id=id)
    recipe.favorite.add(request.user)  # aggiunta
    return redirect('home_see_recipe', id=id)


@login_required
def see_favorite_recipes(request):
    preferiti = request.user.favorite_recipe.all()
    return render(request, 'see_favorite_recipes.html', {'preferiti': preferiti})


@login_required
def delete_favorite_recipes(request, id):
    oggetto = get_object_or_404(Recipe, id=id)
    if request.method == 'POST':
        request.user.favorite_recipe.remove(oggetto)
        return redirect('see-favorite-recipes')
    return render(request, 'delete_favorite_recipes.html', {'object': oggetto})


@login_required
def fast_delete_favorite_recipes(request, id):
    oggetto = get_object_or_404(Recipe, id=id)
    request.user.favorite_recipe.remove(oggetto)
    return redirect('home_see_recipe', id=id)
