from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import TaskSerializer
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from .forms import TaskForm
from .models import Task


def task_list(request):

    tasks = Task.objects.all()

    return render(
        request,
        'tasks/task_list.html',
        {'tasks': tasks}
    )


def create_task(request):

    if request.user.role != 'ADMIN':
        return HttpResponse("Only Admin can create tasks")

    if request.method == 'POST':

        form = TaskForm(request.POST)

        if form.is_valid():

            form.save()

            return redirect('task_list')

    else:

        form = TaskForm()

    return render(
        request,
        'tasks/create_task.html',
        {'form': form}
    )
def edit_task(request, task_id):

    task = get_object_or_404(Task, id=task_id)

    if request.method == 'POST':

        form = TaskForm(request.POST, instance=task)

        if form.is_valid():

            form.save()

            return redirect('task_list')

    else:

        form = TaskForm(instance=task)

    return render(
        request,
        'tasks/create_task.html',
        {'form': form}
    )


def delete_task(request, task_id):

    task = get_object_or_404(Task, id=task_id)

    task.delete()

    return redirect('task_list')
@api_view(['GET'])
def task_api(request):

    tasks = Task.objects.all()

    serializer = TaskSerializer(
        tasks,
        many=True
    )

    return Response(serializer.data)