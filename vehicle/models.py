from django.db import models

class Vehicle(models.Model):
    VEHICLE_STATUS_CHOICES = (
        ('B', 'Booked'),
        ('NB', 'Not Booked'),
    )
    INSURANCE_STATUS_CHOICES = (
        ('U','Updated'),
        ('NU','Not Updated'),
    )
    VEHICLE_TYPE_CHOICES = (
        ('P','Passenger'),
        ('T','Truck'),
        ('C','Construction'),
    )
    owner = models.CharField(max_length=200)
    cost_per_km = models.DecimalField(max_digits=20, decimal_places=3)
    price = models.DecimalField(max_digits=20, decimal_places=3)
    registration_plate = models.CharField(max_length=200)
    vehicle_status = models.CharField(max_length=2,default='NB',choices=VEHICLE_STATUS_CHOICES)
    insurance_status = models.CharField(max_length=2,choices=INSURANCE_STATUS_CHOICES)
    no_of_km_travelled = models.DecimalField(max_digits=20, decimal_places=0)
    fuel_type = models.CharField(max_length=200)
    mileage = models.DecimalField(max_digits=20, decimal_places=0)
    vehicle_type = models.CharField(max_length=1,choices=VEHICLE_TYPE_CHOICES)

    def __str__(self):
        return self.registration_plate



