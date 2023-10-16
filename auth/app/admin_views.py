from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth import get_user_model
from .forms import AddStudentForm
from .models import *
from . import helpfun
import pandas as pd
import pickle
from .models import Feedback

User = get_user_model()

def home(request):
    return render(request, "admin/home.html")

def add_student(request):
    stud_form = AddStudentForm()
    if request.method == 'POST':
        photo = request.FILES['photo']

        stud_data = ['pid', 'first_name', 'last_name', 'age', 'gender', 'hostel', 'address', 'branch', 'semester', 'division']
        user_data = ['username', 'password', 'email']

        U_data = helpfun.getdata(request, user_data)
        S_data = helpfun.getdata(request, stud_data)

        new_student_info = Student(
            pid=S_data[0], photo=photo, first_name=S_data[1],
            last_name=S_data[2], age=S_data[3], gender=S_data[4],
            hostel=S_data[5], address=S_data[6], branch=S_data[7],
            semester=S_data[8], division=S_data[9]
        )
        new_student_info.save()
        new_student = User.objects.create_user(username=U_data[0], password=U_data[1], email=U_data[2], student=new_student_info)
        new_student.save()
    return render(request, "admin/add_student.html", {"form": stud_form})

def add_student_file(request):
    if request.method == 'POST':
        file_upload = request.FILES.get('file_upload')

        if file_upload:
            try:
                if file_upload.name.endswith('.csv'):
                    df = pd.read_csv(file_upload)
                elif file_upload.name.endswith(('.xls', '.xlsx')):
                    df = pd.read_excel(file_upload)
                else:
                    messages.error(request, "Unsupported file format.")
                    return redirect('manage_student')

                for _, row in df.iterrows():
                    student_data = {
                        'pid': row['pid'],
                        'first_name': row['first_name'],
                        'last_name': row['last_name'],
                        'age': row['age'],
                        'gender': row['gender'],
                        'hostel': row['hostel'],
                        'address': row['address'],
                        'branch': row['branch'],
                        'semester': row['semester'],
                        'division': row['division'],
                    }

                    # Extract 'username', 'password', and 'email' directly from the row
                    username = row['username']
                    password = str(row['password'])
                    email = row['email']

                    new_student_info = Student(
                        pid=student_data['pid'], first_name=student_data['first_name'],
                        last_name=student_data['last_name'], age=student_data['age'], gender=student_data['gender'],
                        hostel=student_data['hostel'], address=student_data['address'], branch=student_data['branch'],
                        semester=student_data['semester'], division=student_data['division']
                    )
                    new_student_info.save()
                    new_student = User.objects.create_user(username=username, password=password, email=email, student=new_student_info)

                    new_student.save()
                messages.success(request, "Student records and users added successfully from the file.")
            except Exception as e:
                messages.error(request, f"An error occurred while processing the file: {str(e)}")

    return redirect('manage_student')

def manage_student(request):
    users = User.objects.filter(is_admin=False)
    return render(request, "admin/manage.html", {"users": users})

def delete_student(request, student_pid):
    if request.method == 'POST':
        student = get_object_or_404(Student, pid=student_pid)
        
        # Delete the associated login record in MyUser model
        user = User.objects.filter(student=student)
        if user.exists():
            user.delete()
        
        # Delete the student record
        student.delete()
        
        # Add a success message
        messages.success(request, "Student record and associated login deleted successfully.")
    
    return redirect('manage_student')

def edit_student(request, student_id):
    pass

def prediction(request):
   ''' with open('model.pkl', 'rb') as model_file:
        model = pickle.load(model_file)

    if request.method == 'POST' and 'prediction' in request.POST:
        predictions = Prediction.objects.all()

        for prediction in predictions:
            features = [
                prediction.age,
                prediction.gender,
                prediction.stream,
                prediction.cgpa,
                prediction.hostel,
                prediction.backlogs,
            ]

            try:
                predicted_result = model.predict([features])[0]
                prediction.results = predicted_result
                prediction.save()
            except Exception as e:
                messages.error(request, f"An error occurred during prediction: {str(e)}")

        return redirect('prediction')

    predictions = Prediction.objects.all()

    return render(request, 'admin/prediction.html', {'predictions': predictions})'''
   return render(request, 'admin/prediction.html')


def feedback(request):
    feedbacks = Feedback.objects.all()
    if request.method == "POST":
        id =request.POST['id']
        reply= request.POST['reply']
        feedback = Feedback.objects.get(id = id)
        feedback.reply = reply
    return render(request,"admin/feedback.html",{"feedbacks":feedbacks})