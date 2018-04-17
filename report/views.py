from django.shortcuts import render,redirect
import requests
from django.http import HttpResponse
from django.core.files.storage import FileSystemStorage
from django.template.loader import render_to_string

from django.core.mail import send_mail
from django.core.mail import EmailMessage
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
        # html_string = render_to_string('report/index.html', {'bookinglist':bookinglist,'totdistance':totdistance,'totcost':totcost})

        # html = HTML(string=html_string)
        # html.write_pdf(target='/tmp/mypdf.pdf');

        # fs = FileSystemStorage('/tmp')
        # with fs.open('mypdf.pdf') as pdf:
        #     response = HttpResponse(pdf, content_type='application/pdf')
        #     response['Content-Disposition'] = 'attachment; filename="mypdf.pdf"'
        #     render(request,'report/index.html',{'bookinglist':bookinglist,'totdistance':totdistance,'totcost':totcost})
        #     return response
        return render(request,'report/index.html',{'bookinglist':bookinglist,'totdistance':totdistance,'totcost':totcost})
    else:
        return redirect("http://localhost:8000/home/404")

def change(request):
    if request.POST:
        return render(request,'booking/index.html',{'form':form})
    else:
        if request.user.is_authenticated:
            bookinglist = Book.objects.filter(allottedUser = request.user,status="B")
            totdistance = 0
            totcost = 0
            for i in bookinglist:
                totdistance = totdistance + i.distance
                totcost = totcost + i.cost
            msg = EmailMessage(
               'Your Travel Report',
               '<!DOCTYPE html><html><head> <title></title> <meta http-equiv="Content-Type" content="text/html; charset=utf-8"/> <meta name="viewport" content="width=device-width, initial-scale=1"> <meta http-equiv="X-UA-Compatible" content="IE=edge"/> <body style="margin: 0 !important; padding: 0 !important; background-color: #eeeeee;" bgcolor="#eeeeee"> <div style="display: none; font-size: 1px; color: #fefefe; line-height: 1px; font-family: Open Sans, Helvetica, Arial, sans-serif; max-height: 0px; max-width: 0px; opacity: 0; overflow: hidden;">Travel Report - RoadLink!</div><table border="0" cellpadding="0" cellspacing="0" width="100%"> <tr> <td align="center" style="background-color: #eeeeee;" bgcolor="#eeeeee"> <table align="center" border="0" cellpadding="0" cellspacing="0" width="100%" style="max-width:600px;"> <tr> <td align="center" valign="top" style="font-size:0; padding: 35px;" bgcolor="#044767"> <div style="display:inline-block; max-width:50%; min-width:100px; vertical-align:top; width:100%;"> <table align="left" border="0" cellpadding="0" cellspacing="0" width="100%" style="max-width:300px;"> <tr> <td align="left" valign="top" style="font-family: Open Sans, Helvetica, Arial, sans-serif; font-size: 36px; font-weight: 800; line-height: 48px;" class="mobile-center"> <h1 style="font-size: 36px; font-weight: 800; margin: 0; color: #ffffff;">RoadLink</h1> </td></tr></table> </div><div style="display:inline-block; max-width:50%; min-width:100px; vertical-align:top; width:100%;" class="mobile-hide"> <table align="left" border="0" cellpadding="0" cellspacing="0" width="100%" style="max-width:300px;"> <tr> <td align="right" valign="top" style="font-family: Open Sans, Helvetica, Arial, sans-serif; font-size: 48px; font-weight: 400; line-height: 48px;"> <table cellspacing="0" cellpadding="0" border="0" align="right"> <tr> <td style="font-family: Open Sans, Helvetica, Arial, sans-serif; font-size: 18px; font-weight: 400;"> <p style="font-size: 18px; font-weight: 400; margin: 0; color: #ffffff;"></p></td><td style="font-family: Open Sans, Helvetica, Arial, sans-serif; font-size: 18px; font-weight: 400; line-height: 24px;"> </td></tr></table> </td></tr></table> </div></td></tr><tr> <td align="center" style="padding: 35px 35px 20px 35px; background-color: #ffffff;" bgcolor="#ffffff"> <table align="center" border="0" cellpadding="0" cellspacing="0" width="100%" style="max-width:600px;"> <tr> <td align="center" style="font-family: Open Sans, Helvetica, Arial, sans-serif; font-size: 16px; font-weight: 400; line-height: 24px; padding-top: 25px;"> <img src="https://kingit.com.au/wp-content/uploads/2016/04/Report.gif" width="125" height="120" style="display: block; border: 0px;"/> <br><h2 style="font-size: 30px; font-weight: 800; line-height: 36px; color: #333333; margin: 0;"> Travel Report !<br><h2><h3><a href="http://localhost:8000/report">See your Report</a> </h3> </td></tr><tr> <td align="left" style="font-family: Open Sans, Helvetica, Arial, sans-serif; font-size: 16px; font-weight: 400; line-height: 24px; padding-top: 10px;"> <p style="font-size: 16px; font-weight: 400; line-height: 24px; color: #777777;"> </p></td></tr><tr> <td align="left" style="padding-top: 20px;"> </td></tr><tr> <td align="left" style="padding-top: 20px;"> <table cellspacing="0" cellpadding="0" border="0" width="100%"> <tr> <td width="75%" align="left" style="font-family: Open Sans, Helvetica, Arial, sans-serif; font-size: 16px; font-weight: 800; line-height: 24px; padding: 10px; border-top: 3px solid #eeeeee; border-bottom: 3px solid #eeeeee;"> Total Distance </td><td width="25%" align="left" style="font-family: Open Sans, Helvetica, Arial, sans-serif; font-size: 16px; font-weight: 800; line-height: 24px; padding: 10px; border-top: 3px solid #eeeeee; border-bottom: 3px solid #eeeeee;"> {} Km</td></tr><tr> <td width="75%" align="left" style="font-family: Open Sans, Helvetica, Arial, sans-serif; font-size: 16px; font-weight: 800; line-height: 24px; padding: 10px; border-top: 3px solid #eeeeee; border-bottom: 3px solid #eeeeee;"> Total Expenditure </td><td width="25%" align="left" style="font-family: Open Sans, Helvetica, Arial, sans-serif; font-size: 16px; font-weight: 800; line-height: 24px; padding: 10px; border-top: 3px solid #eeeeee; border-bottom: 3px solid #eeeeee;"> Rs {}</td></tr></table> </td></tr></table> </td></tr><tr> <td align="center" height="100%" valign="top" width="100%" style="padding: 0 35px 35px 35px; background-color: #ffffff;" bgcolor="#ffffff"> <table align="center" border="0" cellpadding="0" cellspacing="0" width="100%" style="max-width:660px;"> <tr> <td align="center" valign="top" style="font-size:0;"> <div style="display:inline-block; max-width:50%; min-width:240px; vertical-align:top; width:100%;"> </div><div style="display:inline-block; max-width:50%; min-width:240px; vertical-align:top; width:100%;"> </body></html>'.format(totdistance,totcost),
               'iit2016106@iiita.ac.in',
               [request.user.email],
            )
            msg.content_subtype = "html"
            msg.send()
            return redirect('http://localhost:8000/report')
        else:
            return redirect("http://localhost:8000/home/404")
