from django.contrib import admin
from .models import Recipe, Ingredient


# Register your models here.

@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    pass

@admin.register(Ingredient)
class IngredientAdmin(admin.ModelAdmin):
    pass