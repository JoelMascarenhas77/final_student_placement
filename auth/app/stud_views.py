from django.shortcuts import render, redirect
from .forms import CertificateForm,ReportForm
from django.contrib.auth import login,logout, authenticate
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect,HttpResponse,JsonResponse
from datetime import datetime, date, time, timedelta
from .models import Feedback,Student,Certificate,Report,StudentCourseInternship,CourseInternship,Prediction
from django.shortcuts import render, redirect
from .forms import CertificateForm, ReportForm
from django.contrib.auth import get_user_model
from django.contrib import messages
User = get_user_model()


def home(request):
    user = request.user.student
    certifications = Certificate.objects.filter(key=user).count()
    recCourse = StudentCourseInternship.objects.filter(key=user).count()
    try:
        prediction = Prediction.objects.get(student=user)
        results = prediction.results
    except Prediction.DoesNotExist:
        results = None
    context = {
        "certifications" : certifications,
        "results": results,
        "user" : user,
        "recCourse" : recCourse,

    }

    return render(request,"student/home.html",context)
 
def prediction(request):
    user = request.user.student
    prediction = Prediction.objects.get(student=user)
    results = prediction.results
    return render(request,"student/prediction.html",{"user":user,"results":results})

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

    previous_applications = StudentCourseInternship.objects.filter(key=student)
    previous_domains = [app.domain for app in previous_applications]

    if previous_domains:
        recommended_courses = CourseInternship.objects.filter(domain__in=previous_domains).exclude(id__in=previous_applications).order_by('?')[:10]
    else:
        recommended_courses = CourseInternship.objects.order_by('?')[:10]

    for course in recommended_courses:
        student_course, created = StudentCourseInternship.objects.get_or_create(
            name=course.name,
            company=course.company,
            level=course.level,
            duration=course.duration,
            domain=course.domain,
            applied=False,
            key=student
        )

    context = {'recommended_courses': recommended_courses}
    return render(request, 'student/manage_courses.html', context)

def apply_course(request):
    if request.method == "POST" and request.is_ajax():
        course_id = request.POST.get("name")
        student = request.user.student

        try:
            course = StudentCourseInternship.objects.get(id=course_id, key=student)
        except StudentCourseInternship.DoesNotExist:
            course = None

        if course:
            course.applied = not course.applied
            course.save()

            if course.applied:
                message = 'You have successfully applied for the course.'
            else:
                message = 'You have unapplied for the course.'
            return JsonResponse({'success': True, 'message': message})

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