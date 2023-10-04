from django.shortcuts import render
from django.contrib.auth import login,logout, authenticate
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect,HttpResponse
from django.contrib.auth import get_user_model
from django.core.mail import EmailMessage


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

        email = EmailMessage('Student password reset', 'Body', to=[usermail])
        email.send()
    

    return render(request,"reset.html")





