from django.contrib import admin

from .models import Dish


class DishAdmin(admin.ModelAdmin):
    list_display = ('dateCreation', 'name_dish', 'recipe', 'category')  # оставляем только имя и цену товара


admin.site.register(Dish, DishAdmin)

