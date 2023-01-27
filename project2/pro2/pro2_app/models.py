from unicodedata import name
from django.db import models
from .validators import validate_domainonly_GPA, validate_domainonly_id, validate_domainonly_email


# Create your models here.

class Student (models.Model):

    gender_student = [
        ('Male','Male'),('Female','Female')
    ]

    status_student = [
        ('Active', 'Active'), ('Inactive', 'Inactive')
    ]

    level_student = [
        ('First Level', 'First Level'), ('Second Level', 'Second Level'),
        ('Third Level', 'Third Level'), ('Fourth Level', 'Fourth Level')
    ]

    department_student = [
        ('Computer_Science_(CS)', 'Computer_Science_(CS)'),
        ('Artificial_Intelligence_(AI)', 'Artificial_Intelligence_(AI)'),
        ('Information_Technology_(IT)', 'Information_Technology_(IT)'),
        ('Information_System_(IS)', 'Information_System_(IS)'),
        ('Decision_Support_(DS)', 'Decision_Support_(DS)'),
    ]

    id = models.IntegerField(primary_key=True, validators=[validate_domainonly_id])
    name = models.CharField(max_length=1000)
    dateOfBirth = models.DateField()
    GPA = models.DecimalField(max_digits=4, decimal_places=2, validators=[validate_domainonly_GPA])
    gender = models.CharField(max_length=250, choices=gender_student, default="Male")
    level = models.CharField(max_length=500, choices=level_student)
    email = models.EmailField(max_length=250, validators=[validate_domainonly_email])
    mobileNumber = models.CharField(max_length=250)
    department = models.CharField(max_length=500, choices=department_student, null=True, blank=True)
    status = models.CharField(max_length=250, choices=status_student, default="Active")

    def __str__(self):
        return self.name


