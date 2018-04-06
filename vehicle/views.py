from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from django.http import Http404
from django.template import loader
from .models import Vehicle
from .forms import VehicleForm
# Create your views here.

def index(request):
    form=VehicleForm()
    return render(request,'vehicle/add_vehicle.html',{'form':form})

def create_vehicle(request):
    if request.POST:
        form=VehicleForm(request.POST)
        if form.is_valid():
            form.save()
            success_message='Adding done'
            form=VehicleForm()
            return render(request,'vehicle/add_vehicle.html.html',{'form':form,'success' : success_message})
    else:
        form=VehicleForm()
        error_message='Something went wrong error'
        return render(request,'vehicle/add_vehicle.html.html',{ 'form' : form ,'error':error_message})

def viewall_vehicle(request):
    list = Vehicle.objects.all()
    return render(request,'vehicle/view_vehicle.html',{'list':list})        