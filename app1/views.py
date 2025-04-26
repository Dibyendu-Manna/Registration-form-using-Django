from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

@login_required(login_url='login')
def HomePage(request):
    return render(request, 'home.html')

def SignupPage(request):
    if request.method == 'POST':
        print("Form submitted")
        uname = request.POST.get('username')
        email = request.POST.get('email')
        pass1 = request.POST.get('password1')
        pass2 = request.POST.get('password2')

        print(f"Username: {uname}, Email: {email}")

        if pass1 != pass2:
            return HttpResponse("Passwords do not match.")
        
        # Create the user object first
        my_user = User.objects.create_user(username=uname, email=email, password=pass1)
        my_user.save()  # Save the user after creation

        return redirect('login')  # Redirect to the login page after signup
    
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
