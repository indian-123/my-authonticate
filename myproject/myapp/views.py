from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login , logout as auth_logout
# Create your views here.
def home(request):
    return render(request,'index.html')

def signup(request):
    if request.method == "POST":
        uname = request.POST['uname']
        uemail = request.POST['uemail']
        upass = request.POST['upass']

        user = User.objects.create_user(username=uname,email=uemail,password=upass)
        user.first_name=uname
        user.is_staff=True
        user.is_superuser=True
        user.save()
        return redirect('login')
		
    return render(request,'register.html')

def login(request):
    if request.method == 'POST':
        number = request.POST['uname']
        password = request.POST['upass']
        user = authenticate(request,username=number,password=password)
        print(user)
        if user is not None:
            auth_login(request,user)
            return redirect('home')
    return render(request,'login.html')


def logout(request):
    auth_logout(request)
    return redirect('home')