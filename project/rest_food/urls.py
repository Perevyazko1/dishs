from django.urls import path
from django.views.decorators.cache import cache_page

from .views import DishAPIView

urlpatterns = [
    path('', DishAPIView.as_view()),

]