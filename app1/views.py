from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

@login_required(login_url='login')
def HomePage(request):
    return render(request, 'home.html')

from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages

def SignupPage(request):
    if request.method == 'POST':
        uname = request.POST.get('username')
        email = request.POST.get('email')
        pass1 = request.POST.get('password1')
        pass2 = request.POST.get('password2')

        # Check if any field is empty
        if not uname or not email or not pass1 or not pass2:
            messages.error(request, "All fields are required!")
            return render(request, 'error.html')

        # Optionally, check if passwords match
        if pass1 != pass2:
            messages.error(request, "Passwords do not match!")
            return render(request, 'error.html')

        # Now safe to create the user
        my_user = User.objects.create_user(username=uname, email=email, password=pass1)
        my_user.save()

        return redirect('login')  # Or wherever you want after signup

    return render(request, 'signup.html')


def LoginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        pass1 = request.POST.get('pass')  # Ensure the field name is 'password'
        
        user = authenticate(request, username=username, password=pass1)
        
        if user is not None:
            login(request, user)
            return redirect('home')  # Redirect to home after successful login
        else:
            return HttpResponse("Username and password are incorrect.")
        
    return render(request, 'login.html')

def LogoutPage(request):
    logout(request)
    return redirect('home')  # Redirect to home page after logout
