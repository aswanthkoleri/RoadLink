from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from vehicle.models import Vehicle

# Create your models here.
class Repair(models.Model):
    registeredDate=models.DateTimeField(default=timezone.now)
    status_CHOICES=(
        ('S','solved'),
        ('NS','not solved')
    )
    status=models.CharField(
        max_length=2,
        choices=status_CHOICES,
        default='NS',
    )
    registeredUser=models.ForeignKey(User,default=None,on_delete=models.CASCADE)
    vehicle=models.ForeignKey(Vehicle,on_delete=models.CASCADE)
    issue=models.CharField(max_length=1000)
    def __str__(self):
        return 'issue : '+self.issue