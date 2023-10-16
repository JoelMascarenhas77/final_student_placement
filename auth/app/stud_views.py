from django.shortcuts import render
from django.contrib.auth import login,logout, authenticate
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect,HttpResponse
from datetime import datetime, date, time, timedelta
from .models import Feedback
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
        print(request.user.id)
        print(the_user)
        print(request.user)
        the_user.save()
        feedback_message= request.POST['feedback_message']
        feedback = Feedback( feedback=feedback_message, created_at= datetime.now(),Student_id = the_user)
        feedback.save()
       


    return render(request,"student/feedback.html",{"feedbacks": feedbacks})

    
