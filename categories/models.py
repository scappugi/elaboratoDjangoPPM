from django.db import models

class Categories(models.Model):
    recipesCategory = models.CharField(primary_key=True, max_length=30)
