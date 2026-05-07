from django.urls import path

from .views import (
    task_list,
    create_task,
    edit_task,
    delete_task,
    task_api,
)

urlpatterns = [

    path('tasks/', task_list, name='task_list'),

    path(
        'tasks/create/',
        create_task,
        name='create_task'
    ),

    path(
        'tasks/edit/<int:task_id>/',
        edit_task,
        name='edit_task'
    ),

    path(
        'tasks/delete/<int:task_id>/',
        delete_task,
        name='delete_task'
    ),
    path('api/tasks/', task_api),
]