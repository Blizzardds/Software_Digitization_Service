from django.contrib import messages
from django.contrib.auth import authenticate
from django.contrib.auth.models import auth
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import User
from dds.decorators import unauthenticated_user, allowed_users


# To Verify the user and let login to the web app.
@unauthenticated_user
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(request, username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('ddsHome')
        else:
            messages.info(request, 'Invalid username or password')
            return redirect('/')
    else:
        return render(request, 'login.html')


# To Logout the user fom web app
def logout(request):
    auth.logout(request)
    return redirect('login')

# To shows the information of user profile.
@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def profile(request):
    return render(request, 'profile.html')
