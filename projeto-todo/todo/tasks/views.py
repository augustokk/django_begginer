from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from .models import Task
from .forms import TaskForm
from django.contrib import messages
from django.core.paginator import Paginator


def helloworld(request):
    return HttpResponse ('Hello World!')


def taskList(request):
    # that will collect all objects from model Task from database
    # that will order the data by creation date
    tasks_list = Task.objects.all().order_by('-created_at')

    # that will create a pagination that will display only 3 tasks per page
    # avoid overuse of the database, user-friendly not populating too much the pages
    paginator = Paginator(tasks_list, 3)

    # create a variable to set the url for the page
    # then the tasks to be shown will be depending of the page requested
    # that allows to show the correct number of tasks (3) on the correct page
    page =request.GET.get('page')
    tasks = paginator.get_page(page)

    # REMEMBER view always need request and return
    # RENDER is a built-in function that needs 2 parameters: a request and a template
    # we are going to create the template called list.html
    # we add a dictionary to send all that objects to the template
    return render (request, 'tasks/list.html', {'tasks' : tasks})


def yourName(request, name):
    # 'name' could be any other word
    # that is returning the request , template , argument
    return render (request, 'tasks/yourname.html', {'name': name})


# that will receive 2 arguments request and unique id provided by django database
def taskView(request, id): 
    # that will get all objects with id as primary key from database
    # if there is none object with id, return a 404 error (safety reason)
    task = get_object_or_404(Task, pk=id)
    return render (request, 'tasks/task.html', {'task' : task})


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

            # session message to show for user that he added the task
            messages.info(request, 'Task Added successfully!')

            # after save the task we want to return to the 'home' page
            return redirect('/')
    else:
        form =TaskForm()  
        return render(request, 'tasks/addtask.html', {'form': form})
    

# that function needs to receive the id to be able to edit the specific task
def editTask(request, id):

    # with that built-in function will collect the object with the specific id
    # if there is none, return error 404
    task = get_object_or_404(Task, pk=id)

    # need to have a filled form to be able to update it
    # we use the instance to be able to show the form filled to the user
    form = TaskForm(instance=task)

    #check if there is any form 
    if(request.method == 'POST'):
        form = TaskForm(request.POST, instance=task)

        # check if the form is valid
        if(form.is_valid()):
            # save the task
            task.save()

            # session message to show for user that he updated the task
            messages.info(request, 'Task Updated successfully!')

             # after save the task we want to return to the 'home' page
            return redirect('/')
        else:
            return render(request, 'tasks/edittask.html', {'form' : form, 'task': task})
        
    else:
        return render(request, 'tasks/edittask.html', {'form' : form, 'task': task})
    
    
# that function needs to receive the id to be able to delete the specific task
def deleteTask(request, id):
    task = get_object_or_404(Task, pk=id)
    task.delete()

    # session message to show for user that he deleted the task
    messages.info(request, 'Task Deleted successfully!')
    return redirect('/')