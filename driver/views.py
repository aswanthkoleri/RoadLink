from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from django.http import Http404
from django.template import loader
from .models import Driver
# Create your views here.

def index(request):
    return render(request,'driver/index.html')

def driver(request):
    driver=Driver(
        firstName=request.POST['firstName'],
        lastName=request.POST['lastName'],
        nationalId=request.POST['nationalId'],
        address=request.POST['nationalId'],
        email=request.POST['email'],
        phoneNumber=request.POST['phoneNumber'],
        licenseCategory=request.POST['licenseCategory'],
    )
    driver.save()
    return render(request,'driver/index.html')