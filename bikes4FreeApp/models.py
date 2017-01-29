from django.db import models
from django.contrib.auth.models import User
from django.template.backends import django
from rest_framework.authtoken.models import Token
from django.db.models.signals import post_save
from django.dispatch import receiver
from decimal import Decimal
import django

# App

class Ingredient(models.Model):
    price = models.FloatField()
    type = models.CharField(max_length=300)
    name = models.CharField(max_length=300, unique=True)

class Dish(models.Model):
    price = models.FloatField()
    name = models.CharField(max_length=300)
    type = models.CharField(max_length=300)
    ingredient = models.ForeignKey(Ingredient)

class Beverage(models.Model):
    price = models.FloatField()
    type = models.CharField(max_length=300)

class Combo(models.Model):
    price = models.FloatField()
    name = models.CharField(max_length=300, unique=True)
    dish = models.ForeignKey(Dish)
    beverage = models.ForeignKey(Beverage)

    # python manage.py makemigrations bikes4FreeApp
    # python manage.py sqlmigrate bikes4FreeApp 0001
    # python manage.py migrate
    # python manage.py createsuperuser
    # $ heroku run python manage.py migrate