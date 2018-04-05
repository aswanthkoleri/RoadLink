from django import forms
from .models import Driver

class DriverForm(forms.ModelForm):

    class Meta:
        model=Driver
        fields=('firstName','lastName','nationalId','address','email','phoneNumber','licenseCategory',)