from django.shortcuts import render, redirect
from django.http import HttpResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response

from .forms import ProjectForm
from .models import Project
from .serializers import ProjectSerializer 
from django.contrib.auth.decorators import login_required 
from django.shortcuts import get_object_or_404

@login_required
def project_list(request):

    projects = Project.objects.all()

    return render(
        request,
        'projects/project_list.html',
        {'projects': projects}
    )

@login_required
def create_project(request):

    if request.user.role != 'ADMIN':
        return HttpResponse("Only Admin can create projects")

    if request.method == 'POST':

        form = ProjectForm(request.POST)

        if form.is_valid():

            project = form.save(commit=False)

            project.created_by = request.user

            project.save()

            form.save_m2m()

            return redirect('project_list')

    else:

        form = ProjectForm()

    return render(
        request,
        'projects/create_project.html',
        {'form': form}
    )

@login_required
def edit_project(request, id):

    project = get_object_or_404(Project, id=id)

    if request.method == 'POST':

        form = ProjectForm(
            request.POST,
            instance=project
        )

        if form.is_valid():
            form.save()
            return redirect('project_list')

    else:
        form = ProjectForm(instance=project)

    return render(
        request,
        'projects/create_project.html',
        {'form': form}
    )
@login_required
def delete_project(request, id):

    project = get_object_or_404(Project, id=id)

    project.delete()

    return redirect('project_list')
@api_view(['GET'])
def project_api(request):

    projects = Project.objects.all()

    serializer = ProjectSerializer(
        projects,
        many=True
    )

    return Response(serializer.data)