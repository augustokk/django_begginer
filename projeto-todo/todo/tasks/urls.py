# from django.contrib import admin [that line just need to be called once on project, not in all apps]
from django.urls import path
from . import views
urlpatterns = [
    path('helloworld/', views.helloworld),
    path('', views.taskList, name='task-list'),  # empty url will be the 'home'
    path('yourname/<str:name>', views.yourName, name='your-name'),  # that will allow to receive a string
    path('task/<int:id>', views.taskView, name="task-view"),  # that will receive an id and return a task on template

]
