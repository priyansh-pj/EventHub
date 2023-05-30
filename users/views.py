from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login, logout
from django.contrib import messages
from django.contrib.auth.models import User
def login(request):
    if request.user.is_authenticated:
        return redirect('Event_List')
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request,'Username does not exist')
        user = authenticate(request, username=username, password=password)
        if user != None:
            auth_login(request, user)
            return redirect('Event_List')
        else:
            return redirect('login')


    return render(request, 'user/login.html')

from django.contrib.auth.decorators import login_required
@login_required(login_url='login')
def sign_out(request):
    logout(request)
    return redirect('login')