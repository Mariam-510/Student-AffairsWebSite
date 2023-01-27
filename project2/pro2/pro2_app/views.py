from multiprocessing import context
from re import S
from django.shortcuts import get_object_or_404, redirect, render
from .models import *
from .forms import StudentForm, DepForm, CreateUserForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
# Create your views here.

def HomePage(request):
    return render(request, 'pages/Home page.html')

def StudentAffairs(request):
    return render(request, 'pages/Student Affairs.html')

def Login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request,user)
            return redirect('/Student Affairs')
        else:
            messages.info(request,'Username or Password is incorrect')
            return render(request, 'pages/Log in.html')

    return render(request, 'pages/Log in.html')


def Register(request):
    Rform = CreateUserForm()
    if request.method == 'POST':
        Rform = CreateUserForm(request.POST)
        if Rform.is_valid():
            Rform.save()
            user = Rform.cleaned_data.get('username')
            messages.success(request,'Account was created for ' + user)
            return redirect('/Login')

    context = {
        'Rform': Rform
    }
    return render(request, 'pages/Register.html',context)


def Logout(request):
    logout(request)
    return redirect('/Login')
    

@login_required(login_url='LoginStudent')
def AddStudent(request):
    if request.method == 'POST':
        add_student = StudentForm(request.POST)
        if add_student.is_valid():
            add_student.save()
        else:
            messages.info(request,'Form is Invalid!')
            return redirect('/Add')


    context = {
        'form': StudentForm(),
    }
    return render(request, 'pages/Add Student.html', context)


@login_required(login_url='LoginStudent')
def EditStudent(request):
    return render(request, 'pages/Edit Student Data.html')


@login_required(login_url='LoginStudent')
def Department(request):
    return render(request, 'pages/Department Assignment.html')


@login_required(login_url='LoginStudent')
def Search(request):
    search = Student.objects.filter(status='Active')
    name = None
    if 'search_name' in request.GET:
        name = request.GET['search_name']
        if name:
            search = search.filter(name__icontains=name)
    context = {
        'students': search,
        'allStudents': Student.objects.filter(status='Active').count(),
    }
    return render(request, 'pages/Search.html', context)


@login_required(login_url='LoginStudent')
def Status(request):
    context = {
        'students': Student.objects.all(),
        'allStudents': Student.objects.all().count(),
    }
    return render(request, 'pages/Status.html', context)


def DeletePage(request):
    return render(request, 'pages/Delete.html')

def update(request,id):
    student_id = Student.objects.get(id=id)
    if request.method == 'POST':
        student_save = StudentForm(request.POST,instance=student_id)
        if student_save.is_valid():
            student_save.save()
            return redirect('/Status')
        else:
            messages.info(request, 'Form is Invalid!')
    else:
        student_save = StudentForm(instance=student_id)

    context = {
        'form':student_save,
    }
    return render(request, 'pages/Edit Student Data.html',context)


def update2(request, id):
    student_id = Student.objects.get(id=id)
    if request.method == 'POST':
        student_save = StudentForm(request.POST, instance=student_id)
        if student_save.is_valid():
            student_save.save()
            return redirect('/Search')
        else:
            messages.info(request, 'Form is Invalid!')
    else:
        student_save = StudentForm(instance=student_id)

    context = {
        'form': student_save,
    }
    return render(request, 'pages/Edit Student Data.html', context)


def depUpdate(request, id):
    student_id = Student.objects.get(id=id)
    if request.method == 'POST':
        student_save = DepForm(request.POST, instance=student_id)
        if student_save.is_valid():
            student_save.save()
            return redirect('/Search')
    else:
        if (student_id.level == 'Third Level' or student_id.level == 'Fourth Level'):
            student_save = DepForm(instance=student_id)
        else:
            messages.info(request, 'Level Should be Third or Fourth To Assign Department')
            return redirect('/Search')

    context = {
        'Dform': student_save,
    }
    return render(request, 'pages/Department Assignment.html', context)


def delete(request, id):
    student_delete = Student.objects.get(id=id)
    if request.method =='POST':
        student_form = StudentForm(request.POST, instance=student_delete)
        student_delete.delete()
        return redirect('/Status')
    else:
        student_form = StudentForm(instance=student_delete)

    context = {
        'form': student_form,
    }
    return render(request, 'pages/Delete.html', context)


def delete2(request, id):
    student_delete = Student.objects.get(id=id)
    if request.method == 'POST':
        student_form = StudentForm(request.POST, instance=student_delete)
        student_delete.delete()
        return redirect('/Search')
    else:
        student_form = StudentForm(instance=student_delete)

    context = {
        'form': student_form,
    }
    return render(request, 'pages/Delete.html', context)
    

def staUpdate(request, id):
    student_id = Student.objects.get(id=id)
    if (student_id.status == 'Active'):
        student_id.status = 'Inactive'
        student_id.save()
        return redirect('/Status')
    elif (student_id.status == 'Inactive'):
        student_id.status = 'Active'
        student_id.save()
        return redirect('/Status')

    return render(request, 'pages/Status.html')


