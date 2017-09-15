from rest_framework import serializers

# noinspection PyUnresolvedReferences
from recipes.models import Recipe, Ingredient


class IngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredient
        fields = ('name', 'amount', 'unit')


class RecipeSerializer(serializers.ModelSerializer):
    ingredients = IngredientSerializer(many=True)

    class Meta:
        model = Recipe
        fields = ('uuid', 'name', 'imagePath', 'description', 'ingredients')

    def create(self, validated_data):
        ingredients = validated_data.pop('ingredients')
        recipe = Recipe.objects.create(**validated_data)
        for ingredient in ingredients:
            ing = Ingredient.objects.create(**ingredient)
            recipe.ingredients.add(ing)
        return recipe

    def update(self, instance, validated_data):
        ingredients = validated_data.pop('ingredients')
        instance.name = validated_data.pop('name')
        instance.id = validated_data.pop('uuid')
        instance.imagePath = validated_data.pop('imagePath')
        instance.description = validated_data.pop('description')
        for ingredient in ingredients:
            ing = Ingredient.objects.create(**ingredient)
            # FIXME instance.ingredients.add(ing)
        return instance
