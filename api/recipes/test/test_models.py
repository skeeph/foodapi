import uuid

from django.test import TestCase

# Create your tests here.
# noinspection PyUnresolvedReferences
from recipes.models import Recipe, Ingredient
# noinspection PyUnresolvedReferences
from users.models import User


class RecipeTest(TestCase):
    def setUp(self):
        User.objects.create(username="testuser")
        Recipe.objects.create(name="Recipe",
                              user=User.objects.first(),
                              uuid=uuid.uuid4(),
                              imagePath="",
                              description="")

    def test_str(self):
        self.assertEqual(str(Recipe.objects.first()), "Recipe")


class IngredientTest(TestCase):
    def setUp(self):
        Ingredient.objects.create(name="Ingredient",
                                  amount=50,
                                  unit="g")

    def test_str(self):
        self.assertEqual(str(Ingredient.objects.first()), "Ingredient")
