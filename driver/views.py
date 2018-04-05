from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from django.http import Http404
from django.template import loader
from .models import Driver
from .forms import DriverForm
# Create your views here.

def index(request):
    form=DriverForm()
    return render(request,'driver/index.html',{'form':form})

def driver(request):
    if request.POST:
        form=DriverForm(request.POST)
        if form.is_valid():
            form.save()
            success_message='Driver registered'
            form=DriverForm()
            return render(request,'driver/index.html',{'form':form,'success' : success_message})
    else:
        form=DriverForm()
        error_message='Something went wrong error'
        return render(request,'driver/index.html',{ 'form' : form ,'error':error_message})