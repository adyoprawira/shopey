# Assignment 2
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
![Blank diagram_page-0001](https://github.com/user-attachments/assets/12800730-2305-44e4-bbb3-6e0735eb77ef)


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

# Assignment 3

## Explain why we need data delivery in implementing a platform.
Data delivery is essential when implementing a platform because it ensures that information gets to the right users or systems quickly and accurately. This helps the platform work smoothly, allows for real-time decisions, keeps data safe, and ensures everyone is working with the same, up-to-date information. Without efficient data delivery, platforms would struggle to meet user expectations, maintain performance, and protect sensitive information.

## In your opinion, which is better, XML or JSON? Why is JSON more popular than XML?
In my opinion JSON is better for most modern application, for these reasons:
1. JSON is simpler and easier to read and write compared to XML.
2. JSON is more efficient because it doesn't require the additional tags and attributes that XML needs. This leads to smaller payload, which means faster data transmission and better performance in web applications.
3. XML has a lot of overhead with its start and end tags, while JSON uses a key-value format thats more concise. This reduces complexity.

JSON is more popular than XML because it is better suited for the modern web, where lightweight, fast, and easy-to-handle data formats are preferred. XML is still useful in some legacy systems and when document structure is important, but JSON’s simplicity and performance have made it the default choice for most applications today.

## Why do we need csrf_token when creating a form in Django? What could happen if we did not use csrf_token on a Django form? How could this be leveraged by an attacker?
```csrf_token``` is used to protect forms from CSRF (Cross-Site Request Forgery) attacks. CSRF occurs when an attacker tricks a user into unknowingly submitting a form or making a request on a website where they are authenticated, potentially leading to unauthorized actions such as changing account details or making transactions. The ```csrf_token``` acts as a security token that ensures the fomr submission is coming from the legitimate source (the same domain) and not from an external malicious site. It is unique and included in forms, which the server verifies when the form is submitted. If the token is missing or invalid, Django rejects the request, preventing unauthorized form submissions. If a Django form doesn't use ```csrf_token```, then it would be vulnerable to CSRF attacks. This means that an attacker could create a form that mimics legitimate actions such as;
   * Changing passwords
   * Transferring funds
   * etc.

## Explain how you implemented the checklist above step-by-step (not just following the tutorial).
### Create a form input to add a model object to the previous app.
1. Create a new file named ```forms.py``` in the ```main``` directory and add the following code;
   ```
   from django.forms import ModelForm
   from main.models import Product

   class ProductForm(ModelForm):
       class Meta:
           model = Product
           fields = ["name", "price", "description"]
   ```
2. Import the model, form, and redirect to ```views.py```.
   ```
   from django.shortcuts import render, redirect
   from main.forms import ProductForm
   from main.models import Product
   ```
3. Create a function named ```create_product``` that produces a form that adds a product data whenever a data is submitted from the form.
   ```
   def create_product(request):
       form = ProductForm(request.POST or None)

       if form.is_valid() and request.method == "POST":
           form.save()
           return redirect("main:show_main")
    
       context = {'form': form}
       return render(request, "create_product.html", context)
   ```
4. Import the ```create_product``` function that was previously created to ```urls.py```.
   ```
   from main.views import show_main, create_product
   ```
5. Add the URL path to ```urlpatterns``` so that it can be accessed.
   ```
   urlpatterns = [
      ...
      path('create-product', create_product, name='create_product'),
   ]
6. Create a new HTML file named ```create_product.html``` in ```templates``` in the ```main``` directory and fill it with;
   ```
   {% extends 'base.html' %}
   {% block content %}
   <h1>Add New Product</h1>
   
   <form method="POST">
       {% csrf_token %}
       <table>
           {{ form.as_table }}
           <tr>
               <td></td>
               <td>
                   <input type="submit" value="Add Mood Entry" />
               </td>
           </tr>
       </table>
   </form> 
   {% endblock %}
   ```
7. Add this following code in ```main.html``` between {% block content %} and {% endblock content %} to display the data in a table form and add a button to redirect to the form page.
   ```
   {% extends 'base.html' %}
   {% block content %}
   <h1>Shopey</h1>
   
   <h5>App name: </h5>
   <p>{{app_name}}</p> 
   
   <h5>Name: </h5>
   <p>{{name}}</p> 
   
   <h5>Class: </h5>
   <p>{{class}}</p> 
   
   {% if not product_entries %}
   <p>There are no product in Shopey.</p>
   {% else %}
   
   <table>
     <tr>
       <th>Name</th>
       <th>Price</th>
       <th>Description</th>
     </tr>
   
     {% comment %} This is how to display product
     {% endcomment %} 
     {% for product_entry in product_entries %}
     <tr>
         <td>{{product_entry.name}}</td>
         <td>{{product_entry.price}}</td>
         <td>{{product_entry.description}}</td>
       </tr>
       {% endfor %}
     </table>
     {% endif %}
   
       <br />
   
       <a href="{% url 'main:create_product' %}">
         <button>Add New Product</button>
       </a>
   
   {% endblock content %}
   ```
### Add 4 views to view the added objects in XML, JSON, XML by ID, and JSON by ID formats.

1.  Import ```HttpResponse``` and ```Serializer``` in ```views.py``` in the ```main``` directory.
   ```
   from django.http import HttpResponse
   from django.core import serializers
   ```
2. Create a few functions that receives a parameter ```request``` that stores the result of the query in XML, JSON, and both by IDs.
   ```
   def show_xml(request):
    data = Product.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

   def show_json(request):
       data = Product.objects.all()
       return HttpResponse(serializers.serialize("json", data), content_type="application/json")
   
   def show_xml_by_id(request, id):
       data = Product.objects.filter(pk=id)
       return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")
   
   def show_json_by_id(request, id):
       data = Product.objects.filter(pk=id)
       return HttpResponse(serializers.serialize("json", data), content_type="application/json")
   ```
### Create URL routing for each of the views added in point 2.
1. Add the URLs in ```urls.py``` file in the ```main``` directory by importing the functions.
   ```
   from main.views import show_main, create_product, show_xml, show_json, show_xml_by_id, show_json_by_id
   ```
2. Add the URL paths to ```urlpatterns```.
   ```
   urlpatterns = [
       ...
       path('xml/', show_xml, name='show_xml'),
       path('json/', show_json, name='show_json'),
       path('xml/<str:id>/', show_xml_by_id, name='show_xml_by_id'),
       path('json/<str:id>/', show_json_by_id, name='show_json_by_id'),
   ]
   ```
## Access the four URLs in point 2 using Postman, take screenshots of the results in Postman, and add them to README.md.

1. **XML**
![image](https://github.com/user-attachments/assets/f38b384b-b7a3-4ae3-b00b-f14f2a1b0116)

2. **JSON**
![image](https://github.com/user-attachments/assets/7a365d94-08da-4206-8ea6-ae7d51f0c522)

3. **XML by ID**
![image](https://github.com/user-attachments/assets/6b9488f5-19b8-4ad6-aba3-7a875bf618bb)

4. **JSON by ID**
![image](https://github.com/user-attachments/assets/976b10fd-60bc-445e-b66a-dfd8284c1c01)

# Assignment 4

## What is the difference between ```HttpResponseRedirect()``` and ```redirect()```?
Here are the key differences;
   1. They receive different arguments/parameters. ```HttpResponseRedirect()``` receives a URL as an argument. It will then redirect the user to that link. ```redirect()``` can receive URL, a view name, or an       object. Django will try to resolve the URL for objects. It automatically handles URL generation and redirection.
   2. ```redirect()``` is more convenient since it can handle a variety of arguments and automatically resolves URLs for views or model objects. On the other hand ```HttpResponseRedirect()``` is more manual and requires the complete URL.
   3. ```redirect()``` is used for common cases because it simplifies redirection logic. But ```HttpResponseRedirect()``` is used in more specific cases where you need more control over the response.

## Explain how the ```MoodEntry``` model is linked with ```User```!
To link ```MoodEntry``` model with the ```User``` model in Django, foreign key relationship is typically used.  This allows each ```MoodEntry``` to be associated with a particular user, representing one-to-many relationship, meaning that one user can have many mood entries, but each mood entry only belongs to a single user. We used this method in this particular code;
```user = models.ForeignKey(User, on_delete=models.CASCADE)```

## What is the difference between authentication and authorization, and what happens when a user logs in? Explain how Django implements these two concepts.
By definition, these two can be defines as such;
   1. **Authentication** is the process of verifying the identity of a user. It ensures that the person trying to access a system is who they claim to be.
   2. **Authorization** determines what an authenticated user is allowed to do within the system. It manages permissions and access controls, specifying what resources the user they can interact with and which actions they can perform.
<br> When a user logs in, here are the differences;
   1. **Authentication**
        <br> The user provides credentials, such as username and password. The system or Django in this case checks the credentials on the stored user information in the database. If the credentials match, then Django           will authenticate the user and sets a session that tracks the user's state (logged in) across requests.

   2. **Authorization**
         <br> After authentication, Django will check the permissions that the users have been assigned to. Depending on the permissions (whether group or user-specific permissions), Django will determine what views,             actions, and resources the user can access.  If the user accesses a resource they are not authorized for, Django can return a '403 Forbidden' response or redirect them to a login page.
Django implements authentication and authorization by providing a built-in authentication framework. We use a User model and other modules, such as login, logout, etc. We can import these by;
```from django.contrib.auth.models import User
   from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
   from django.contrib.auth import authenticate, login, logout
   from django.contrib.auth.decorators import login_required
```
## How does Django remember logged-in users? Explain other uses of cookies and whether all cookies are safe to use.
Django uses sessions and cookies to remember logged-in users across multiple requests. Here is the process:
   1. **Session Framework**
      <br> When a user logs in, Django creates a session for that user. This session stores information about the user, such as ID, on the server.
   2. **Cookies**
      <br> The session ID is stored in a cookie. Every time the user makes a new request, the browser sends this session ID cookie to the server, allowing Django to retrieve the corresponding session data and identify the logged-in user.
<br> Here are other uses of cookies;
   1. Session Management : It is used to store session IDs to keep track of user sessions.
   2. Persistent Login : It can be used for a "Remember Me" feature that stores login information so users don't have to log in repeatedly. This is done by storing a token in a cookie that allows the system to recognize the user even after closing the browser.
   3. User Prefences : It can also be used to save user's preferences such as themes, language, or region, so the application remembers these choices across visits.
<br> Not all cookies are safe, there are potential security risks depending on how the cookie is used. Here are the examples;
   1. Session Hijacking
   2. Cross-Site Scripting (XSS)
   3. Cross-Site Request Forgery

## Explain how did you implement the checklist step-by-step (apart from following the tutorial).
### Implementing Function and Registration Forms
1. Import ```UserCreationForm``` and ```messages``` in ```views.py``` by;
   ```from django.contrib.auth.forms import UserCreationForm
      from django.contrib import messages
   ```
2. Add the ```register``` function to ```views.py```
   ```def register(request):
          form = UserCreationForm()
      
          if request.method == "POST":
              form = UserCreationForm(request.POST)
              if form.is_valid():
                  form.save()
                  messages.success(request, 'Your account has been successfully created!')
                  return redirect('main:login')
          context = {'form':form}
          return render(request, 'register.html', context)
   ```
3. Create a new HTML file named ```register.html``` and fill it with the following code;
   ```{% extends 'base.html' %} {% block meta %}
      <title>Register</title>
      {% endblock meta %} {% block content %}
      
      <div class="login">
        <h1>Register</h1>
      
        <form method="POST">
          {% csrf_token %}
          <table>
            {{ form.as_table }}
            <tr>
              <td></td>
              <td><input type="submit" name="submit" value="Register" /></td>
            </tr>
          </table>
        </form>
      
        {% if messages %}
        <ul>
          {% for message in messages %}
          <li>{{ message }}</li>
          {% endfor %}
        </ul>
        {% endif %}
      </div>
      
      {% endblock content %}
   ```
4. Import the ```register``` function in ```urls.py```
   ```from main.views import register```
5. Add a URL path for ```register``` function to ```urlpatterns```
   ``` urlpatterns = [
           ...
           path('register/', register, name='register'),
       ]
   ```
### Implementing a Login Function
1. Import ```authenticate```, ```login```, and ```AuthenticationForm``` in ```views.py```
   ```from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
      from django.contrib.auth import authenticate, login
   ```
2. Add the ```login_user``` function into ```views.py``` with the following code;
   ```def login_user(request):
         if request.method == 'POST':
            form = AuthenticationForm(data=request.POST)
      
            if form.is_valid():
                  user = form.get_user()
                  login(request, user)
                  return redirect('main:show_main')
      
         else:
            form = AuthenticationForm(request)
         context = {'form': form}
         return render(request, 'login.html', context)
   ```
3. Create a new HTML file named ```login.html``` and fill it with the following code;
   ```{% extends 'base.html' %}

      {% block meta %}
      <title>Login</title>
      {% endblock meta %}
      
      {% block content %}
      <div class="login">
        <h1>Login</h1>
      
        <form method="POST" action="">
          {% csrf_token %}
          <table>
            {{ form.as_table }}
            <tr>
              <td></td>
              <td><input class="btn login_btn" type="submit" value="Login" /></td>
            </tr>
          </table>
        </form>
      
        {% if messages %}
        <ul>
          {% for message in messages %}
          <li>{{ message }}</li>
          {% endfor %}
        </ul>
        {% endif %} Don't have an account yet?
        <a href="{% url 'main:register' %}">Register Now</a>
      </div>
      
      {% endblock content %}
   ```
   4. Import ```login_user``` function to ```urls.py```
      ```from main.views import login_user```
   5. Add the URL path to ```urlpatterns```
      ```urlpatterns = [
            ...
            path('login/', login_user, name='login'),
         ]
      ```
### Implementing a Logout Function
1. Import ```logout``` in ```views.py```
2. Add the ```logout``` function to ```views.py```
   ```def logout_user(request):
          logout(request)
          return redirect('main:login')
   ```
3. Add the following code under "Add Product" with the following code;
   ```...
      <a href="{% url 'main:logout' %}">
        <button>Logout</button>
      </a>
      ...
   ```
4. Import ```logout_user``` to ```urls.py```
   ```from main.views import logout_user```
5. Add the URL path to ```urlpatterns```
   ```urlpatterns = [
         ...
         path('logout/', logout_user, name='logout'),
      ]
   ```
### Restricting Access to the Main Page
1. Import ```login_required``` in ```views.py```
   ```from django.contrib.auth.decorators import login_required```
2. Add the code snippet ```@login_required(login_url='/login')``` above the ```show_main``` function.
   ```...
      @login_required(login_url='/login')
      def show_main(request):
      ...
   ```
### Using Data from Cookies
1. Import ```HttpResponseRedirect```, ```reverse```, and ```datetime``` in ```views.py```
2. Add cookie functionality in the ```login_user``` function
   ```...
      if form.is_valid():
          user = form.get_user()
          login(request, user)
          response = HttpResponseRedirect(reverse("main:show_main"))
          response.set_cookie('last_login', str(datetime.datetime.now()))
          return response
      ...
   ```
3. Add ```last_login``` to ```context``` in ```show_main``` function
   ```context = {
          'name': 'Pak Bepe',
          'class': 'PBP D',
          'npm': '2306123456',
          'mood_entries': mood_entries,
          'last_login': request.COOKIES['last_login'],
      }
   ```
4. Modify the ```logout_user``` as such;
   ```def logout_user(request):
          logout(request)
          response = HttpResponseRedirect(reverse('main:login'))
          response.delete_cookie('last_login')
          return response
   ```
5. Add this code to ```main.html``` to display the ```last login``` data.
   ```...
      <h5>Last login session: {{ last_login }}</h5>
      ...
   ```
### Connecting the ```Product``` model to the User model
1. Import User in ```models.py```
   ```...
      from django.contrib.auth.models import User
      ...
   ```
2. Add the following code to ```Product``` model, to the following code;
   ```class MoodEntry(models.Model):
          user = models.ForeignKey(User, on_delete=models.CASCADE)
          ...
   ```
3. Modify ```create_product``` function in ```views.py``` as follows;
   ```def create_mood_entry(request):
          form = MoodEntryForm(request.POST or None)
      
          if form.is_valid() and request.method == "POST":
              mood_entry = form.save(commit=False)
              mood_entry.user = request.user
              mood_entry.save()
              return redirect('main:show_main')
      
          context = {'form': form}
          return render(request, "create_mood_entry.html", context)
       ...
   ```
4. Modify ```mood_entries``` and ```context``` in ```show_main``` as follows;
   ```def show_main(request):
          mood_entries = MoodEntry.objects.filter(user=request.user)
      
          context = {
               'name': request.user.username,
               ...
          }
      ...
   ```
5. Do migrations with;
   ```python manage.py makemigrations```
   ```python manage.py migrate```
6. Add another import statement in settings.py in the mental_health_tracker subdirectory
   ```import os```
7. Then, change ```DEBUG``` in ```settings.py```
   ```PRODUCTION = os.getenv("PRODUCTION", False)
      DEBUG = not PRODUCTION
   ```

   

