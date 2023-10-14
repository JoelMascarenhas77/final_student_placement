from django.shortcuts import render
from django.contrib.auth import login,logout, authenticate
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect,HttpResponse


def home(request):
    user = request.user.student
    return render(request,"student/home.html",{"user":user})

