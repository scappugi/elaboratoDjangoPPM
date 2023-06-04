from django import forms
from django.forms import ModelForm
from .models import Recipe


class RecipeForm(ModelForm):
    class Meta:
        CHOICES = (
            # metodo debole per vincolare le risposte, ricorda che etichetta a destra è per utente sinistra per noi
            ('', ''),
            ('easy', 'easy'),
            ('medium', 'medium'),
            ('hard', 'hard'),
            ('really hard', 'really hard'),
        )
        CHOICES_CATEGORY = (
            ('', ''),
            ('First Plate', 'First plate'),
            ('Second Plate', 'Second Plate'),
            ('Dessert', 'Dessert'),
        )
        model = Recipe
        fields = ('recipesName', 'category', 'recipesDifficult', 'description')
        widgets = {'recipesDifficult': forms.Select(choices=CHOICES), 'category': forms.Select(choices=CHOICES_CATEGORY)}



