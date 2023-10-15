from django.shortcuts import render,redirect
from django.contrib.auth import login,logout, authenticate
from django.http import HttpResponseRedirect,HttpResponse
from django.core.mail import EmailMessage
from django.contrib import messages
from datetime import datetime, timedelta
from . import helpfun
from django.contrib.auth import get_user_model
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
    
    print(request.method)
    if request.method == "POST":
        if 'email-form' in request.POST:
            email=request.POST['email']
            try:
                user = User.objects.get(email = email)
            except:
                messages.error(request,"user does not exist")
                return render(request,"reset.html",{"val":"0"})
            otp = str(helpfun.otp(5))
            try:
                email = EmailMessage('Student password reset', otp , to=[email])
                email.send()
            except: 
                messages.error(request,"email could not be sent")
                return render(request,"reset.html",{"val":"0"})

             
            response = render(request,"reset.html",{"val":"1"})
            expiration_time = datetime.now() + timedelta(minutes=10)
            response.set_cookie('otp', helpfun.hash(otp), expires=expiration_time)
            response.set_cookie('email', email, expires=expiration_time)
            return response
        
        if 'otp-form' in request.POST:
            
            otp=request.POST['otp']
            sentotp = request.COOKIES.get('otp')
            if helpfun.hash(otp) == sentotp:
                return render(request,"password.html")
            
            messages.error(request,"wrong otp")
            return render(request,"reset.html",{"val":"1"})
        
        if 'password-form' in request.POST:

            password = request.POST['confirm_password']
            email = request.COOKIES.get(email)
            user = User.objects.get(email = email)
            user.set_password(password)
            return redirect('login')
        
    return render(request,"reset.html",{"val":"0"})


def new_password(request):
    return HttpResponse()