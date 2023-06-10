from django.contrib.auth.models import User
from django.db import models


class Recipe(models.Model):
    recipesName = models.CharField(max_length=30)
    recipesDifficult = models.CharField(max_length=30)
    category = models.CharField(blank=True, max_length=30, null=True)
    users = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE)
    description = models.CharField(max_length=2000, null=True)  # deve consentire una breve descrizione del piatto
    favorite = models.ManyToManyField(User, related_name='favorite_recipe')