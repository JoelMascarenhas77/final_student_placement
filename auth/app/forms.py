from django import forms 
from django.forms import Form


class AddStudentForm(forms.Form):

    photo = forms.FileField(label="Photo", required=False, widget=forms.FileInput(attrs={"class":"form-control"}))
    username = forms.CharField(label="Username", max_length=50, widget=forms.TextInput(attrs={"class":"form-control"}))
    password = forms.CharField(label="Password", max_length=50, widget=forms.PasswordInput(attrs={"class":"form-control"}))
    email = forms.EmailField(label="Email", max_length=50, widget=forms.EmailInput(attrs={"class":"form-control"}))
    first_name = forms.CharField(label="First Name", max_length=50, widget=forms.TextInput(attrs={"class":"form-control"}))
    last_name = forms.CharField(label="Last Name", max_length=50, widget=forms.TextInput(attrs={"class":"form-control"}))
    age = forms.IntegerField(label="Age",  widget=forms.NumberInput(attrs={"class":"form-control"}))
    
   

    gender_list = (
        ('Male','Male'),
        ('Female','Female')
    )

    branch_list = (
        ('Computer','Computer'),
        ('Information Technology','Information Technology'),
        ('Electronics & Telecomunication','Electronics & Telecomunication'),
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

    )
    division_list = (
        ('A','A'),
        ('B','B')

    )
    gender = forms.ChoiceField(label="Gender", choices=gender_list, widget=forms.Select(attrs={"class":"form-control"}))
    address = forms.CharField(label="Address", max_length=50, widget=forms.TextInput(attrs={"class":"form-control"}))
    branch = forms.ChoiceField(label="Branch", choices=branch_list, widget=forms.Select(attrs={"class":"form-control"}))
    semester = forms.ChoiceField(label="Semester", choices=semester_list, widget=forms.Select(attrs={"class":"form-control"}))
    division = forms.ChoiceField(label="Division", choices=division_list, widget=forms.Select(attrs={"class":"form-control"}))
   
                                  
    
    
    

    
    
    
    
    