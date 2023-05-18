from django.db import models

class Task(models.Model): #inherit data from the file models of the class Model

    # constant with values in tuple 
    STATUS= (
        ('Doing', 'Doing'),
        ('Done', 'Done'),
    )

    title = models.CharField(max_length=255)
    # inherit data from the file models of the class Charfield
    # charfield means that will accpt any element from charset
    # that needs to receive a size argument, we set as 255

    description = models.TextField()
    # use textfield, because there is no max length, better choice for description

    done = models.CharField(
        max_length=10, 
        choices = STATUS,)
    # the value will be determined by the constant STATUS

    created_at = models.DateTimeField(auto_now_add=True)
    # that will automatically store the new date and time when a new object is created

    updated_at =  models.DateTimeField(auto_now=True)
    # that will automatically store the date and time when a new object is updated

# function to show title of task in the django admin website
    def __str__(self):
        return self.title