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

from django.core.mail import send_mail
from django.core.mail import EmailMessage
# Create your views here.


def index(request):
    if request.user.is_authenticated:
        form=BookForm()
        return render(request,'booking/index.html',{'form':form})
    else:
        return redirect("http://localhost:8000/home/404")

def pay(request):
    if request.user.is_authenticated:
        return render(request,'booking/payment.html')
    else:
        return redirect("http://localhost:8000/home/404")

def book(request):
    if request.POST:
        form=BookForm(request.POST)
        if form.is_valid():
            print('success')
            instance=form.save(commit=False)
            instance.allottedUser=request.user
            source=instance.source
            source=source.replace(" ","+")
            instance.source=source
            print(instance.source)
            destination=instance.destination
            destination=destination.replace(" ","+")
            instance.destination=destination
            print(instance.destination)
            url='https://maps.googleapis.com/maps/api/distancematrix/json?units=metric&origins='+source +'&destinations='+destination+'&key=AIzaSyBKmBYERZyz9Cj7-F9bT7WMWVuSHiaX9kU';
            print(url)
            r = requests.get(url)
            results = r.json()
            instance.distance=int(results["rows"][0]["elements"][0]["distance"]["value"]/1000)
            instance.duration=results["rows"][0]["elements"][0]["duration"]["text"]
            print(instance.distance)
            print(instance.vehicle.cost_per_km)
            instance.cost=int(float(instance.vehicle.cost_per_km)*float(instance.distance))
            instance.save()
            print('success')
            success_message='Booking done. You will be informed once the booking is confirmed'
            return render(request,'booking/success.html',{'details': instance ,'success' : success_message})
    else:
        if request.user.is_authenticated:
            form=BookForm()
            error_message='Something went wrong error'
            return render(request,'booking/index.html',{ 'form' : form ,'error':error_message})
        else:
            return redirect("http://localhost:8000/home/404")

def booking(request):
    if request.POST:
        form=BookForm(request.POST)
        return render(request,'booking/index.html',{'form':form})
    else:
        if request.user.is_authenticated:
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
        else:
            return redirect("http://localhost:8000/home/404")

def delete(request,id):
    if request.POST:
        return render(request,'vehicle/index.html',{'form':form})
    else:
        if request.user.is_authenticated:
            booking = Book.objects.get(id=id)
            booking.delete()
            return redirect('http://localhost:8000/booking/bookings')
        else:
            return redirect("http://localhost:8000/home/404")

