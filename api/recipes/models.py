from django.db import models


# Create your models here.
class Ingredient(models.Model):
    name = models.CharField(max_length=256)
    amount = models.FloatField()
    unit = models.CharField(max_length=10)


class Recipe(models.Model):
    uuid = models.UUIDField()
    name = models.CharField(max_length=256)
    imagePath = models.URLField()
    description = models.TextField()
    ingredients = models.ManyToManyField(Ingredient, 'recipes')
