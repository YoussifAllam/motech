# Generated by Django 5.0.2 on 2024-03-21 12:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("RatingApp", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="ratingmodel",
            name="Rate_Desc",
            field=models.CharField(max_length=255),
        ),
    ]