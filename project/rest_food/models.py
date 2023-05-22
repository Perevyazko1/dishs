from django.db import models


class Dish(models.Model):
    name_dish = models.TextField(max_length=128)
    recipe = models.TextField()
    dateCreation = models.DateTimeField(auto_now_add=True, verbose_name='Дата')
    image = models.URLField(default=None)

    RUSSIAN_FOOD = 'RU'
    KAZAKH_FOOD = 'KZ'
    AMERICAN_FOOD = 'USA'

    CATEGORY_CHOICES = (
        (RUSSIAN_FOOD, 'Русская кухня'),
        (KAZAKH_FOOD, 'Казахская кухня'),
        (AMERICAN_FOOD, 'Американская кухня'),
    )

    category = models.CharField(
        max_length=128, choices=CATEGORY_CHOICES,
        default=RUSSIAN_FOOD, verbose_name='Тип'
    )


