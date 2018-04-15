from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from django.http import Http404
from django.template import loader

# Create your views here.
def index(request):
    return render(request,'home/index.html')

def notfound(request):
	return render(request,'home/404.html')