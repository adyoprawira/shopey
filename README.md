# Tugas 2
Link: http://adyo-arkan-shopey.pbp.cs.ui.ac.id/
## Creating a Django Project
### Django Project Initialization
1. Create a new folder with the project name ```shopey```
2. Create a Python Virtual Environment on that folder using this command in PowerShell:
   ```bash
   python -m venv env
   ```
3. Activate the Virtual Environment using this command:
   ```bash
   env/Scripts/Activate
   ```
4. Create a new requirements.txt in that folder, and fill it with:
   ```
   django
   gunicorn
   whitenoise
   psycopg2-binary
   requests
   urllib3
   ```
5. Install the dependencies with env using this command:
   ```bash
   pip install -r requirements.txt
   ```
6. Create the Django Project using this command:
   ```bash
   django-admin startproject shopey .
   ```
### Routing
1. Route the project to localhost, add this to ALLOWED_HOSTS in settings.py:
   ```
   ...
   ALLOWED_HOSTS = ["localhost", "127.0.0.1"]
   ...
   ```
2. Ensure that my Django project has been successfully made and ported locally by running:
   ```bash
   python manage.py runserver
   ```
   , access http://localhost:8000/ and check the flying rocket animation.
### Upload Project to Github
1. Create a new Github repo named ```shopey```.
2. Initialize the current directory as a Git repository using:
   ```bash
   git init
   ```
3. Add a ```.gitignore``` file, with the following text:
   ```
   # Django
   *.log
   *.pot
   *.pyc
   __pycache__
   db.sqlite3
   media
   
   # Backup files
   *.bak
   
   # If you are using PyCharm
   # User-specific stuff
   .idea/**/workspace.xml
   .idea/**/tasks.xml
   .idea/**/usage.statistics.xml
   .idea/**/dictionaries
   .idea/**/shelf
   
   # AWS User-specific
   .idea/**/aws.xml
   
   # Generated files
   .idea/**/contentModel.xml
   .DS_Store
   
   # Sensitive or high-churn files
   .idea/**/dataSources/
   .idea/**/dataSources.ids
   .idea/**/dataSources.local.xml
   .idea/**/sqlDataSources.xml
   .idea/**/dynamic.xml
   .idea/**/uiDesigner.xml
   .idea/**/dbnavigator.xml
   
   # Gradle
   .idea/**/gradle.xml
   .idea/**/libraries
   
   # File-based project format
   *.iws
   
   # IntelliJ
   out/
   
   # JIRA plugin
   atlassian-ide-plugin.xml
   
   # Python
   *.py[cod]
   *$py.class
   
   # Distribution / packaging
   .Python build/
   develop-eggs/
   dist/
   downloads/
   eggs/
   .eggs/
   lib/
   lib64/
   parts/
   sdist/
   var/
   wheels/
   *.egg-info/
   .installed.cfg
   *.egg
   *.manifest
   *.spec
   
   # Installer logs
   pip-log.txt
   pip-delete-this-directory.txt
   
   # Unit test / coverage reports
   htmlcov/
   .tox/
   .coverage
   .coverage.*
   .cache
   .pytest_cache/
   nosetests.xml
   coverage.xml
   *.cover
   .hypothesis/
   
   # Jupyter Notebook
   .ipynb_checkpoints
   
   # pyenv
   .python-version
   
   # celery
   celerybeat-schedule.*
   
   # SageMath parsed files
   *.sage.py
   
   # Environments
   .env
   .venv
   env/
   venv/
   ENV/
   env.bak/
   venv.bak/
   
   # mkdocs documentation
   /site
   
   # mypy
   .mypy_cache/
   
   # Sublime Text
   *.tmlanguage.cache
   *.tmPreferences.cache
   *.stTheme.cache
   *.sublime-workspace
   *.sublime-project
   
   # sftp configuration file
   sftp-config.json
   
   # Package control specific files Package
   Control.last-run
   Control.ca-list
   Control.ca-bundle
   Control.system-ca-bundle
   GitHub.sublime-settings
   
   # Visual Studio Code
   .vscode/*
   !.vscode/settings.json
   !.vscode/tasks.json
   !.vscode/launch.json
   !.vscode/extensions.json
   .history
   ```
4. Push to Github using:
```bash
git add .
git commit -m "Uploaded project to Github"
git push -u origin main
```
## Create an application with the name main in the project
### Creating Django App and Model
1. Activate Python Virtual Environment on the root directory, if haven't, using:
   ```bash
   python -m venv env
   env\Scripts\Activate
   ```
