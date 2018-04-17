from django.shortcuts import render,get_object_or_404,redirect
from django.http import HttpResponse
from django.http import Http404
from django.template import loader
from .models import Driver
from .forms import DriverForm
# Create your views here.

def index(request):
    if request.user.is_authenticated:
        form=DriverForm()
        return render(request,'driver/index.html',{'form':form})
    else:
        return redirect("http://localhost:8000/home/404")

def driver(request):
    if request.POST:
        form=DriverForm(request.POST)
        if form.is_valid():
            form.save()
            success_message='Driver registered'
            form=DriverForm()
            return render(request,'driver/index.html',{'form':form,'success' : success_message})
    else:
        if request.user.is_authenticated:
            form=DriverForm()
            error_message='Something went wrong error'
            return render(request,'driver/index.html',{ 'form' : form ,'error':error_message})
        else:
            return redirect("http://localhost:8000/home/404")

def drivers(request):
    if request.POST:
        form=DriverForm(request.POST)
        return render(request,'driver/index.html',{'form':form})
    else:
        if request.user.is_authenticated:
            drivers = Driver.objects.all()
            return render(request,'driver/driverlist.html',{ 'drivers' : drivers ,'user':request.user})
        else:
            return redirect("http://localhost:8000/home/404")

def delete(request,id):
    if request.POST:
        return render(request,'driver/index.html',{'form':form})
    else:
        if request.user.is_authenticated:
            drivers = Driver.objects.get(id=id)
            drivers.delete()
            return redirect('http://localhost:8000/driver/drivers')
        else:
            return redirect("http://localhost:8000/home/404")

def edit(request,id):
    if request.method == "POST":
        driver=Driver.objects.get(id=id)
        form=DriverForm(request.POST,instance=driver)
        if form.is_valid():
            form.save()
            return redirect('http://localhost:8000/driver/drivers')
    elif request.user.is_authenticated:
        driver=Driver.objects.get(id=id)
        form=DriverForm(instance=driver)
        return render(request,'driver/driverEdit.html',{ 'form' : form ,'id':id})
    
        