from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from django.http import Http404
from django.template import loader
from .models import Repair
from .forms import RepairForm
import requests
import geopy.distance
# Create your views here.

def index(request):
    form=RepairForm()
    return render(request,'repair/index.html',{'form':form})

def repair(request):
    if request.POST:
        form=RepairForm(request.POST)
        if form.is_valid():
            instance=form.save(commit=False)
            instance.registeredUser=request.user
            instance.save()
            success_message='Issue Registered'
            form=RepairForm()
            return render(request,'repair/index.html',{'form':form,'success' : success_message})
    else:
        form=RepairForm()
        error_message='Something went wrong error'
        return render(request,'repair/index.html',{ 'form' : form ,'error':error_message})

def issues(request):
    if request.POST:
        # form=RepairForm(request.POST)
        # if form.is_valid():
        #     instance=form.save(commit=False)
        #     instance.registeredUser=request.user
        #     instance.save()
        #     success_message='Issue Registered'
        #     form=RepairForm()
        return render(request,'repair/index.html',{'form':form})
    else:
        repairsList = Repair.objects.all()
        return render(request,'repair/issues.html',{ 'repairsList' : repairsList})

def update(request,id):
    if request.POST:
        # form=RepairForm(request.POST)
        # if form.is_valid():
        #     instance=form.save(commit=False)
        #     instance.registeredUser=request.user
        #     instance.save()
        #     success_message='Issue Registered'
        #     form=RepairForm()
        return render(request,'repair/index.html',{'form':form})
    else:
        repair = Repair.objects.get(id=id)
        repair.status = "S"
        repair.save()
        repairsList = Repair.objects.all()
        return redirect('http://localhost:8000/repair/issues')