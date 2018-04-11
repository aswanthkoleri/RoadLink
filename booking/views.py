from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from django.http import Http404
from django.template import loader
from .models import Book
from .forms import BookForm
import requests
import geopy.distance
# Create your views here.

def index(request):
    form=BookForm()
    return render(request,'booking/index.html',{'form':form})

def book(request):
    if request.POST:
        form=BookForm(request.POST)
        if form.is_valid():
            instance=form.save(commit=False)
            instance.allottedUser=request.user
            url = 'https://maps.googleapis.com/maps/api/geocode/json?address=' +instance.source+ ',+CA&key=AIzaSyBKmBYERZyz9Cj7-F9bT7WMWVuSHiaX9kU'
            r = requests.get(url)
            results = r.json()
            source_latitude = results["results"][0]["geometry"]["location"]["lat"]
            source_longitude = results["results"][0]["geometry"]["location"]["lng"]
            instance.source_longitude=source_longitude
            instance.source_latitude=source_latitude
            url = 'https://maps.googleapis.com/maps/api/geocode/json?address=' +instance.destination+ ',+CA&key=AIzaSyBKmBYERZyz9Cj7-F9bT7WMWVuSHiaX9kU'
            r = requests.get(url)
            results = r.json()
            destination_latitude = results["results"][0]["geometry"]["location"]["lat"]
            destination_longitude = results["results"][0]["geometry"]["location"]["lng"]
            instance.destination_longitude=destination_longitude
            instance.destination_latitude=destination_latitude
            coords_1 = (source_latitude, source_longitude)
            coords_2 = (destination_latitude, destination_longitude)
            distance=geopy.distance.vincenty(coords_1, coords_2).km
            instance.distance=distance
            instance.save()
            success_message='Booking done'
            form=BookForm()
            return render(request,'booking/index.html',{'form':form,'success' : success_message})
    else:
        form=BookForm()
        error_message='Something went wrong error'
        return render(request,'booking/index.html',{ 'form' : form ,'error':error_message})