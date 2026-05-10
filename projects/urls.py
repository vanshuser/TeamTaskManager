from django.urls import path
from .views import project_list, create_project,edit_project, delete_project , project_api

urlpatterns = [
    path('projects/', project_list, name='project_list'),
    path('projects/create/', create_project, name='create_project'),
    path('api/projects/', project_api),
    path('projects/edit/<int:id>/',edit_project,name='edit_project'),
    path('projects/delete/<int:id>/',delete_project,name='delete_project'),
    ]