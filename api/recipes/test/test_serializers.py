# -*- coding: utf-8 -*-
from django.test import TestCase

# noinspection PyUnresolvedReferences
from recipes.serializers import RecipeSerializer
# noinspection PyUnresolvedReferences
from users.models import User

# noinspection PyUnresolvedReferences
from recipes.models import Recipe


class RecipesSerializer(TestCase):
    def setUp(self):
        self.user = User.objects.create(username="test_user")
        self.recipe_data = {"description": "https://pikabu.ru/story/arbuznyiy_burger_5284556",
                            "uuid": "7ce95ba1-2555-4d0e-d327-2fe05993cb81",
                            "imagePath": "https://cs9.pikabu.ru/post_img/2017/08/22/10/1503421660120544798.jpg",
                            "ingredients": [
                                {"amount": 4, "name": "Арбуз", "unit": "куска"}
                            ], "name": "Арбузный бургер",
                            "publ": True}

    def test_serializer_with_empty_data(self):
        serializer = RecipeSerializer(data={})
        self.assertFalse(serializer.is_valid())

    def test_serializer_with_valid_data(self):
        serializer = RecipeSerializer(data=self.recipe_data)
        self.assertTrue(serializer.is_valid())

    def test_update_serializer(self):
        serializer = RecipeSerializer(data=self.recipe_data)
        if serializer.is_valid():
            serializer.save(user=self.user)
        data = self.recipe_data.copy()
        data["name"] = "UPDATED {}".format(data["name"])
        data["description"] = "UPDATED {}".format(data["name"])
        data['ingredients'].append({"amount": 200, "name": "Сливочный сыр", "unit": "гр"})
        serializer.update(serializer.instance, data)
        self.assertTrue(serializer)
        self.assertEqual(Recipe.objects.first().ingredients.count(),2)
