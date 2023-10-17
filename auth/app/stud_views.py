from django.shortcuts import render, redirect
from .forms import CertificateForm,ReportForm
from django.contrib.auth import login,logout, authenticate
from django.contrib.auth.decorators import login_required
<<<<<<< HEAD
from django.http import HttpResponseRedirect,HttpResponse
from datetime import datetime
from .models import Feedback,Student,Internship,Certificate,Report
=======
from django.http import HttpResponseRedirect,HttpResponse,JsonResponse
from datetime import datetime, date, time, timedelta
from .models import Feedback,Student,Certificate,Report,StudentCourseInternship,CourseInternship
from django.shortcuts import render, redirect
from .forms import CertificateForm, ReportForm
>>>>>>> 1361f3561a7a2b26fc3880f55346c2e0fb980f15
from django.contrib.auth import get_user_model
from django.contrib import messages
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


def add_certificates_and_reports(request):
    if request.method == "POST":
        certificate_form = CertificateForm(request.POST, request.FILES)
        report_form = ReportForm(request.POST, request.FILES)

        if "certificate_submit" in request.POST:
            if certificate_form.is_valid():
                domain = certificate_form.cleaned_data['domain']
                certificates = certificate_form.cleaned_data['certificates']
                
                # Save the certificate data to the database
                certificate_instance = Certificate(domain=domain, file=certificates)
                certificate_instance.key = request.user.student
                certificate_instance.save()
                
                # Add a success message
                messages.success(request, 'Certificate uploaded successfully')
                
        elif "report_submit" in request.POST:
            if report_form.is_valid():
                cgpa = report_form.cleaned_data['cgpa']
                backlogs = report_form.cleaned_data['backlogs']
                report = report_form.cleaned_data['reports']
                
                # Save the report data to the database
                report_instance = Report(cgpa=cgpa, backlogs=backlogs, file=report)
                report_instance.key = request.user.student
                report_instance.save()
                
                # Add a success message
                messages.success(request, 'Report uploaded successfully')
    
    else:
        certificate_form = CertificateForm()
        report_form = ReportForm()

    return render(request, 'student/add_certificates.html', {'certificate_form': certificate_form, 'report_form': report_form})

import random

def manage_courses(request):
    student = request.user.student

    # Get domains for courses the student has applied for before.
    previous_applications = StudentCourseInternship.objects.filter(key=student)
    previous_domains = [app.domain for app in previous_applications]

    # If the student has previous applications, recommend courses with matching domains.
    if previous_domains:
        recommended_courses = CourseInternship.objects.filter(domain__in=previous_domains).exclude(id__in=previous_applications).order_by('?')[:10]
    else:
        # If there are no previous applications, recommend random courses.
        recommended_courses = CourseInternship.objects.order_by('?')[:10]

    context = {'recommended_courses': recommended_courses}
    return render(request, 'student/manage_courses.html', context)

def apply_course(request):
    if request.method == "POST" and request.is_ajax():
        course_id = request.POST.get("course_id")
        student = request.user.student

        # Check if the student hasn't already applied for this course.
        if not StudentCourseInternship.objects.filter(key=student, id=course_id).exists():
            # Mark the course as applied for the student.
            student_course = StudentCourseInternship.objects.create(key=student, id=course_id, applied=True)
            student_course.save()
            return JsonResponse({'success': True})

    return JsonResponse({'success': False})

def update_profile_picture(request):
    if request.method == "POST":
        student_id = request.user.student.pid  # Get the student's ID
        student = Student.objects.get(pid=student_id)
        profile_picture = request.FILES.get('profile_picture')

        if profile_picture:
            student.photo = profile_picture
            student.save()
            messages.success(request, 'Profile picture updated successfully.')
        else:
            messages.error(request, 'Error updating profile picture. Please try again.')

    return redirect('update_profile_picture')