from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from django.http import Http404
from django.utils import timezone
from django.template import loader
from .models import Book
from driver.models import Driver
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
            print('success')
            instance=form.save(commit=False)
            instance.allottedUser=request.user
            url = 'https://maps.googleapis.com/maps/api/geocode/json?address=' +instance.source+ ',+CA&key=AIzaSyBKmBYERZyz9Cj7-F9bT7WMWVuSHiaX9kU'
            print(url)
            r = requests.get(url)
            results = r.json()
            print(results)
            source_latitude = results["results"][0]["geometry"]["location"]["lat"]
            source_longitude = results["results"][0]["geometry"]["location"]["lng"]
            instance.source_longitude=source_longitude
            instance.source_latitude=source_latitude
            url = 'https://maps.googleapis.com/maps/api/geocode/json?address=' +instance.destination+ ',+CA&key=AIzaSyBKmBYERZyz9Cj7-F9bT7WMWVuSHiaX9kU'
            r = requests.get(url)
            print(r)
            print(url)
            results = r.json()
            destination_latitude = results["results"][0]["geometry"]["location"]["lat"]
            destination_longitude = results["results"][0]["geometry"]["location"]["lng"]
            instance.destination_longitude=destination_longitude
            instance.destination_latitude=destination_latitude
            coords_1 = (source_latitude, source_longitude)
            coords_2 = (destination_latitude, destination_longitude)
            distance=geopy.distance.vincenty(coords_1, coords_2).km
            instance.distance=distance
            print(instance.distance)
            print(instance.vehicle.cost_per_km)
            instance.cost=float(instance.vehicle.cost_per_km)*float(instance.distance)
            instance.save()
            print('success')
            success_message='Booking done'
            return render(request,'booking/success.html',{'details': instance ,'success' : success_message})
    else:
        form=BookForm()
        error_message='Something went wrong error'
        return render(request,'booking/index.html',{ 'form' : form ,'error':error_message})

def booking(request):
    if request.POST:
        form=BookForm(request.POST)
        return render(request,'booking/index.html',{'form':form})
    else:
        bookings = Book.objects.all()
        for booking in bookings:
            if booking.status=="B" and timezone.now()>booking.endDate:
                vehicle = booking.vehicle
                vehicle.status="NB"
                vehicle.save()
                booking.status="E"
                driver=booking.allottedDriver
                booking.allottedDriver=None
                driver.status="NB"
                booking.save()
                driver.save()
            elif booking.status=="NB" and timezone.now()>booking.endDate:
                booking.status="E"
                booking.save()
        if request.user.is_superuser:
            return render(request,'booking/bookinglist.html',{ 'bookings' : bookings ,'user':request.user})
        else:
            bookings = Book.objects.filter(allottedUser=request.user)
            return render(request,'booking/bookinglist.html',{ 'bookings' : bookings ,'user':request.user})

def delete(request,id):
    if request.POST:
        return render(request,'vehicle/index.html',{'form':form})
    else:
        booking = Book.objects.get(id=id)
        booking.delete()
        return redirect('http://localhost:8000/booking/bookings')

def change(request,id):
    if request.POST:
        return render(request,'repair/index.html',{'form':form})
    else:
        booking = Book.objects.get(id=id)
        if booking.status == "B":
            vehicle = booking.vehicle
            vehicle.vehicle_status="NB"
            vehicle.save()
            booking.status = "NB"
            driver=booking.allottedDriver
            driver.status="NB"
            driver.save()
            booking.allottedDriver = None
        else:
            booking.status = "B"
            drivers = Driver.objects.filter(status="NB")
            for driver in drivers:
                vehicle = booking.vehicle
                if vehicle.vehicle_status == "B":
                    bookings = Book.objects.all()
                    return redirect('http://localhost:8000/booking/bookings')
                else:    
                    vehicle.vehicle_status="B"
                    vehicle.save()
                    booking.allottedDriver = driver
                    driver.status="B"
                    driver.save()
                break
        booking.save()
        return redirect('http://localhost:8000/booking/bookings')
