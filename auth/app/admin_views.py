from django.shortcuts import render
from django.contrib import messages
from django.contrib.auth import get_user_model
from .forms import  AddStudentForm
from .models import *
from django.http import HttpResponseRedirect,HttpResponse
from . import helpfun


User = get_user_model()

def home(request):
    return render(request,"admin/home.html")


def add_student(request):
    stud_form  =  AddStudentForm()
    if request.method =='POST':
        photo =request.FILES['photo']
        
        stud_data=['first_name','last_name',
            'age','gender','address','branch','semester','division']
        
        user_data=['username','password','email']

        U_data = helpfun.getdata(request,user_data)
        S_data = helpfun.getdata(request,stud_data)

        new_studnent_info = student(photo=photo,first_name=S_data[0] ,
                                    last_name=S_data[1],age=S_data[2],gender=S_data[3],
                                    address=S_data[4],branch=S_data[5],
                                    semester=S_data[6],divison=S_data[7]) 
        new_studnent_info.save()
        new_student = User.objects.create_user(key=new_studnent_info,username =U_data[0],password =U_data[1] ,email=U_data[2])
        new_student.save()
    return render(request,"admin/add_student.html",{"form":stud_form})
    
def save_student(request):
    if request.method =="GET":
        return HttpResponse("<h1> fail <h1>")
    
def edit_studen(request):   
    users = User.objects.filter()

def edit_student(request): 
 pass

    
