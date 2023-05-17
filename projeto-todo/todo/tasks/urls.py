# from django.contrib import admin [that line just need to be called once on project, not in all apps]
from django.urls import path
from . import views
urlpatterns = [
    path('helloworld/', views.helloworld),
]
