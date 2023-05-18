from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import Task


def helloworld(request):
    return HttpResponse ('Hello World!')


def taskList(request):
    tasks = Task.objects.all() # that will collect all objects from model Task from database
    return render (request, 'tasks/list.html', {'tasks' : tasks})
# REMEMBER view always need request and return
# RENDER is a built-in function that needs 2 parameters: a request and a template
# we are going to create the template called list.html
# we add a dictionary to send all that objects to the template

def yourName(request, name):
    return render (request, 'tasks/yourname.html', {'name': name})
# 'name' could be any other word
# that is returning the request , template , argument


def taskView(request, id): 
    task = get_object_or_404(Task, pk=id)
    return render (request, 'tasks/task.html', {'task' : task})
    # that will receive 2 arguments request and unique id provided by django database
    # that will get all objects with id as primary key from database
    # if there is none object with id, return a 404 error (safety reason)

