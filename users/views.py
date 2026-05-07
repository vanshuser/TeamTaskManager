from django.utils.timezone import now
from projects.models import Project
from tasks.models import Task
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.http import HttpResponse

from .forms import SignupForm


def signup_view(request):

    if request.method == 'POST':
        form = SignupForm(request.POST)

        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('dashboard')

    else:
        form = SignupForm()

    return render(request, 'users/signup.html', {'form': form})


def login_view(request):

    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('dashboard')

    else:
        form = AuthenticationForm()

    return render(request, 'users/login.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('login')


def dashboard(request):

    total_projects = Project.objects.count()

    total_tasks = Task.objects.count()

    completed_tasks = Task.objects.filter(
        status='DONE'
    ).count()

    pending_tasks = Task.objects.exclude(
        status='DONE'
    ).count()
    overdue_tasks = Task.objects.filter(
    deadline__lt=now().date()
    ).exclude(status='DONE').count()

    context = {
        'total_projects': total_projects,
        'total_tasks': total_tasks,
        'completed_tasks': completed_tasks,
        'pending_tasks': pending_tasks,
        'overdue_tasks': overdue_tasks,
    }

    return render(
        request,
        'users/dashboard.html',
        context
    )