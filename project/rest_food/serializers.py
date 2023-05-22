from rest_framework import serializers
from .models import Dish


class DishSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dish
        fields = ('id', 'dateCreation', 'name_dish', 'recipe', 'category', 'image')