from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from django.http import Http404
from django.template import loader
from .models import Book
from .forms import BookForm
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
            instance.save()
            success_message='Booking done'
            form=BookForm()
            return render(request,'booking/index.html',{'form':form,'success' : success_message})
    else:
        form=BookForm()
        error_message='Something went wrong error'
        return render(request,'booking/index.html',{ 'form' : form ,'error':error_message})