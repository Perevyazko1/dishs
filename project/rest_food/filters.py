import django_filters
from .models import Dish


class RecipeFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Dish
        fields = ['category', 'id']