# Generated by Django 4.2.1 on 2023-05-21 17:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rest_food', '0002_dish_image_alter_dish_name_dish'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dish',
            name='image',
            field=models.URLField(default=None),
        ),
    ]
