from django.shortcuts import render,redirect
from django.http.response import HttpResponse
from django.contrib.auth.models import auth,User

# Create your views here.
def index(request):
    return render(request,"index.html")


def login(request):
    if request.method=="POST":
        usr=request.POST["uname"]
        pwd=request.POST["pwrd"]
        user=auth.authenticate(username=usr,password=pwd)
        if user is not None:
            auth.login(request,user)
            msg="Login successful"
            return redirect("/")
        else:
            msg="Invalid username and password"
            return render(request,"login.html",{"message":msg})
        
    else:
        return render(request,"login.html")
    

def register(request):
    if request.method=="POST":
        ftname=request.POST["fname"]
        ltname=request.POST["lname"]
        usr=request.POST["uname"]
        mail=request.POST["email"]
        pwd=request.POST["pswd"]
        rpwd=request.POST["repswd"]
        if pwd==rpwd:
            if User.objects.filter(username=usr).exists():
                msg="Username already taken"
            elif User.objects.filter(email=mail).exists():
                msg="Email already taken"
            else:
                User.objects.create_user(username=usr,first_name=ftname,last_name=ltname,email=mail,password=pwd)
                User.save();
                msg="Registration Successful"
                return redirect("/")
        else:
            msg="Invalid password"       
            return render(request,"register.html",{"message":msg})
    else:                           
        return render(request,"register.html")
    
def logout(request):
    auth.logout(request)
    return redirect("/")


    
