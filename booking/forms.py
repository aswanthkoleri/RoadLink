from django import forms
from .models import Book

class BookForm(forms.ModelForm):
    startDate=forms.DateTimeField(widget=forms.DateTimeInput(attrs={'type':'date'}))
    endDate=forms.DateTimeField(widget=forms.DateTimeInput(attrs={'type':'date'}))
    class Meta:
        model=Book
        fields=('source','destination','startDate','endDate','securityDeposit','discountId','vehicle',)
