from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend
from .filters import RecipeFilter
from .models import Dish
from .serializers import DishSerializer


class DishAPIView(generics.ListAPIView):
    queryset = Dish.objects.all()
    serializer_class = DishSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = RecipeFilter
