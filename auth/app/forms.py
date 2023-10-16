from django import forms 
from django.forms import Form

from .models import CourseInternship,StudentCourseInternship,Report,Student


class AddStudentForm(forms.Form):

    photo = forms.FileField(label="Photo", required=False, widget=forms.FileInput(attrs={"class":"form-control"}))
    pid = forms.IntegerField(label="PID",  widget=forms.NumberInput(attrs={"class":"form-control"}))
    username = forms.CharField(label="Username", max_length=50, widget=forms.TextInput(attrs={"class":"form-control"}))
    password = forms.CharField(label="Password", max_length=8, widget=forms.PasswordInput(attrs={"class":"form-control"}))
    email = forms.EmailField(label="Email", max_length=50, widget=forms.EmailInput(attrs={"class":"form-control"}))
    first_name = forms.CharField(label="First Name", max_length=50, widget=forms.TextInput(attrs={"class":"form-control"}))
    last_name = forms.CharField(label="Last Name", max_length=50, widget=forms.TextInput(attrs={"class":"form-control"}))
    age = forms.IntegerField(label="Age",  widget=forms.NumberInput(attrs={"class":"form-control"}))
    
   

    gender_list = (
        ('Male','Male'),
        ('Female','Female')
    )

    branch_list = (
        ('Civil','Civil'),
        ('Computer Science','Computer Science'),
        ('Information Technology','Information Technology'),
        ('Electronics & Communication','Electronics & Communication'),
        ('Electrical','Electrical'),
        ('Mechanical','Mechanical')
    )

    semester_list = (
        ('I','I'),
        ('II','II'),
        ('III','III'),
        ('IV','IV'),
        ('V','V'),
        ('VI','VI'),
        ('VII','VII'),
        ('VIII','VIII'),

    )
    division_list = (
        ('A','A'),
        ('B','B')

    )

    hostel_list = (
        ('No','No'),
        ('Yes','Yes')

    )

    gender = forms.ChoiceField(label="Gender", choices=gender_list, widget=forms.Select(attrs={"class":"form-control"}))
    hostel = forms.ChoiceField(label="Hostel", choices=hostel_list, widget=forms.Select(attrs={"class":"form-control"}))
    address = forms.CharField(label="Address", max_length=50, widget=forms.TextInput(attrs={"class":"form-control"}))
    branch = forms.ChoiceField(label="Branch", choices=branch_list, widget=forms.Select(attrs={"class":"form-control"}))
    semester = forms.ChoiceField(label="Semester", choices=semester_list, widget=forms.Select(attrs={"class":"form-control"}))
    division = forms.ChoiceField(label="Division", choices=division_list, widget=forms.Select(attrs={"class":"form-control"}))

class CertificateForm(forms.ModelForm):
    domain = forms.ChoiceField(choices=[], required=False)
    certificates = forms.FileField()

    def __init__(self, *args, **kwargs):
        super(CertificateForm, self).__init__(*args, **kwargs)
        domains = CourseInternship.objects.values_list('domain', flat=True).distinct()
        domain_choices = [(domain, domain) for domain in domains]
        
        domain_choices.insert(0, ('Other', 'Other'))
        
        self.fields['domain'].choices = domain_choices

    class Meta:
        model = StudentCourseInternship
        fields = ('domain','certificates')

class ReportForm(forms.ModelForm):
    cgpa = forms.DecimalField()
    backlogs = forms.IntegerField()
    reports = forms.FileField()

    class Meta:
        model = Report
        fields = ('cgpa', 'backlogs', 'reports')


    
   
                                  
    
    
    

    
    
    
    
    