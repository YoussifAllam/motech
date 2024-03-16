from django.db import models
import uuid
# Create your models here.



class Cars_Info(models.Model):
    Keys = [
    ('Yes', 'Yes'),
    ('No', 'No'),
    ]

    control_type = [    
        ('AUTOMATIC', 'AUTOMATIC'),
        ('Manual', 'Manual'),
        ('steptronic', 'steptronic'),
    ]

    Fuel_Type = [
        ('Petrol', 'Petrol'),
        ('Gas', 'Gas'),
        ('FLEXIBLE FUEL', 'FLEXIBLE FUEL'),
        ('Electric', 'Electric'),
    ]

    Cylinders_type = [
        ('4', '4'),
        ('6', '6'),
        ('8', '8'),
    ]

    Company_name = models.CharField(max_length= 50  )
    Car_model_name = models.CharField(max_length= 50  )
    status =  models.CharField(max_length= 20  ) # new , used 
    price  = models.DecimalField(max_digits=10, decimal_places=2)
    production_year = models.IntegerField ()
    mileage  = models.IntegerField() # number of miles that the cat done
    Car_Color = models.CharField(max_length=10)
    engine_capacity = models.CharField(max_length=30)
    Vin = models.CharField(default = '3GNTKGE79DG260069',max_length=30)
    Body_styel = models.CharField(default = 'SPORT PI',max_length=15)
    Drive = models.CharField(default = '4x4 w/Rear Wheel Drv',max_length=30)
    Vehicle_Type = models.CharField(default = 'AUTOMOBILE',max_length=30)
    
    Cylinders_type = models.CharField(choices=Cylinders_type,max_length=20)
    Keys = models.CharField(choices=Keys , max_length=10)
    control_type = models.CharField(choices=control_type,max_length=20 ) # e.g., manual, automatic, CVT
    Fuel_Type = models.CharField(choices=Fuel_Type,max_length=20 )
    description = models.TextField()
    
    class Meta:
        verbose_name_plural = "Cars Info"
        ordering = ['production_year', '-price']

    def __str__(self):
        return f" {self.Car_model_name} , Car Num : {self.pk} "


class CarPhoto(models.Model):
    car = models.ForeignKey(Cars_Info, on_delete=models.CASCADE, related_name='photos')
    photo = models.ImageField(upload_to='cars_photos/')

    def __str__(self):
        return f"Photo for {self.car.Car_model_name} , Car num : {self.car.pk} ,  Photo num {self.pk}"