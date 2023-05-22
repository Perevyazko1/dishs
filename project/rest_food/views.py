from django.shortcuts import render
from rest_framework import generics, viewsets
from django_filters.rest_framework import DjangoFilterBackend
from .filters import RecipeFilter
from .models import Dish
from .serializers import DishSerializer


class DishAPIView(generics.ListAPIView):
    queryset = Dish.objects.all()
    serializer_class = DishSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = RecipeFilter
    # def get_queryset(self):
    #     queryset = Dish.objects.all()
    #     category = self.request.query_params.get('category', None)
    #     if category is not None:
    #         queryset = queryset.filter(category=category)
    #     return queryset