# Generated by Django 5.0.2 on 2024-03-03 11:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0003_cars_info_engine_capacity'),
    ]

    operations = [
        migrations.AddField(
            model_name='cars_info',
            name='Body_styel',
            field=models.CharField(default='SPORT PI', max_length=15),
        ),
        migrations.AddField(
            model_name='cars_info',
            name='Cylinders_type',
            field=models.CharField(choices=[('OPTION_1', '4'), ('OPTION_2', '6'), ('OPTION_3', '8')], default=0, max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='cars_info',
            name='Drive',
            field=models.CharField(default='4x4 w/Rear Wheel Drv', max_length=30),
        ),
        migrations.AddField(
            model_name='cars_info',
            name='Keys',
            field=models.CharField(choices=[('OPTION_1', 'Yes'), ('OPTION_2', 'No')], default=0, max_length=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='cars_info',
            name='Vehicle_Type',
            field=models.CharField(default='AUTOMOBILE', max_length=30),
        ),
        migrations.AddField(
            model_name='cars_info',
            name='Vin',
            field=models.CharField(default='3GNTKGE79DG260069', max_length=30),
        ),
        migrations.AlterField(
            model_name='cars_info',
            name='Fuel_Type',
            field=models.CharField(choices=[('OPTION_1', 'Petrol'), ('OPTION_2', 'Gas'), ('OPTION_3', 'FLEXIBLE FUEL'), ('OPTION_4', 'Electric')], max_length=20),
        ),
        migrations.AlterField(
            model_name='cars_info',
            name='control_type',
            field=models.CharField(choices=[('OPTION_1', 'AUTOMATIC'), ('OPTION_2', 'Manual'), ('OPTION_3', 'steptronic')], max_length=20),
        ),
        migrations.AlterField(
            model_name='cars_info',
            name='engine_capacity',
            field=models.CharField(max_length=30),
        ),
    ]