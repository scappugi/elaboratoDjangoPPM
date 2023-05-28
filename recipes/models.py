from django.contrib.auth.models import User
from django.db import models

from categories.models import Categories


class Recipe(models.Model):
    recipesName = models.CharField(primary_key=True, max_length=30)
    recipesDifficult= models.CharField(max_length=30)
    category=models.ForeignKey(Categories, on_delete=models.CASCADE)
    users=models.ForeignKey(User, on_delete=models.CASCADE)

