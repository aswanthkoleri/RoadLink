from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from django.http import Http404
from django.template import loader
from .models import Vehicle
from .forms import VehicleForm
# Create your views here.

def index(request):
    form=VehicleForm()
    return render(request,'vehicle/index.html',{'form':form})

def addVehicle(request):
    if request.POST:
        form=VehicleForm(request.POST)
        if form.is_valid():
            form.save()
            success_message='Adding done'
            form=VehicleForm()
            return render(request,'vehicle/index.html',{'form':form,'success' : success_message})
    else:
        form=VehicleForm()
        error_message='Something went wrong error'
        return render(request,'vehicle/index.html',{ 'form' : form ,'error':error_message})

def showVehicles(request):
    if request.POST:
        # form=VehicleForm(request.POST)
        # if form.is_valid():
        #     form.save()
        #     success_message='Adding done'
        #     form=VehicleForm()
        return render(request,'vehicle/index.html')
    else:
        vehiclesList = Vehicle.objects.filter(owner=request.user)
        return render(request,'vehicle/vehiclelist.html',{ 'vehiclesList' : vehiclesList})

def delete(request,id):
    if request.POST:
        # form=RepairForm(request.POST)
        # if form.is_valid():
        #     instance=form.save(commit=False)
        #     instance.registeredUser=request.user
        #     instance.save()
        #     success_message='Issue Registered'
        #     form=RepairForm()
        return render(request,'vehicle/index.html',{'form':form})
    else:
        vehicle = Vehicle.objects.get(id=id)
        vehicle.delete()
        return redirect('http://localhost:8000/vehicle/vehicles')