2. Create app main by running:
   ```bash
   python manage.py startapp main
   ```
3. Create ```main.html``` annd fill it with:
   ```
   <h1>Shopey</h1>
   
   <h5>App name: </h5>
   <p>{{app_name}}</p> <!-- Change according to your npm -->
   <h5>Name: </h5>
   <p>{{name}}</p> <!-- Change according to your name -->
   <h5>Class: </h5>
   <p>{{kki}}</p> <!-- Change according to your class -->
   ```
   
##  Perform routing in the project so that the application main can run
1. Register ```main``` app on the project by adding it to ```INSTALLED_APPS``` on ```settings.py```
   ```
   INSTALLED_APPS = [
      ...,
      'main'
   ]
   ```

## Create a model in the application main with the name Product and have the mandatory attributes name, price and description
### Implement Models
1. Fill ```models.py``` in the main app directory with:
   ```
   from django.db import models

   class Product(models.Model):
       name = models.CharField(max_length=50)
       price = models.IntegerField()
       description = models.TextField()
   ```
### Migrate Models
1. Create model migrations by running:
   ```bash
   python manage.py makemigrations
   ```
2. Apply migrations to local database by running:
   ```bash
   python manage.py migrate
   ```
## Create a function in views.py to return to an HTML template that displays the name of the application and your name and class.
1. Open ```views.py``` in the main app and fill it with:
   ```
   def show_main(request):
       context = {
           'app_name' : 'Shopey',
           'name': 'Adyo Arkan Prawira',
           'class': 'KKI'
       }
   
       return render(request, "main.html", context)
   ```
## Create a routing in urls.py for the application main to map the function created in views.py
1. Create ```urls.py``` in main directory and fill it with:
   ```
   from django.urls import path
   from main.views import show_main
   
   app_name = 'main'
   
   urlpatterns = [
       path('', show_main, name='show_main'),
   ]
   ```
2. Configure the project URL routing by importing include from django.urls and URL route in ```urls.py```:
   ```
   ...
   from django.urls import path, include
   ...

   urlpatterns = [
       ...
       path('', include('main.urls')),
       ...
   ]
   ```
## Perform deployment to PWS for the application that has been created so that it can be accessed by others via the Internet.
1. Create a new project in https://pbp.cs.ui.ac.id/
2. Save the project credentials
3. Add the PWS deployment url to ```ALLOWED_HOSTS``` in ```settings.py```
4. Do add, commit, and push:
   ```bash
   git remote add pws <pws-url>
   git push pws main:master
   ```
## Create a ```README.md``` that contains a link to the PWS application that has been deployed, as well as answers to the following questions
1. Go to Github.com
2. Create new ```README.md``` file

## Create a diagram that contains the request client to a Django-based web application and the response it gives, and explain the relationship between urls.py, views.py, models.py, and the html file.
https://imgur.com/a/vL10NcL


## Use of Git in Software Development
1. Git tracks changes to files over time. This allows developers to revisit specific versions of the project. So, they can revert to a previous state.
2. With Git, it is possible tfor multiple developers to collaborate and work on the same project at the same time. It allows each person to have a local copy of the project. Each devs can make changes independently and Git helps in merging changes from different contributors.

## In your opinion, out of all the frameworks available, why is Django used as the starting point for learning software development?
1. Django has an Object-Relational Mapper (ORM), which allows developers to interact with the database using Python code instead of writing raw SQL queries. This abstraction simplifies database management for beginners and helps them understand database concepts without the need for complex SQL knowledge right away.
2. Django enforces the Model-View-Template (MVT) design pattern, which provides a clear separation of concerns:
Model: Manages the database and data structures.
View: Handles business logic and user interaction.
Template: Manages the presentation layer (HTML, CSS).
This structure helps beginners learn how to organize their code effectively, which is an essential skill in software development.
3. Django is a full-stack web framework, meaning it covers both the front-end and back-end aspects of web development. Beginners can build complete web applications without having to use multiple frameworks for different parts of the project. This helps learners understand the full process of web development in one place.
   
## Why is the Django model called an ORM?
The Django model is called an ORM (Object-Relational Mapping) because it serves as a bridge between object-oriented programming and relational databases. An ORM is a programming technique that allows developers to interact with a relational database using the principles of object-oriented programming. Instead of writing raw SQL queries to manipulate the database, you work with Python objects (in Django’s case), and the ORM handles converting those objects into database queries and vice versa.
