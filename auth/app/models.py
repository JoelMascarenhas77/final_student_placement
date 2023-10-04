from django.db import models
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager


class MyUserManager(BaseUserManager):
    def create_user(self,username ,email ,password,key):
        user = self.model(username=username,email=email)
        user.set_password(password)
        user.save(using=self._db)
        user.student = key
        return user

    def create_superuser(self, username,email, password):
      
        user = self.model(username=username,email=email)
        user.set_password(password)
        user.is_admin = True
        user.save(using=self._db)
        return user
    

      

class student(models.Model):
        first_name = models.CharField(max_length=30)
        last_name = models.CharField(max_length=30)
        gender = models.CharField(max_length=4)
        age = models.IntegerField(default=0)
        branch = models.CharField(max_length=30)
        semester = models.CharField(max_length=2)
        divison = models.CharField(max_length=1)
        address = models.CharField(max_length=30)
        photo = models.FileField(upload_to='profiles/')
        grade = models.CharField(max_length=30)

  





class MyUser(AbstractBaseUser):
    username = models.CharField(max_length=30, unique=True)
    email = models.EmailField(max_length=50, unique=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    student = models.ForeignKey(student, on_delete=models.CASCADE ,null=True,default=None)

    objects = MyUserManager()

    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ['email']

    def __str__(self):  
        return self.username



class courses_internships(models.Model):
        name = models.CharField(max_length=30)
        company = models.CharField(max_length=30)
        students_enrolled = models.IntegerField(default=0)
        level= models.CharField(max_length=30)
        durations = models.CharField(max_length=30)
        grade = models.CharField(max_length=1)

class company(models.Model):
        name = models.CharField(max_length=30)
        city = models.CharField(max_length=30)
        positions = models.CharField(max_length=30)
        salary = models.IntegerField(default=0)
        students_alloted = models.IntegerField(default=0)

class feedback(models.Model):
        info = models.ForeignKey(MyUser, on_delete=models.CASCADE ,null=True,default=None)
        feedback= models.CharField(max_length=200)
        reply = models.CharField(max_length=200)
        created_at = models.DateField(max_length=30)
        updated_at = models.DateField(default=0)


class internships(models.Model):
      internship = models.FileField(upload_to="auth/media/internships")
      key = models.ForeignKey(student, on_delete=models.CASCADE ,null=True,default=None)
      
class reports(models.Model):
      repot = models.FileField(upload_to="auth/media/repots")
      key = models.ForeignKey(student, on_delete=models.CASCADE ,null=True,default=None)
      
class certificates(models.Model):  
       certificate = models.FileField(upload_to="auth/media/certificates")
       key = models.ForeignKey(student, on_delete=models.CASCADE ,null=True,default=None)

        









