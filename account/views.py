from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import login,logout
from account.forms import RegistrationForm
from django.contrib.auth.models import User

def signup(request):
    if request.method=="POST":
        form=RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('account:login')
    else:
        form=RegistrationForm()
    return render(request,'account/signup.html',{'form' : form})

def loginView(request):
    if request.method == 'POST':
        form=AuthenticationForm(data=request.POST)
        if form.is_valid():
            user=form.get_user()
            login(request,user)
            return redirect('account:profile')
    else:
        form=AuthenticationForm()
    return render(request,'account/login.html',{'form': form})

def logoutView(request):
    if request.method == 'POST':
        logout(request)
        return redirect('account:login')

def profileView(request):
    if request.user.is_authenticated:
        user=request.user
        form=RegistrationForm(instance=user)
        args = { 'user' : request.user,'form' : form}
        return render(request,'account/profile.html',args)
    else:
        return redirect("http://localhost:8000/home/404")
    if request.method == "POST":
        form=RegistrationForm(request.POST,instance=user)
        if form.is_valid():
            form.save()
            return redirect('account:profile')