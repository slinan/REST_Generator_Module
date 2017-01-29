from django.shortcuts import render
from rest_framework import filters
from rest_framework import viewsets
from bikes4FreeApp.serializers import ComboSerializer, IngredientSerializer, BeverageSerializer, DishSerializer
from .models import Combo, Dish, Beverage, Ingredient


def index(request):
    return render(request, 'index.html')

# App

class ComboViewSet(viewsets.ModelViewSet):
    #authentication_classes = (SessionAuthentication, BasicAuthentication, TokenAuthentication)
    #permission_classes = (IsAuthenticated,estaDeshabilitado)
    queryset = Combo.objects.all().order_by('-id')
    serializer_class = ComboSerializer
    filter_backends = (filters.DjangoFilterBackend, filters.OrderingFilter)
    filter_fields = ('price', 'name')
    ordering_fields = ('price', 'name')

class DishViewSet(viewsets.ModelViewSet):
    #authentication_classes = (SessionAuthentication, BasicAuthentication, TokenAuthentication)
    #permission_classes = (IsAuthenticated,estaDeshabilitado)
    queryset = Dish.objects.all().order_by('-id')
    serializer_class = DishSerializer
    filter_backends = (filters.DjangoFilterBackend, filters.OrderingFilter)
    filter_fields = ('price', 'name', 'type', 'ingredient')
    ordering_fields = ('price', 'name', 'type', 'ingredient')

class BeverageViewSet(viewsets.ModelViewSet):
    #authentication_classes = (SessionAuthentication, BasicAuthentication, TokenAuthentication)
    #permission_classes = (IsAuthenticated,estaDeshabilitado)
    queryset = Beverage.objects.all().order_by('-id')
    serializer_class = BeverageSerializer
    filter_backends = (filters.DjangoFilterBackend, filters.OrderingFilter)
    filter_fields = ('price', 'type')
    ordering_fields = ('price', 'type')

class IngredientViewSet(viewsets.ModelViewSet):
    #authentication_classes = (SessionAuthentication, BasicAuthentication, TokenAuthentication)
    #permission_classes = (IsAuthenticated,estaDeshabilitado)
    queryset = Ingredient.objects.all().order_by('-id')
    serializer_class = IngredientSerializer
    filter_backends = (filters.DjangoFilterBackend, filters.OrderingFilter)
    filter_fields = ('price', 'type', 'name')
    ordering_fields = ('price', 'type', 'name')