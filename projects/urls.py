from django.urls import path
from .views import project_list, create_project, project_api

urlpatterns = [
    path('projects/', project_list, name='project_list'),
    path('projects/create/', create_project, name='create_project'),
    path('api/projects/', project_api),
    ]