from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth import get_user_model
from .forms import AddStudentForm
from .models import *
from django.db.models import Avg, Sum
from . import helpfun
import pandas as pd
import pickle,joblib
from django.conf import settings
from django.http import HttpResponse

User = get_user_model()

def home(request):
    students_count = Student.objects.all().count()
    company_count=   Company.objects.all().count()
    course_count = CourseInternship.objects.all().count()
    courses = ["mechanical","civil","electronics"]
  
    context={
        "student_count": students_count ,
        "company_count": company_count,
        "course_count": course_count,
    }
    return render(request, "admin/home.html",context)
    

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
    students = Student.objects.all() 
    return render(request, "admin/manage.html", {"students": students})
import pandas as pd

def add_company_file(request):
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

                # Remove commas from the 'salary' column
                df['students'] = df['students'].astype(str).str.replace(',', '', regex=True).astype(int)
                df['salary'] = df['salary'].str.replace(',', '').astype(int)

                for _, row in df.iterrows():
                    company_data = {
                        'id': row['id'],
                        'name': row['name'],
                        'city': row['city'],
                        'position': row['position'],
                        'salary': int(row['salary']),
                        'students': int(row['students']),
                    }

                    new_company_info = Company(
                        id=company_data['id'], name=company_data['name'],
                        city=company_data['city'], positions=company_data['position'], salary=company_data['salary'],
                        students_allotted=company_data['students']
                    )
                    new_company_info.save()
                messages.success(request, "Company records added successfully from the file.")
            except Exception as e:
                messages.error(request, f"An error occurred while processing the file: {str(e)}")

    return redirect('manage_company')



def manage_company(request):
    companies = Company.objects.all()
    return render(request, "admin/manage_company.html", {"companies": companies})

def add_course_file(request):
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
                    return redirect('manage_course')

                # Remove commas from the 'students_enrolled' column
                df['students_enrolled'] = df['students_enrolled'].astype(str).str.replace(',', '', regex=True).astype(int)


                for _, row in df.iterrows():
                    course_data = {
                        'name': row['name'],
                        'company': row['company'],
                        'level': row['level'],
                        'duration': row['duration'],
                        'domain': row['domain'],
                        'students_enrolled': int(row['students_enrolled']),
                    }

                    new_course_info = CourseInternship(
                        name=course_data['name'],
                        company=course_data['company'],
                        level=course_data['level'],
                        duration=course_data['duration'],
                        domain=course_data['domain'],
                        students_enrolled=course_data['students_enrolled'],
                    )
                    new_course_info.save()
                messages.success(request, "Course records added successfully from the file.")
            except Exception as e:
                messages.error(request, f"An error occurred while processing the file: {str(e)}")

    return redirect('manage_course')


def manage_course(request):
    course = CourseInternship.objects.all()
    return render(request, "admin/manage_course.html", {"course": course})

def delete_student(request, student_pid):
    if request.method == 'POST':
        student = get_object_or_404(Student, pid=student_pid)
    
        user = User.objects.filter(student=student)
        if user.exists():
            user.delete()
        student.delete()
        messages.success(request, "Student record and associated login deleted successfully.")
    
    return redirect('manage_student')

def edit_student(request, student_id):
    pass


from django.contrib import messages
from django.shortcuts import render, redirect
from .models import Student, Report, Prediction
import joblib
from django.conf import settings

from django.contrib import messages
from django.shortcuts import render, redirect
from .models import Student, Report, Prediction, Certificate
import joblib
from django.conf import settings
from django.db.models import Avg, Sum, Count  # Import the necessary functions

from django.contrib import messages
from django.shortcuts import render, redirect
from .models import Student, Report, Prediction, Certificate
import joblib
from django.conf import settings
from django.db.models import Avg, Sum, Count  # Import the necessary functions

def update_prediction(request):
    # Load the machine learning model (replace 'your_model.pkl' with the actual model file)
    model = joblib.load(settings.MODEL_PATH)

    try:
        # Get all students from the database
        students = Student.objects.all()
        Prediction.objects.filter(student__in=students).delete()

        # Map gender, stream, and hostel to numerical values
        gender_mapping = {'Female': 0, 'Male': 1}
        stream_mapping = {
            'Civil': 1,
            'Information Technology': 2,
            'Electrical': 3,
            'Electronics And Communication': 4,
            'Mechanical': 5,
            'Computer Science': 6,
        }
        hostel_mapping = {'No': 0, 'Yes': 1}

        # Create a list to store prediction results
        prediction_results = []

        for student in students:
            report = Report.objects.filter(key=student)

            # Prepare the input data for prediction
            age = student.age
            gender = gender_mapping.get(student.gender, 0)
            stream = stream_mapping.get(student.branch, 0)
            
            # Calculate the average CGPA and sum of backlogs for the student
            cgpa = report.aggregate(Avg('cgpa'))['cgpa__avg']
            backlog = report.aggregate(Sum('backlogs'))['backlogs__sum']

            # Calculate the count of certificates for the student
            internship = Certificate.objects.filter(key=student).aggregate(Count('id'))['id__count']

            hostel = hostel_mapping.get(student.hostel, 0)

            # Perform the prediction
            prediction_result = model.predict([[age, gender, stream, cgpa, backlog, internship, hostel]])

            # Save the prediction result to the "Prediction" table
            prediction = Prediction.objects.create(
                student=student,
                age=age,
                gender=gender,
                stream=stream,
                cgpa=cgpa,
                backlogs=backlog,
                hostel=hostel,
                internship=internship,
                results=prediction_result[0]  # Assuming the model returns a single result
            )
            prediction_results.append(prediction)

        # Retrieve the predictions to pass to the template
        predictions = Prediction.objects.all()

        # Set a success message
        messages.success(request, "Predictions updated for all students.")

    except Student.DoesNotExist:
        messages.error(request, "Student not found.")

    # Pass predictions to the template context
    context = {
        'predictions': predictions
    }

    return render(request, 'admin/prediction.html', context)



def feedback(request):
    feedbacks = Feedback.objects.all()
    if request.method == "POST":
        id =request.POST['id']
        reply= request.POST['reply']
        feedback = Feedback.objects.get(id = id)
        feedback.reply = reply
        feedback.save()
        return HttpResponse("True")
    return render(request,"admin/feedback.html",{"feedbacks":feedbacks})


def add_placement_file(request):
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
                    return redirect('manage_placement')

                # Ensure 'salary' is read as a string, replace commas, and convert to integer
                df['salary'] = df['salary'].astype(str).str.replace(',', '', regex=True).astype(int)

                for _, row in df.iterrows():
                    placement_data = {
                        'pid': row['pid'],
                        'company_name': row['company_name'],
                        'position': row['position'],
                        'salary': row['salary'],
                        'placement_type': row['placement_type'],  # Include placement_type
                    }

                    new_placement = Placement(
                        pid_id=placement_data['pid'],
                        company_name=placement_data['company_name'],
                        position=placement_data['position'],
                        salary=placement_data['salary'],
                        placement_type=placement_data['placement_type'],  # Assign placement_type
                    )
                    new_placement.save()
                messages.success(request, "Placement records added successfully from the file.")
            except Exception as e:
                messages.error(request, f"An error occurred while processing the file: {str(e)}")

    return redirect('manage_placement')


def manage_placement(request):
    placements = Placement.objects.all()
    for placement in placements:
        placement.student_name = placement.pid.first_name + " " + placement.pid.last_name # Assuming "name" is the field in the Student model you want to display

    return render(request, "admin/manage_placement.html", {"placements": placements})

