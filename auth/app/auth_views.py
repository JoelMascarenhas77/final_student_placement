from django.shortcuts import render
from django.contrib.auth import login,logout, authenticate
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect,HttpResponse
from django.contrib.auth import get_user_model
from django.core.mail import EmailMessage
from . import helpfun
from django.http import HttpResponse
import datetime


User = get_user_model()


def user_login(request):
    if request.method == "POST":
        username =request.POST['username']
        password = request.POST['password']
        myuser = authenticate(request, username=username, password=password)
        if myuser is not None:
            login(request,myuser)
            if myuser.is_admin==True:    
                return HttpResponseRedirect('admin_home/')
            else:
                 return HttpResponseRedirect('student_home/')
            
    return render(request,"login.html")


def user_logout(requset):
    logout(requset)
    return HttpResponseRedirect('/')



def reset_password(request):
    if request.method == "POST":
        usermail =request.POST['email']
        otp = helpfun.otp(5)
        email = EmailMessage('Student password reset',  opt , to=[usermail])
        email.send()

        otp = helpfun.hash(otp)
        response = render(request,"reset.html")
        response.set_cookie('my_cookie_name', 'cookie_value', expires=datetime.datetime.now() + datetime.timedelta(days=30), path='/')
        
        
    return render(request,"reset.html")


def set_cookie_view(request):
    response = HttpResponse("Cookie set successfully!")
    response.set_cookie('my_cookie_name', 'cookie_value', expires=datetime.datetime.now() + datetime.timedelta(days=30), path='/')
    return response



