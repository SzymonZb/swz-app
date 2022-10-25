from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from .forms import TaskUpdateForm
from .models import *
from .decorators import unauthenticated_user, admin_only


@unauthenticated_user
def loginPage(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'Nieprawidłowy login lub hasło')

    context = {}
    return render(request, 'tasks/login.html', context)


def logoutUser(request):
    logout(request)
    return redirect('login')


@login_required(login_url='login')
@admin_only
def home(request):
    task_updates = TaskUpdate.objects.all()
    employees = Employee.objects.all()
    total_orders = task_updates.count()

    context = {'task_updates': task_updates, 'employees': employees,
               'total_orders': total_orders}

    return render(request, 'tasks/dashboard.html', context)


@login_required(login_url='login')
def userPage(request):
    tasks = request.user.employee.task_set.all()
    context = {'tasks': tasks}
    return render(request, 'tasks/user.html', context)

@login_required(login_url='login')
def tasks(request):
    tasks = Task.objects.all()

    return render(request, 'tasks/tasks.html', {'tasks': tasks})


@login_required(login_url='login')
def employee(request, pk_test):
    employee = Employee.objects.get(id=pk_test)

    tasks = Task.objects.all()

    taskupdates = employee.taskupdate_set.all()
    context = {'employee': employee, 'taskupdates': taskupdates, 'tasks': tasks}
    return render(request, 'tasks/employee.html', context)


@login_required(login_url='login')
def updateTask(request):
    form = TaskUpdateForm()
    if request.method == 'POST':
        form = TaskUpdateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'form': form}

    return render(request, 'tasks/taskupdate_form.html', context)

@login_required(login_url='login')
def overview(request, pk_ov):
    employee = Employee.objects.get(id=pk_ov)

    tasks = Task.objects.all()

    taskupdates = employee.taskupdate_set.all()
    context = {'employee': employee, 'taskupdates': taskupdates, 'tasks': tasks}
    return render(request, 'tasks/overview.html', context)
