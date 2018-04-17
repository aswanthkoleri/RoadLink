from django.shortcuts import render
import requests
from django.http import HttpResponse
from django.core.files.storage import FileSystemStorage
from django.template.loader import render_to_string

from weasyprint import HTML
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
        html_string = render_to_string('report/index.html', {'bookinglist':bookinglist,'totdistance':totdistance,'totcost':totcost})

        html = HTML(string=html_string)
        html.write_pdf(target='/tmp/mypdf.pdf');

        fs = FileSystemStorage('/tmp')
        with fs.open('mypdf.pdf') as pdf:
            response = HttpResponse(pdf, content_type='application/pdf')
            response['Content-Disposition'] = 'attachment; filename="mypdf.pdf"'
            render(request,'report/index.html',{'bookinglist':bookinglist,'totdistance':totdistance,'totcost':totcost})
            return response
        return render(request,'report/index.html',{'bookinglist':bookinglist,'totdistance':totdistance,'totcost':totcost})
    else:
        return redirect("http://localhost:8000/home/404")