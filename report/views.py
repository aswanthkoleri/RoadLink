from django.shortcuts import render
import requests
from booking.models import Book
# Create your views here.
def index(request):
    if request.user.is_authenticated:
        bookinglist = Book.objects.filter(allottedUser = request.user,status="B")
        totdistance = 0
        totcost = 0
        for i in bookinglist:
            totdistance = totdistance + i.distance
            totcost = totcost + i.cost
        return render(request,'report/index.html',{'bookinglist':bookinglist,'totdistance':totdistance,'totcost':totcost})
    else:
        return redirect("http://localhost:8000/home/404")