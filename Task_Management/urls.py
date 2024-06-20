from django.contrib import admin
from django.urls import path, include
from task.views import show_tasks

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', show_tasks, name='home'), 
    path('task/', include('task.urls')),
    path('category/', include('category.urls')),
]

