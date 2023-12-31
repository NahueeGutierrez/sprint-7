from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm


# Create your views here.

def registro(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user=form.save()
            login(request, user)
            return redirect('home')
    else:
        form=UserCreationForm()
    return render(request, 'login/registro.html',{'form':form})

def user_login(request):
    if request.method == 'POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(request, username=username, password=password)
        if user:
            login(request,user)
            return redirect('home')
    return render(request,'login/login.html')

def user_logout(request):
    logout(request)
    return redirect('home')

