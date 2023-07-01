from django.shortcuts import render
from .models import *

# Create your views here.
def indexpage(request):
    return render(request,'index.html') 

def Userregister(request):
    if request.method=="POST":
        fname=request.POST['fname']
        lname=request.POST['lname']
        mail=request.POST['mail']
        phone=request.POST['phone']
        password=request.POST['password']
        cpassword=request.POST['cpassword']

    #First we will validate that user already exit
    users=user.objects.filter(Email=mail)

    if users:
        message="User Already Register"
        return render(request,"login.html",{'msg':message})
    else:
        if password == cpassword:
            newuser=user.objects.create(Firstname=fname,Lastname=lname,Email=mail,Contact=phone,Password=password)
            message="User Successfully Registered"
            return render(request,"login.html",{'msg':message})
        else:
            message="Password and Comfirm Password doesn't match"
            return render(request,"index.html",{'msg':message})
        
def Loginpage(request):
    return render(request,"login.html")

def Loginuser(request):
    if request.method=="POST":
        mail=request.POST['mail']
        password=request.POST['password']

        users=user.objects.filter(Email=mail)
        if users:

            users=user.objects.get(Email=mail)

            if users:
                if users.Password==password:
                    request.session['Firstname']=users.Firstname
                    request.session['Lastname']=users.Lastname
                    request.session['Email']=users.Email
                    request.session['Contact']=users.Contact
                    message="Successfully Login"
                    return render(request,"home.html",{'msg':message})
                else:
                    message="Password doesn't match"
                    return render(request,"login.html",{'msg':message})
        else:
            message="User Does not Exist"
            return render(request,"login.html",{'msg':message})










