# Generated by Django 5.0.2 on 2024-03-05 10:12

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='RatingModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('UserName', models.CharField(max_length=20)),
                ('Num_OF_Stars', models.IntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(5)])),
                ('Rate_Desc', models.TextField()),
                ('Rate_date', models.DateField()),
            ],
            options={
                'verbose_name_plural': 'Rating Info',
                'ordering': ['-Rate_date'],
            },
        ),
    ]
