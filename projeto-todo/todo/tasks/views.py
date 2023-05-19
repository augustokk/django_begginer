from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from .models import Task
from .forms import TaskForm


def helloworld(request):
    return HttpResponse ('Hello World!')


def taskList(request):
    # that will collect all objects from model Task from database
    # that will order the data by creation date
    tasks = Task.objects.all().order_by('-created_at')
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

def newTask(request):
    # that if will select the option to add task 
    if request.method == 'POST':

        #create a variable to access that form to be able to send to the template
        # fill the form with the data from POST
        form =TaskForm(request.POST) 

        # check if the form is valid
        if form.is_valid():

            # we select commit = False, because that will wait to see if the user change the option doing to done
            task = form.save(commit=False) 
            
            # we set as pattern the status of task as doing
            task.done = 'doing'

            # we save the task
            task.save()

            # after save the task we want to return to the 'home' page
            return redirect('/')
    else:
        form =TaskForm()  
        return render(request, 'tasks/addtask.html', {'form': form})