def change(request,id):
    if request.POST:
        return render(request,'booking/index.html',{'form':form})
    else:
        if request.user.is_authenticated:
            booking = Book.objects.get(id=id)
            if booking.status == "B":
                vehicle = booking.vehicle
                vehicle.vehicle_status="NB"
                driver=booking.allottedDriver
                driver.status="NB"
                vehicle.save()
                driver.save()
                booking.status = "NB"
                booking.allottedDriver = None
                booking.save()
            else:
                drivers = Driver.objects.filter(status="NB")
                if drivers:
                    for driver in drivers:
                        vehicle = booking.vehicle
                        if vehicle.vehicle_status == "B":
                            failure_message="Vehicle already booked"
                            return redirect('http://localhost:8000/booking/bookings')
                        else:
                            booking.status = "B"
                            vehicle.vehicle_status="B"
                            vehicle.save()
                            booking.allottedDriver = driver
                            driver.status="B"
                            driver.save()
                            msg = EmailMessage(
                               'Your Booking Has Been Confirmed',
                               '<!DOCTYPE html><html><head><title></title><meta http-equiv="Content-Type" content="text/html; charset=utf-8"/><meta name="viewport" content="width=device-width, initial-scale=1"><meta http-equiv="X-UA-Compatible" content="IE=edge"/><body style="margin: 0 !important; padding: 0 !important; background-color: #eeeeee;" bgcolor="#eeeeee"><div style="display: none; font-size: 1px; color: #fefefe; line-height: 1px; font-family: Open Sans, Helvetica, Arial, sans-serif; max-height: 0px; max-width: 0px; opacity: 0; overflow: hidden;">Confirmation of your booking - RoadLink!</div><table border="0" cellpadding="0" cellspacing="0" width="100%"> <tr> <td align="center" style="background-color: #eeeeee;" bgcolor="#eeeeee"><!--[if (gte mso 9)|(IE)]> <table align="center" border="0" cellspacing="0" cellpadding="0" width="600"> <tr> <td align="center" valign="top" width="600"><![endif]--> <table align="center" border="0" cellpadding="0" cellspacing="0" width="100%" style="max-width:600px;"> <tr> <td align="center" valign="top" style="font-size:0; padding: 35px;" bgcolor="#044767"><!--[if (gte mso 9)|(IE)]> <table align="center" border="0" cellspacing="0" cellpadding="0" width="600"> <tr> <td align="left" valign="top" width="300"><![endif]--> <div style="display:inline-block; max-width:50%; min-width:100px; vertical-align:top; width:100%;"> <table align="left" border="0" cellpadding="0" cellspacing="0" width="100%" style="max-width:300px;"> <tr> <td align="left" valign="top" style="font-family: Open Sans, Helvetica, Arial, sans-serif; font-size: 36px; font-weight: 800; line-height: 48px;" class="mobile-center"> <h1 style="font-size: 36px; font-weight: 800; margin: 0; color: #ffffff;">RoadLink</h1> </td></tr></table> </div><!--[if (gte mso 9)|(IE)]> </td><td align="right" width="300"><![endif]--> <div style="display:inline-block; max-width:50%; min-width:100px; vertical-align:top; width:100%;" class="mobile-hide"> <table align="left" border="0" cellpadding="0" cellspacing="0" width="100%" style="max-width:300px;"> <tr> <td align="right" valign="top" style="font-family: Open Sans, Helvetica, Arial, sans-serif; font-size: 48px; font-weight: 400; line-height: 48px;"> <table cellspacing="0" cellpadding="0" border="0" align="right"> <tr> <td style="font-family: Open Sans, Helvetica, Arial, sans-serif; font-size: 18px; font-weight: 400;"> <p style="font-size: 18px; font-weight: 400; margin: 0; color: #ffffff;"></p></td><td style="font-family: Open Sans, Helvetica, Arial, sans-serif; font-size: 18px; font-weight: 400; line-height: 24px;">  </td></tr></table> </td></tr></table> </div><!--[if (gte mso 9)|(IE)]> </td></tr></table><![endif]--> </td></tr><tr> <td align="center" style="padding: 35px 35px 20px 35px; background-color: #ffffff;" bgcolor="#ffffff"><!--[if (gte mso 9)|(IE)]> <table align="center" border="0" cellspacing="0" cellpadding="0" width="600"> <tr> <td align="center" valign="top" width="600"><![endif]--> <table align="center" border="0" cellpadding="0" cellspacing="0" width="100%" style="max-width:600px;"> <tr> <td align="center" style="font-family: Open Sans, Helvetica, Arial, sans-serif; font-size: 16px; font-weight: 400; line-height: 24px; padding-top: 25px;"> <img src="https://goo.gl/fZqQ2F" width="125" height="120" style="display: block; border: 0px;"/><br><h2 style="font-size: 30px; font-weight: 800; line-height: 36px; color: #333333; margin: 0;"> Your Booking is Confirmed!<br><h2><h3><a href="http://localhost:8000/booking/bookings">See your Booking</a> </h3> </td></tr><tr> <td align="left" style="font-family: Open Sans, Helvetica, Arial, sans-serif; font-size: 16px; font-weight: 400; line-height: 24px; padding-top: 10px;"> <p style="font-size: 16px; font-weight: 400; line-height: 24px; color: #777777;"> </p></td></tr><tr> <td align="left" style="padding-top: 20px;"> </td></tr><tr> <td align="left" style="padding-top: 20px;"> <table cellspacing="0" cellpadding="0" border="0" width="100%"> <tr> <td width="75%" align="left" style="font-family: Open Sans, Helvetica, Arial, sans-serif; font-size: 16px; font-weight: 800; line-height: 24px; padding: 10px; border-top: 3px solid #eeeeee; border-bottom: 3px solid #eeeeee;"> TOTAL </td><td width="25%" align="left" style="font-family: Open Sans, Helvetica, Arial, sans-serif; font-size: 16px; font-weight: 800; line-height: 24px; padding: 10px; border-top: 3px solid #eeeeee; border-bottom: 3px solid #eeeeee;"> Rs{}</td></tr></table> </td></tr></table><!--[if (gte mso 9)|(IE)]> </td></tr></table><![endif]--> </td></tr><tr> <td align="center" height="100%" valign="top" width="100%" style="padding: 0 35px 35px 35px; background-color: #ffffff;" bgcolor="#ffffff"><!--[if (gte mso 9)|(IE)]> <table align="center" border="0" cellspacing="0" cellpadding="0" width="600"> <tr> <td align="center" valign="top" width="600"><![endif]--> <table align="center" border="0" cellpadding="0" cellspacing="0" width="100%" style="max-width:660px;"> <tr> <td align="center" valign="top" style="font-size:0;"><!--[if (gte mso 9)|(IE)]> <table align="center" border="0" cellspacing="0" cellpadding="0" width="600"> <tr> <td align="left" valign="top" width="300"><![endif]--> <div style="display:inline-block; max-width:50%; min-width:240px; vertical-align:top; width:100%;"> </div><!--[if (gte mso 9)|(IE)]> </td><td align="left" valign="top" width="300"><![endif]--> <div style="display:inline-block; max-width:50%; min-width:240px; vertical-align:top; width:100%;"> <table align="left" border="0" cellpadding="0" cellspacing="0" width="100%" style="max-width:300px;"> <tr> <td align="left" valign="top" style="font-family: Open Sans, Helvetica, Arial, sans-serif; font-size: 16px; font-weight: 400; line-height: 24px;"> <p style="font-weight: 800;">Driver Details</p><p>Name :{}{}</p><p>Contact :{}</p></td></tr></table> </div><!--[if (gte mso 9)|(IE)]> </td></tr></table><![endif]--> </td></tr></table> </td></tr></table> </body></html>'.format(booking.cost,driver.firstName,driver.lastName,driver.phoneNumber),
                               'iit2016106@iiita.ac.in',
                               [booking.allottedUser.email],
                            )
                            msg.content_subtype = "html"
                            msg.send()
                        booking.save()
                        break
                else:
                    failure_message="No Drivers Available"
                    return redirect('http://localhost:8000/booking/bookings')
            return redirect('http://localhost:8000/booking/bookings')
        else:
            return redirect("http://localhost:8000/home/404")
