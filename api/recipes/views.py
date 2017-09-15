from rest_framework import viewsets

# noinspection PyUnresolvedReferences
from recipes.models import Recipe
# noinspection PyUnresolvedReferences
from recipes.serializers import RecipeSerializer


class RecipeViewSet(viewsets.ModelViewSet):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer
