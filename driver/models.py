from django.db import models

class Driver(models.Model):
    firstName=models.CharField(max_length=100)
    lastName=models.CharField(max_length=100)
    nationalId=models.CharField(max_length=13)
    address=models.CharField(max_length=1000)
    email=models.CharField(max_length=300)
    phoneNumber=models.CharField(max_length=10)
    licenseCategory=models.CharField(max_length=100)
    status_CHOICES=(
        ('B','booked'),
        ('NB','not booked')
    )
    status=models.CharField(
        max_length=2,
        choices=status_CHOICES,
        default='NB',
    )
    def __str__(self):
        return 'Driver name : '+self.firstName