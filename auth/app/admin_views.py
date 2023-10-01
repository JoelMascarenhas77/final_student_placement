from django.shortcuts import render
from django.contrib import messages
from django.contrib.auth import get_user_model
from .forms import  AddStudentForm
from .models import *
from django.http import HttpResponseRedirect,HttpResponse



User = get_user_model()

def home(request):
    return render(request,"admin/home.html")


def add_student(request):
    stud_form  =  AddStudentForm()
    if request.method =='POST':

            photo = request.FILES['photo']
            username=request.POST["username"]
            password=request.POST["password"]
            email=request.POST["email"]
            first_name=request.POST["first_name"]
            last_name=request.POST["last_name"]
            age=request.POST["age"]
            gender=request.POST["gender"]
            address=request.POST["address"]
            branch=request.POST["branch"]
            semester=request.POST["semester"]
            division=request.POST["division"]


            new_studnent_info = student_info(photo=photo,first_name=first_name ,last_name=last_name,age=age,gender=gender,address=address,branch=branch,semester=semester,divison=division) 
            new_studnent_info.save()
            new_student = User.objects.create_user(username =username,key =new_studnent_info,password =password ,email=email)
            new_student.save()
    
    return render(request,"admin/add_student.html",{"form":stud_form})
    
def save_student(request):
    if request.method =="GET":
        return HttpResponse("<h1> fail <h1>")
    
