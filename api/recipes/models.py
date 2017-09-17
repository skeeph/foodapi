from django.db import models

from django.utils.encoding import python_2_unicode_compatible


@python_2_unicode_compatible
class Ingredient(models.Model):
    name = models.CharField(max_length=256)
    amount = models.FloatField()
    unit = models.CharField(max_length=10)

    def __str__(self):
        return self.name


@python_2_unicode_compatible
class Recipe(models.Model):
    uuid = models.UUIDField()
    name = models.CharField(max_length=256)
    imagePath = models.URLField()
    description = models.TextField()
    ingredients = models.ManyToManyField(Ingredient, 'recipes')
    publ = models.BooleanField(default=False)

    def __str__(self):
        return self.name
