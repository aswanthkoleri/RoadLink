from django import forms
from .models import Repair

class RepairForm(forms.ModelForm):
    class Meta:
        model=Repair
        fields=('issue','vehicle',)
