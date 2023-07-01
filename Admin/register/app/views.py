from django.shortcuts import render
from django.contrib.auth.models import User,auth

# Create your views here.
def indexpage(request):
    return render(request,'index.html') 

def Userregister(request):
    if request.method=="POST":
        fname=request.POST['fname']
        lname=request.POST['lname']
        mail=request.POST['mail']
        uname=request.POST['uname']
        password=request.POST['password']
        cpassword=request.POST['cpassword']

    #First we will validate that user already exit
    user=User.objects.filter(email=mail)

    if user:
        message="User Already Register"
        return render(request,"login.html",{'msg':message})
    else:
        if password == cpassword:
            newuser=User.objects.create_user(first_name=fname,last_name=lname,email=mail,password=password,username=uname)
            newuser.save()
            message="User Successfully Registered"
            return render(request,"login.html",{'msg':message})
        else:
            message="Password and Comfirm Password doesn't match"
            return render(request,"index.html",{'msg':message})
        
def Loginpage(request):
    return render(request,"login.html")

def Loginuser(request):
    if request.method=="POST":
        uname=request.POST['uname']
        password=request.POST['password']

        user=auth.authenticate(username=uname,password=password)
        if user is not None:
            auth.login(request,user)
            message="Successfully Login"
            return render(request,'home.html',{'msg':message, 'user':user})
        else:
            message="Mail or Password is Wrong"
            return render(request,"login.html",{'msg':message})

def Home(request):
    return render(request,"home.html")

def Logout(request):
    auth.logout(request)
    message="Successfully LogOut"
    return render(request,"login.html",{'msg':message})










