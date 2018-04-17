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
    if request.user.is_authenticated:
        form=RepairForm()
        return render(request,'repair/index.html',{'form':form})
    else:
        return redirect("http://localhost:8000/home/404")

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
        if request.user.is_authenticated:
            form=RepairForm()
            error_message='Something went wrong error'
            return render(request,'repair/index.html',{ 'form' : form ,'error':error_message})
        else:
            return redirect("http://localhost:8000/home/404")

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
        if request.user.is_authenticated:
            repairsList = Repair.objects.all()
            return render(request,'repair/issues.html',{ 'repairsList' : repairsList})
        else:
            return redirect("http://localhost:8000/home/404")

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
        if request.user.is_authenticated:
            repair = Repair.objects.get(id=id)
            if repair.status == "S":
                repair.status = "NS"
            else:
                repair.status = "S"
            repair.save()
            repairsList = Repair.objects.all()
            return redirect('http://localhost:8000/repair/issues')
        else:
            return redirect("http://localhost:8000/home/404")

def edit(request,id):
    if request.method == "POST":
        repair=Repair.objects.get(id=id)
        form=RepairForm(request.POST,instance=repair)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.save()
            return redirect('http://localhost:8000/repair/issues')
    elif request.user.is_authenticated:
        repair=Repair.objects.get(id=id)
        form=RepairForm(instance=repair)
        return render(request,'repair/repairEdit.html',{ 'form' : form ,'id':id})