# Generated by Django 5.0.2 on 2024-03-02 14:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0002_rename_car_model_cars_info_car_model_name_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='cars_info',
            name='engine_capacity',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
