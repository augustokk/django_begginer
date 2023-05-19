from django import forms

# that will make easier, because it will respect the fields we have already
from .models import Task 

# create a class using the method Modelform imported from django 
class TaskForm(forms.ModelForm):

    class Meta:
        # we use our Task class as model, that will have only attributes that we need
        model = Task

        # select the fields that we want to appear on the screen (title / description)
        fields = ('title', 'description')
        