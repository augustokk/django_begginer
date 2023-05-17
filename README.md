# django_begginer
That repository will help to show how you start your first steps using django

Firts step install python in your machine: 
- you can download it from (https://www.python.org/downloads/)

Second step open your cmd on your windows:
- run command (python --version) [that will check if you got python properly installed] 
- run command (pip --version) [when you download python that will install together unless you decide for not to do]
- run command (python -m pip install --upgrade pip) [that will upgrade your pip for the newes version, if necessary]
- run command (pip install virtualenv) [that will install necessary tools for virtual environment]
- run command (mkdir testevenv) [that will create a specific directory where we are going to use our virtual env *testevenv can be any name]
- run command (cd testevenv) [that will move us into that new directory]
- run command (virtualenv myenv) [that wil crreate your virtual environment *myenv can be any name]
- run command (myenv\Scripts\activate) [that will move you into the virtual environment]
- run command (pip install django) [that will install django in your virtual environment]
- run command (django-admin --version) [that will check if you got django properly installed]
- run command (django-admin startproject helloworld) [that will start our first test project *helloworld can be any name]
- run command (python manage.py runserver) [that will run the django server]

Third step open your browser:
- type http://localhost:8000/ on your url
- that will open a django page with the successful message (The install worked successfully! Congratulations!)
