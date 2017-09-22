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
        fields = ('uuid', 'name', 'imagePath', 'description', 'ingredients', 'publ')

    def create(self, validated_data):
        user = None
        request = self.context.get("request")
        if request and hasattr(request, "user"):
            user = request.user

        ingredients = validated_data.pop('ingredients')
        uuid = validated_data['uuid']
        if Recipe.objects.filter(uuid=uuid).count() == 0:
            recipe = Recipe.objects.create(user=user, **validated_data)
            for ingredient in ingredients:
                ing = Ingredient.objects.create(recipe=recipe, **ingredient)
            return recipe
        else:
            return Recipe.objects.first()

    def update(self, instance, validated_data):
        for ing in instance.ingredients.all():
            ing.delete()
        ingredients = validated_data.pop('ingredients')
        instance.name = validated_data.pop('name')
        instance.uuid = validated_data.pop('uuid')
        instance.imagePath = validated_data.pop('imagePath')
        instance.description = validated_data.pop('description')
        instance.publ = validated_data.pop('publ')

        for ingredient in ingredients:
            Ingredient.objects.create(recipe_id=instance.pk, **ingredient)
        return instance
