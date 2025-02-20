from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.shortcuts import redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
@login_required(login_url='login')
# Create your views here.

def HomePage(request):
    return render(request,'home.html')
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
        

        else:
            my_user.save()
            return redirect('login')
            my_user = User.objects.create_user(uname, email, pass1)
    return render(request,'signup.html')


def LoginPage(request):
    if request.method=='POST':
        username=request.POST.get('username')
        pass1=request.POST.get('pass')
        user=authenticate(request,username=username,password=pass1)
        if user is not None:
            login(request,user)
            return redirect('home')
        
        else:
            return HttpResponse("username and password is incorrect")
        
    return render (request,'login.html')
def LogoutPage(request):
        logout(request)
        return redirect('home')

