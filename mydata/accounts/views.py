from .forms import UserCreateForm
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .models import  Employee
from .forms import EmployeeForm


def welcome(request):
    return render(request, 'student/welcome.html')

def load_form(request):
    form = EmployeeForm
    return render(request, 'student/index.html', {'form': form})

def add(request):
    form = EmployeeForm(request.POST)
    form.save()
    return redirect('show/')

def show(request):
    employee = Employee.objects.all
    return render(request, 'student/show.html', {'employee': employee})

def edit(request, id):
    employee = Employee.objects.get(id=id)
    return render(request, 'student/edit.html', {'employee': employee})

def update(request, id):
    emplyee = Employee.objects.get(id=id)
    form = EmployeeForm(request.POST, instance=emplyee)
    form.save()
    return redirect('/show')

def delete(request, id):
    employee = Employee.objects.get(id=id)
    employee.delete()
    return redirect('/show')

def search(request):
    given_name = request.POST['name']
    employee = Employee.objects.filter(ename__icontains=given_name)
    return render(request, 'student/show.html', {'employee': employee})

def signup(request):
    if request.method == 'POST':
        form = UserCreateForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            new_user = authenticate(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password1']
            )
            login(request, new_user)
            return redirect('home')
    else:
        form = UserCreateForm()
    return render(request, 'registration/signup.html', {'form': form})
