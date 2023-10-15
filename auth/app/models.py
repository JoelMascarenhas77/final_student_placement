from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin


class MyUserManager(BaseUserManager):
    def create_user(self, username, email, password, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(username=username, email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, password):
        user = self.create_user(
            username=username,
            email=email,
            password=password
        )
        user.is_admin = True
        user.save(using=self._db)
        return user
    
class Student(models.Model):
    pid = models.IntegerField( primary_key=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    gender = models.CharField(max_length=4)
    age = models.IntegerField(default=0)
    branch = models.CharField(max_length=30)
    semester = models.CharField(max_length=2)
    division = models.CharField(max_length=1)
    address = models.CharField(max_length=30)
    hostel = models.CharField(max_length=3)
    photo = models.FileField(upload_to='profiles/')
    grade = models.CharField(max_length=30)

class MyUser(AbstractBaseUser, PermissionsMixin):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, null=True, default=None)
    username = models.CharField(max_length=30, unique=True)
    email = models.EmailField(max_length=50, unique=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)  # Use is_admin for admin access
    is_superuser = models.BooleanField(default=False)
    objects = MyUserManager()

    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ["email"]

    def __str__(self):
        return self.username
    
class Result(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    cgpa = models.DecimalField(max_digits=4, decimal_places=2)
    sem = models.IntegerField()
    backlog = models.IntegerField()

    @classmethod
    def create_result(cls, student_pid, cgpa, backlog):
        student = Student.objects.get(pid=student_pid)
        sem = student.semester 

        result = cls(
            student=student,
            cgpa=cgpa,
            sem=sem,
            backlog=backlog
        )
        result.save()

class Prediction(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    age = models.IntegerField()
    gender = models.IntegerField()  # 1 for male, 0 for female
    stream = models.IntegerField()  # 1 for Civil, 2 for IT, 3 for Electrical, etc.
    cgpa = models.DecimalField(max_digits=4, decimal_places=2)  
    hostel = models.BooleanField()  # 0 for no, 1 for yes
    backlogs = models.IntegerField()
    results = models.IntegerField()

    @classmethod
    def create_prediction(cls, student):
        results = Result.objects.filter(student=student)
        student_info = student

        avg_cgpa = results.aggregate(avg_cgpa=models.Avg('cgpa'))['avg_cgpa']
        sum_backlogs = results.aggregate(sum_backlogs=models.Sum('backlog'))['sum_backlogs']

        # Create a Prediction instance
        prediction = cls(
            student=student,
            age=student_info.age,
            gender=1 if student_info.gender == 'Male' else 0,
            stream={
                'Civil': 1,
                'Information Technology': 2,
                'Electrical': 3,
                'Electronics And Communication': 4,
                'Mechanical': 5,
                'Computer Science': 6,
            }[student_info.branch],
            cgpa=avg_cgpa,
            hostel=1 if student_info.hostel == 'Yes' else 0,
            backlogs=sum_backlogs,
            results=0
        )
        prediction.save()

class CourseInternship(models.Model):
    name = models.CharField(max_length=30)
    company = models.CharField(max_length=30)
    level = models.CharField(max_length=30)
    duration = models.CharField(max_length=30)
    domain = models.CharField(max_length=30)
    students_enrolled = models.IntegerField(default=0)

class Company(models.Model):
    name = models.CharField(max_length=30)
    city = models.CharField(max_length=30)
    positions = models.CharField(max_length=30)
    salary = models.IntegerField(default=0)
    students_allotted = models.IntegerField(default=0)

class Feedback(models.Model):
    info = models.ForeignKey(MyUser, on_delete=models.CASCADE, null=True, default=None)
    feedback = models.CharField(max_length=200)
    reply = models.CharField(max_length=200)
    created_at = models.DateField(max_length=30)
    updated_at = models.DateField(default=0)

class Internship(models.Model):
    internship = models.FileField(upload_to="internships")
    key = models.ForeignKey(Student, on_delete=models.CASCADE, null=True, default=None)

class Report(models.Model):
    report = models.FileField(upload_to="reports")  # Corrected field name
    key = models.ForeignKey(Student, on_delete=models.CASCADE, null=True, default=None)

class Certificate(models.Model):  
    certificate = models.FileField(upload_to="certificates")
    key = models.ForeignKey(Student, on_delete=models.CASCADE, null=True, default=None)

class Placement(models.Model):
    pid = models.ForeignKey(Student, on_delete=models.CASCADE)
    company_name = models.CharField(max_length=100)
    salary = models.IntegerField()
    position = models.CharField(max_length=100)
    PLACEMENT_TYPES = (
        ('incampus', 'In Campus Placement'),
        ('outside', 'Outside Placement'),
    )
    placement_type = models.CharField(max_length=10, choices=PLACEMENT_TYPES, default='incampus')
