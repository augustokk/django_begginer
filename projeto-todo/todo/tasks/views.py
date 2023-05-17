from django.http import HttpResponse
from django.shortcuts import render


def helloworld(request):
    return HttpResponse ('Hello World!')


def taskList(request):
    return render (request, 'tasks/list.html')
# REMEMBER view always need request and return
# RENDER is a built-in function that needs 2 parameters: a request and a template
# we are going to create the template called list.html


def yourName(request, name):
    return render (request, 'tasks/yourname.html', {'name': name})
# 'name' could be any other word
# that is returning the request , template , argument

