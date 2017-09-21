from rest_framework import viewsets

# noinspection PyUnresolvedReferences
from recipes.models import Recipe
# noinspection PyUnresolvedReferences
from recipes.serializers import RecipeSerializer


class RecipeViewSet(viewsets.ModelViewSet):
    def get_queryset(self):
        user = self.request.user
        return user.get_recipes()

    serializer_class = RecipeSerializer
    lookup_field = 'uuid'
