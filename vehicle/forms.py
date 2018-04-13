from django import forms
from .models import Vehicle

class VehicleForm(forms.ModelForm):
    class Meta:
        model=Vehicle
        fields = ('cost_per_km','price','registration_plate','insurance_status',
        'no_of_km_travelled','fuel_type','mileage','vehicle_type','image')