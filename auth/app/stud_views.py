from django.shortcuts import render
from django.contrib.auth import login,logout, authenticate
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect,HttpResponse
from datetime import datetime
from .models import Feedback,Student,Internship,Certificate,Report
from django.contrib.auth import get_user_model
User = get_user_model()


def home(request):
    user = request.user.student
  

    return render(request,"student/home.html",{"user":user})
 
def prediction(request):
    user = request.user.student
    return render(request,"student/prediction.html",{"user":user})

def feedback(request):
    
    
    
    feedbacks=Feedback.objects.filter(Student_id=request.user.id)
    if request.method == "POST":
        the_user = User.objects.get(id   = request.user.id)

        the_user.save()
        feedback_message= request.POST['feedback_message']
        feedback = Feedback( feedback=feedback_message, created_at= datetime.now(),Student = the_user)
        feedback.save()
       


    return render(request,"student/feedback.html",{"feedbacks": feedbacks})

    
def add_certificates(request):
    if request.method =="POST":
        pid = Student.objects.get(pid=request.user.student.pid)
        for file in request.FILES.getlist('internships'):
            if file is not None:
                internship= Internship(file=file,key=pid)
                internship.save()
        for file in request.FILES.getlist('reports'):
            if file is not None:
                report= Report(file=file,key=pid)
                report.save()
        for file in request.FILES.getlist('certificates'):
                certificate= Certificate(file=file,key=pid)
                certificate.save()



       
    return render(request,"student/add_certificates.html")


