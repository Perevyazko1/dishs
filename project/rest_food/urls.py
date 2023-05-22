from django.urls import path

from .views import DishAPIView

urlpatterns = [
    path('', DishAPIView.as_view()),

]