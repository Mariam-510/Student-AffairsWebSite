from dataclasses import field
from distutils.command.clean import clean
from tkinter import Widget
from django import forms
from .models import Student
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = [
            'id',
            'name',
            'dateOfBirth',
            'GPA',
            'gender',
            'level',
            'email',
            'mobileNumber',
            'department',
            'status',
        ]

        Widgets={
            'id': forms.NumberInput(),
            'name': forms.TextInput(),
            'dateOfBirth': forms.DateInput(),
            'GPA': forms.NumberInput(),
            'gender': forms.Select(),
            'level': forms.Select(),
            'email': forms.EmailInput(),
            'mobileNumber': forms.TextInput(),
            'department': forms.Select(),
            'status': forms.Select(),
        }

class DepForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = [
            'name',
            'id',
            'department',
        ]

        Widgets = {
            'id': forms.NumberInput(),
            'name': forms.TextInput(),
            'department': forms.Select(),
        }

    def __init__(self, *args, **kwargs):
        super(DepForm, self).__init__(*args, **kwargs)
        instance = getattr(self, 'instance', None)
        if instance and instance.pk:
            for field in self.fields.keys():
                self.fields[field].widget.attrs['readonly'] = True


class CreateUserForm (UserCreationForm):
    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'password1',
            'password2',
        ]

