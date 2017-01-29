from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Combo, Dish, Ingredient, Beverage


## App

class ComboSerializer(serializers.ModelSerializer):
    class Meta:
        model = Combo

class DishSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dish

class IngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredient

class BeverageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Beverage