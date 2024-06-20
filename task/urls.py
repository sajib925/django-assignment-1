# from django.urls import path
# from . import views

# urlpatterns = [
#     path('add/', views.add_task, name='add_task'),
#     path('edit/<int:task_id>/', views.edit_task, name='edit_task'),
#     path('delete/<int:task_id>/', views.delete_task, name='delete_task'),
#     path('complete/<int:task_id>/', views.complete_task, name='complete_task'),
#     path('', views.show_tasks, name='show_tasks'),
# ]

# from django.urls import path
# from .views import add_task, show_tasks, edit_task, delete_task, complete_task

# app_name = 'tasks'

# urlpatterns = [
#     path('add/', add_task, name='add_task'),
#     path('show/', show_tasks, name='show_tasks'),
#     path('edit/<int:task_id>/', edit_task, name='edit_task'),
#     path('delete/<int:task_id>/', delete_task, name='delete_task'),
#     path('complete/<int:task_id>/', complete_task, name='complete_task'),
# ]

from django.urls import path
from .views import add_task, edit_task, delete_task, complete_task, show_tasks

urlpatterns = [
    path('', show_tasks, name='home'),
    path('add/', add_task, name='add_task'),
    path('edit/<int:task_id>/', edit_task, name='edit_task'),
    path('delete/<int:task_id>/', delete_task, name='delete_task'),
    path('complete/<int:task_id>/', complete_task, name='complete_task'),
]
