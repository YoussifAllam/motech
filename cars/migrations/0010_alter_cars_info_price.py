# Generated by Django 5.0.2 on 2024-03-19 08:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("cars", "0009_alter_cars_info_car_code_alter_cars_info_price"),
    ]

    operations = [
        migrations.AlterField(
            model_name="cars_info",
            name="price",
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
    ]
