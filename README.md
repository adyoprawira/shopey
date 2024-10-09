# Dropdown Link  
Assignment 6 https://github.com/adyoprawira/shopey/edit/main/README.md#assignment-6

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
```csrf_token``` is used to protect forms from CSRF (Cross-Site Request Forgery) attacks. CSRF occurs when an attacker tricks a user into unknowingly submitting a form or making a request on a website where they are authenticated, potentially leading to unauthorized actions such as changing account details or making transactions. The ```csrf_token``` acts as a security token that ensures the form submission is coming from the legitimate source (the same domain) and not from an external malicious site. It is unique and included in forms, which the server verifies when the form is submitted. If the token is missing or invalid, Django rejects the request, preventing unauthorized form submissions. If a Django form doesn't use ```csrf_token```, then it would be vulnerable to CSRF attacks. This means that an attacker could create a form that mimics legitimate actions such as;
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

# Assignment 5
## If there are multiple CSS selectors for an HTML element, explain the priority order of these CSS selectors!
There are 4 selectors that we can use in CSS. Those are inline styles, ID selectors, classes selectors, and element selectors. The order of priority are;
1. Inline styles
2. ID selectors
3. Classes selector
4. Element selector

## Why does responsive design become an important concept in web application development? Give examples of applications that have and have not implemented responsive design!
A responsive web application ensures that it provides an optimal viewing experience across devices, from desktops to mobile phones. With increasing use of mobile devices, it is important to implement responsive design in making a successful web applications. Examples of applications that have not implemented responsive design are old websites, especially those designed in the early 2000s. These websites are built only for desktop viewing and break down on mobile devices.

## Explain the differences between margin, border, and padding, and how to implement these three things!
1. Margin is the space outside the element. It creates a gap between the element and its neighboring elements.
2. Border is the border that surrounds the padding and content. It creates a visible line around the element.
3. The space inside the element between the content and the border. It creates an inner gap between the content and the element's border.
<br> The content is at the center. The padding surrounds the content. The border surrounds the padding. The margin is the space outside the border, separating this element from others.
<br> Here's an example on how to implement all three things:
```
<div class="box">Hello, world!</div>

<style>
  .box {
    margin: 20px;             /* 20px space outside the element */
    padding: 10px;            /* 10px space inside the element */
    border: 2px solid black;  /* A 2px solid black border around the element */
  }
</style>
```

## Explain the concepts of flex box and grid layout along with their uses!
1. Flexbox: Flexbox is a one-dimensional layout model that arranges items either in a row (horizontally) or in a column (vertically).It is designed to distribute space within a container efficiently, even when the size of the container is unknown or dynamic. The uses of flexbox are one-dimensional elements (single row or column elements), and for responsive layouts that can adjust to different screen sizes by resizing.
2. Grid Layout is a two-dimensional layout system that allows you to define both rows and columns, making it more powerful and flexible for creating complex layouts. The uses of grid layout are for two dimensional layouts (dashboards, web page layouts with headers, sidebars, and footers), complex layouts with precise control over positioning and aligning of elements.

## Explain how you implemented the checklist above step-by-step (not just following the tutorial)!
### Implement functions to delete and edit products.
#### Implementing edit function.
1. Create a new function in ```views.py``` named ```edit_product``` that takes ```request``` and ```id``` as parameter.
   ```
   def edit_product(request, id):
       # Get product entry based on id
       product = Product.objects.get(pk = id)
   
       # Set product entry as an instance of the form
       form = ProductForm(request.POST or None, instance=product)
   
       if form.is_valid() and request.method == "POST":
           # Save form and return to home page
           form.save()
           return HttpResponseRedirect(reverse('main:show_main'))
   
       context = {'form': form}
       return render(request, "edit_product.html", context)
   ```
   
2. Create a new HTML file named ```edit_product.html``` and fill it with:
   ```
   {% extends 'base.html' %}
   {% load static %}
   {% block meta %}
   <title>Edit Product</title>
   {% endblock meta %}
   
   {% block content %}
   {% include 'navbar.html' %}
   <div class="flex flex-col min-h-screen bg-[#040709]">
     <div class="container mx-auto px-4 py-8 mt-16 max-w-xl">
       <h1 class="text-3xl font-bold text-center mb-8 text-white">Edit Product</h1>
     
       <div class="bg-white rounded-lg p-6 form-style">
         <form method="POST" class="space-y-6">
             {% csrf_token %}
             {% for field in form %}
                 <div class="flex flex-col">
                     <label for="{{ field.id_for_label }}" class="mb-2 font-semibold text-gray-700">
                         {{ field.label }}
                     </label>
                     <div class="w-full">
                         {{ field }}
                     </div>
                     {% if field.help_text %}
                         <p class="mt-1 text-sm text-gray-500">{{ field.help_text }}</p>
                     {% endif %}
                     {% for error in field.errors %}
                         <p class="mt-1 text-sm text-red-600">{{ error }}</p>
                     {% endfor %}
                 </div>
             {% endfor %}
             <div class="flex justify-center mt-6">
                 <button type="submit" class="bg-[#0814F1] text-white font-semibold px-6 py-3 rounded-lg hover:bg-[#060FB5] transition duration-300 ease-in-out w-full">
                     Edit Product
                 </button>
             </div>
         </form>
     </div>
     </div>
   </div>
   {% endblock %}
   ```
3. Import ```edit_product``` in ```urls.py```
   ```from main.views import edit_product```
4. Add a URL path to ```urlpatterns```
   ```
   ...
   path('edit-product/<uuid:id>', edit_product, name='edit_product'),
   ...
   ```
5. Edit ```main.html``` with the following code
   ```
   ...
   <tr>
       ...
       <td>
           <a href="{% url 'main:edit_product' product_entry.pk %}">
               <button>
                   Edit
               </button>
           </a>
       </td>
   </tr>
   ...
   ```
#### Implementing delete function
1. Create a new function in ```views.py``` named ```delete_product``` that takes ```request``` and ```id``` as parameter.
   ```
   def delete_product(request, id):
       # Get product based on id
       product = Product.objects.get(pk = id)
       # Delete product
       product.delete()
       # Return to home page
       return HttpResponseRedirect(reverse('main:show_main'))
   ```
2. Import ```delete_product``` in ```urls.py```
   ```from main.views import delete_product```
3. Add a URL path to ```urlpatterns```
   ```
   ...
   path('delete/<uuid:id>', delete_product, name='delete_product'),
   ...
   ```
4. Edit ```main.html``` with the following code
   ```
   ...
   <tr>
       ...
       <td>
           <a href="{% url 'main:edit_mood' mood_entry.pk %}">
               <button>
                   Edit
               </button>
           </a>
       </td>
       <td>
           <a href="{% url 'main:delete_mood' mood_entry.pk %}">
               <button>
                   Delete
               </button>
           </a>
       </td>
   </tr>
   ...
   ```
###  Customize the login, register, and add product pages to be as attractive as possible.
#### Customizing the login page.
1. Create ```login.html```
2. Change the background login page to black
   ```
   {% block content %}
   <div class="min-h-screen flex items-center justify-center w-screen bg-black py-12 px-4 sm:px-6 lg:px-8">
   ...
   ```
3. Change the text color to be visible (white/gray)
   ```
   <h2 class="mt-6 text-center text-white text-3xl font-extrabold text-gray-900">
        Login to your account
   </h2>
   ```
4.  Complete the code
   ```
   {% extends 'base.html' %}

   {% block meta %}
   <title>Login</title>
   {% endblock meta %}
   
   {% block content %}
   <div class="min-h-screen flex items-center justify-center w-screen bg-black py-12 px-4 sm:px-6 lg:px-8">
     <div class="max-w-md w-full space-y-8">
       <div>
         <h2 class="mt-6 text-center text-white text-3xl font-extrabold text-gray-900">
           Login to your account
         </h2>
       </div>
       <form class="mt-8 space-y-6" method="POST" action="">
         {% csrf_token %}
         <input type="hidden" name="remember" value="true">
         <div class="rounded-md shadow-sm -space-y-px">
           <div>
             <label for="username" class="sr-only">Username</label>
             <input id="username" name="username" type="text" required class="appearance-none rounded-none relative block w-full px-3 py-2 border border-gray-300 placeholder-gray-500 text-gray-900 rounded-t-md focus:outline-none focus:ring-gray-200 focus:border-gray-200 focus:z-10 sm:text-sm" placeholder="Username">
           </div>
           <div>
             <label for="password" class="sr-only">Password</label>
             <input id="password" name="password" type="password" required class="appearance-none rounded-none relative block w-full px-3 py-2 border border-gray-300 placeholder-gray-500 text-gray-900 rounded-b-md focus:outline-none focus:ring-gray-200 focus:border-gray-200 focus:z-10 sm:text-sm" placeholder="Password">
           </div>
         </div>
   
         <div>
           <button type="submit" class="group relative w-full flex justify-center py-2 px-4 border border-transparent text-sm font-medium rounded-md text-white bg-[#0814F1] hover:bg-indigo-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-500">
             Sign in
           </button>
         </div>
       </form>
   
       {% if messages %}
       <div class="mt-4">
         {% for message in messages %}
         {% if message.tags == "success" %}
               <div class="bg-green-100 border border-green-400 text-green-700 px-4 py-3 rounded relative" role="alert">
                   <span class="block sm:inline">{{ message }}</span>
               </div>
           {% elif message.tags == "error" %}
               <div class="bg-red-100 border border-red-400 text-red-700 px-4 py-3 rounded relative" role="alert">
                   <span class="block sm:inline">{{ message }}</span>
               </div>
           {% else %}
               <div class="bg-blue-100 border border-blue-400 text-blue-700 px-4 py-3 rounded relative" role="alert">
                   <span class="block sm:inline">{{ message }}</span>
               </div>
           {% endif %}
         {% endfor %}
       </div>
       {% endif %}
   
       <div class="text-center mt-4">
         <p class="text-sm text-gray-200">
           Don't have an account yet?
           <a href="{% url 'main:register' %}" class="font-medium text-indigo-200 hover:text-indigo-300">
               Register Now
           </a>
         </p>
       </div>
     </div>
   </div>
   {% endblock content %}
   ```
#### Customizing the register page.
1. Create ```register.html```
2. Change the background of the register page to black
   ```
   {% block content %}
   <div class="min-h-screen flex items-center justify-center bg-black py-12 px-4 sm:px-6 lg:px-8">
   ```
3. Change the text color to be visible (white/gray)
   ```
   <div>
      <h2 class="mt-6 text-center text-3xl font-extrabold text-gray-200">
        Create your account
      </h2>
   </div>
   ```
4. Complete the code
   ```
   {% extends 'base.html' %}

   {% block meta %}
   <title>Register</title>
   {% endblock meta %}
   
   {% block content %}
   <div class="min-h-screen flex items-center justify-center bg-black py-12 px-4 sm:px-6 lg:px-8">
     <div class="max-w-md w-full space-y-8 form-style">
       <div>
         <h2 class="mt-6 text-center text-3xl font-extrabold text-gray-200">
           Create your account
         </h2>
       </div>
       <form class="mt-8 space-y-6" method="POST">
         {% csrf_token %}
         <input type="hidden" name="remember" value="true">
         <div class="rounded-md shadow-sm -space-y-px">
           {% for field in form %}
             <div class="{% if not forloop.first %}mt-4{% endif %}">
               <label for="{{ field.id_for_label }}" class="mb-2 font-semibold text-gray-200">
                 {{ field.label }}
               </label>
               <div class="relative">
                 {{ field }}
                 <div class="absolute inset-y-0 right-0 pr-3 flex items-center pointer-events-none">
                   {% if field.errors %}
                     <svg class="h-5 w-5 text-red-500" fill="currentColor" viewBox="0 0 20 20">
                       <path fill-rule="evenodd" d="M18 10a8 8 0 11-16 0 8 8 0 0116 0zm-7 4a1 1 0 11-2 0 1 1 0 012 0zm-1-9a1 1 0 00-1 1v4a1 1 0 102 0V6a1 1 0 00-1-1z" clip-rule="evenodd" />
                     </svg>
                   {% endif %}
                 </div>
               </div>
               {% if field.errors %}
                 {% for error in field.errors %}
                   <p class="mt-1 text-sm text-red-600">{{ error }}</p>
                 {% endfor %}
               {% endif %}
             </div>
           {% endfor %}
         </div>
   
         <div>
           <button type="submit" class="group relative w-full flex justify-center py-2 px-4 border border-transparent text-sm font-medium rounded-md text-white bg-[#0814F1] hover:bg-indigo-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-500">
             Register
           </button>
         </div>
       </form>
   
       {% if messages %}
       <div class="mt-4">
         {% for message in messages %}
         <div class="bg-red-100 border border-red-400 text-red-700 px-4 py-3 rounded relative" role="alert">
           <span class="block sm:inline">{{ message }}</span>
         </div>
         {% endfor %}
       </div>
       {% endif %}
   
       <div class="text-center mt-4">
         <p class="text-sm text-gray-200">
           Already have an account?
           <a href="{% url 'main:login' %}" class="font-medium text-indigo-200 hover:text-indigo-300">
             Login here
           </a>
         </p>
       </div>
     </div>
   </div>
   {% endblock content %}
   ```
#### Customizing the product list page.
1. Change the background color
2. Change some positioning of buttons
3. Change button and hover colors

### If there are no products saved in the application, the product list page will display an image and a message that no products are registered.
Add this code to ```main.html```
   ```
   {% if not product_entries %}
       <div class="flex flex-col items-center justify-center min-h-[24rem] p-6">
         <img src="{% static 'image/very-sad.jpg' %}" alt="Sad face" class="w-128 h-64 mb-4"/>
         <p class="text-center text-gray-600 mt-4">There is no product in Shopey.</p>
       </div>
   ...
   ```
###  If there are products saved, the product list page will display details of each product using cards (must not be exactly the same as the design in the Tutorial!).
Add this code to ```main.html``` below the if that was previously created.
   ```
   {% else %}
       <div class="columns-1 sm:columns-2 lg:columns-3 gap-6 space-y-6 w-full">
         {% for product in product_entries %}
           {% include 'card_product.html' with product=product %}
         {% endfor %}
       </div>
   {% endif %}
   ```
###  For each product card, create two buttons to edit and delete the product on that card!
Add this code to ```card_product.html```
   ```
   <div class="absolute top-10 right-5 flex space-x-1">
    <a href="{% url 'main:edit_product' product.pk %}" class="bg-[#0814F1] hover:bg-[#060FB5] text-white rounded-full p-2 transition duration-300 shadow-md">
      <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5" viewBox="0 0 20 20" fill="currentColor">
        <path d="M13.586 3.586a2 2 0 112.828 2.828l-.793.793-2.828-2.828.793-.793zM11.379 5.793L3 14.172V17h2.828l8.38-8.379-2.83-2.828z" />
      </svg>
    </a>
    <a href="{% url 'main:delete_product' product.pk %}" class="bg-red-500 hover:bg-red-600 text-white rounded-full p-2 transition duration-300 shadow-md">
      <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5" viewBox="0 0 20 20" fill="currentColor">
        <path fill-rule="evenodd" d="M9 2a1 1 0 00-.894.553L7.382 4H4a1 1 0 000 2v10a2 2 0 002 2h8a2 2 0 002-2V6a1 1 0 100-2h-3.382l-.724-1.447A1 1 0 0011 2H9zM7 8a1 1 0 012 0v6a1 1 0 11-2 0V8zm5-1a1 1 0 00-1 1v6a1 1 0 102 0V8a1 1 0 00-1-1z" clip-rule="evenodd" />
      </svg>
    </a>
  </div>
   ```
### Create a navigation bar (navbar) for the features in the application that is responsive to different device sizes, especially mobile and desktop.
1. Create ```navbar.html```
2. To make it responsive to different device sizes, use two different sections and use flex.
   ```
   <!-- Desktop Menu (Visible on large screens) -->
            <div class="hidden md:flex items-center space-x-6">

   <!-- Mobile Menu (Hidden by default) -->
    <div class="mobile-menu hidden md:hidden px-4 w-full bg-[#8B008B]">
   ```
3. Add buttons on the navbar by adding
   ```
   <div class="hidden md:flex items-center space-x-6">
                <a href="/" class="text-white px-3 py-2 rounded-md text-sm font-medium hover:bg-[#101010]">Home</a>
                <a href="/" class="text-white px-3 py-2 rounded-md text-sm font-medium hover:bg-[#101010]">Products</a>
                <a href="#" class="text-white px-3 py-2 rounded-md text-sm font-medium hover:bg-[#101010]">Categories</a>
                <a href="#" class="text-white px-3 py-2 rounded-md text-sm font-medium hover:bg-[#101010]">Cart</a>
   ```
# Assignment 6
## Explain the benefits of using JavaScript in developing web applications!

JavaScript is essential in web application development due to its ability to create dynamic, interactive content through real-time DOM manipulation and asynchronous operations, allowing for smoother user experiences without full page reloads. It works across all modern browsers, ensuring cross-platform compatibility, and can be used for both client-side and server-side development with frameworks like React, Angular, and Node.js, enabling full-stack development. JavaScript supports real-time communication with WebSockets, is backed by powerful developer tools for debugging and performance analysis, and benefits from a vast community and rich ecosystem of libraries that accelerate development. Additionally, modern JavaScript engines offer fast execution, and its event-driven architecture is well-suited for responsive interfaces, making it a versatile language for building scalable web applications.

## Explain why we need to use await when we call fetch()! What would happen if we don't use await?

We use ```await``` when calling ```fetch()``` to pause the execution until the promise returned by ```fetch()``` is resolved, allowing us to handle the result immediately. Since ```fetch()``` is asynchronous, without ```await```, the code would continue executing before the data is received, potentially leading to issues like trying to use the response before it's ready. Using ```await``` makes the code easier to read and ensures that subsequent actions dependent on the fetched data occur only after the network request completes. Without ```await```, you would need to use ```.then()``` to handle the resolved promise, which can make the code more complex.

## Why do we need to use the csrf_exempt decorator on the view used for AJAX POST?

We use the csrf_exempt decorator on views handling AJAX POST requests in Django to disable CSRF protection, which is normally applied to prevent cross-site request forgery attacks. AJAX requests may not always include the necessary CSRF token in the headers, especially if not properly configured on the client side, causing Django to reject the request. By using csrf_exempt, we bypass this CSRF check for the specific view, allowing the AJAX request to be processed without the token. However, it's important to ensure that this is done in safe scenarios where the risk of CSRF attacks is minimal.

## On this week's tutorial, the user input sanitization is done in the back-end as well. Why can't the sanitization be done just in the front-end?

User input sanitization should not be done solely on the front-end because client-side code can be easily bypassed or manipulated by malicious users. While front-end validation improves user experience by providing immediate feedback, it cannot be trusted for security since users can disable JavaScript, alter the code, or send requests directly to the server using tools like cURL or Postman. Therefore, back-end sanitization is essential to ensure that any input reaching the server is properly validated and sanitized, protecting the application from attacks such as SQL injection, cross-site scripting (XSS), and other security vulnerabilities.

## Explain how you implemented the checklist above step-by-step (not just following the tutorial)!
### Modify the codes in data cards to able to use AJAX GET.
1. Remove two lines in ```views.py```
   ```
   product_entries = Product.objects.filter(user=request.user)
   ```
   and
   ```
   'product_entries': product_entries,
   ```
2. Replace the first line ```show_json``` and ```show_xml``` with;
   ```
   data = Product.objects.filter(user=request.user)
   ```
3. Remove the ```product_entries``` block that display products when empty.
   ```
   ...
    {% if not product_entries %}
        <div class="flex flex-col items-center justify-center min-h-[24rem] p-6">
            <img src="{% static 'image/very-sad.png' %}" alt="Sad face" class="w-32 h-32 mb-4"/>
            <p class="text-center text-gray-600 mt-4">No products yet</p>
        </div>
    {% else %}
        <div class="columns-1 sm:columns-2 lg:columns-3 gap-6 space-y-6 w-full">
            {% for product_entry in product_entries %}
                {% include 'card_product.html' with product_entry=product_entry %}
            {% endfor %}
        </div>
    {% endif %}
   ...
   ```
4. Replace the just removed code with;
   ```
   <div id="product_entry_cards"></div>
   ```
5. Add a <script> block before ```{% endblock content %}``` and create a new function named ```getProductEntries```.
   ```
   <script>
     async function getMoodEntries(){
         return fetch("{% url 'main:show_json' %}").then((res) => res.json())
     }
   </script>
   ```
6.  Add another function in ```<script>``` block named ```refreshProductEntries``` to refresh products data asynchronously.
   ```
   async function refreshProductEntries() {
       document.getElementById("product_entry_cards").innerHTML = "";
       document.getElementById("product_entry_cards").className = "";
       const productEntries = await getProductEntries();
       let htmlString = "";
       let classNameString = "";
   
       if (productEntries.length === 0) {
         classNameString = "flex flex-col items-center justify-center min-h-[24rem] p-6";
         htmlString = `
           <div class="flex flex-col items-center justify-center min-h-[24rem] p-6">
             <img src="{% static 'image/very-sad.png' %}" alt="Sad face" class="w-32 h-32 mb-4"/>
             <p class="text-center text-gray-600 mt-4">No product yet.</p>
           </div>
         `;
       } else {
         classNameString = "columns-1 sm:columns-2 lg:columns-3 gap-6 space-y-6 w-full";
         productEntries.forEach((item) => {
           const name = DOMPurify.sanitize(item.fields.name);
           const description = DOMPurify.sanitize(item.fields.description);
           const category = DOMPurify.sanitize(item.fields.category);
   
           htmlString += `
             <div class="relative break-inside-avoid">
               <div class="relative top-5 bg-indigo-200 shadow-md rounded-lg mb-6 break-inside-avoid flex flex-col border-2 border-gray-700 transform rotate-1 hover:rotate-0 transition-transform duration-300">
                 <div class="bg-black text-gray-200 p-4 rounded-t-lg border-b-2 border-indigo-300">
                   <h3 class="font-bold text-xl mb-2">${name}</h3>
                 </div>
                 <div class="p-4 flex">
                   <!-- Left section with description and price -->
                   <div class="w-2/3">
                     <p class="font-semibold text-lg mb-2">Description</p>
                     <p class="text-gray-700 mb-2">
                       <span class="text-gray-700">${description}</span>
                     </p>
                     <div class="mt-4">
                       <p class="text-gray-700 font-semibold mb-2">Price</p>
                       <div class="relative pt-1">
                         <div class="flex mb-2 items-center justify-between">
                           <div>
                             <span class="text-xs font-semibold inline-block py-1 px-2 uppercase rounded-full text-gray-900 bg-white shadow-lg">
                               ${item.fields.price}
                             </span>
                           </div>
                         </div>
                       </div>
                     </div>
                   </div>
                   <!-- Right section with product image -->
                   <div class="w-1/3">
                     {% if product.image %}
                     <img src="{{ product.image.url }}" alt="{{ product.name }}" class="w-full h-auto rounded-lg shadow-xl">
                     {% else %}
                     <img src="{% static 'image/no_image.webp' %}" alt="No image available" class="w-full h-auto rounded-lg">
                     {% endif %}
                   </div>
                 </div>
               </div>
               <div class="absolute top-10 right-5 flex space-x-1">
                 <a href="/edit-product/${item.pk}" class="bg-[#0814F1] hover:bg-[#060FB5] text-white rounded-full p-2 transition duration-300 shadow-md">
                   <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5" viewBox="0 0 20 20" fill="currentColor">
                     <path d="M13.586 3.586a2 2 0 112.828 2.828l-.793.793-2.828-2.828.793-.793zM11.379 5.793L3 14.172V17h2.828l8.38-8.379-2.83-2.828z" />
                   </svg>
                 </a>
                 <a href="/delete/${item.pk}" class="bg-red-500 hover:bg-red-600 text-white rounded-full p-2 transition duration-300 shadow-md">
                   <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5" viewBox="0 0 20 20" fill="currentColor">
                     <path fill-rule="evenodd" d="M9 2a1 1 0 00-.894.553L7.382 4H4a1 1 0 000 2v10a2 2 0 002 2h8a2 2 0 002-2V6a1 1 0 100-2h-3.382l-.724-1.447A1 1 0 0011 2H9zM7 8a1 1 0 012 0v6a1 1 0 11-2 0V8zm5-1a1 1 0 00-1 1v6a1 1 0 102 0V8a1 1 0 00-1-1z" clip-rule="evenodd" />
                   </svg>
                 </a>
               </div>
             </div>
           `;
         });
       }
   ```
### Create a button that opens a modal with a form for adding a mood entry.
1. Add this code to implement the Tailwind modal below the ```div``` with the ```id``` ```product_entry_cards``` that have been added previously.
   ```
         <div id="crudModal" tabindex="-1" aria-hidden="true" class="hidden fixed inset-0 z-50 w-full flex items-center justify-center bg-gray-800 bg-opacity-50 overflow-x-hidden overflow-y-auto transition-opacity duration-300 ease-out">
          <div id="crudModalContent" class="relative bg-white rounded-lg shadow-lg w-5/6 sm:w-3/4 md:w-1/2 lg:w-1/3 mx-4 sm:mx-0 transform scale-95 opacity-0 transition-transform transition-opacity duration-300 ease-out">
            <!-- Modal header -->
            <div class="flex items-center justify-between p-4 border-b rounded-t">
              <h3 class="text-xl font-semibold text-gray-900">
                Add Product
              </h3>
              <button type="button" class="text-gray-400 bg-transparent hover:bg-gray-200 hover:text-gray-900 rounded-lg text-sm p-1.5 ml-auto inline-flex items-center" id="closeModalBtn">
                <svg aria-hidden="true" class="w-5 h-5" fill="currentColor" viewBox="0 0 20 20" xmlns="http://www.w3.org/2000/svg">
                  <path fill-rule="evenodd" d="M4.293 4.293a1 1 0 011.414 0L10 8.586l4.293-4.293a1 1 0 111.414 1.414L11.414 10l4.293 4.293a1 1 0 01-1.414 1.414L10 11.414l-4.293 4.293a1 1 0 01-1.414-1.414L8.586 10 4.293 5.707a1 1 0 010-1.414z" clip-rule="evenodd"></path>
                </svg>
                <span class="sr-only">Close modal</span>
              </button>
            </div>
            <!-- Modal body -->
            <div class="px-6 py-4 space-y-6 form-style">
              <form id="productEntryForm">
                <div class="mb-4">
                  <label for="name" class="block text-sm font-medium text-gray-700">Name</label>
                  <input type="text" id="name" name="name" class="mt-1 block w-full border border-gray-300 rounded-md p-2 hover:border-indigo-700" placeholder="Enter your product" required>
                </div>
                <div class="mb-4">
                  <label for="description" class="block text-sm font-medium text-gray-700">Description</label>
                  <textarea id="description" name="description" rows="3" class="mt-1 block w-full h-52 resize-none border border-gray-300 rounded-md p-2 hover:border-indigo-700" placeholder="Describe your product" required></textarea>
                </div>
                <div class="mb-4">
                  <label for="price" class="block text-sm font-medium text-gray-700">Price</label>
                  <input type="number" id="price" name="price" class="mt-1 block w-full border border-gray-300 rounded-md p-2 hover:border-indigo-700" required>
                </div>
                <div class="mb-4">
                  <label for="category" class="block text-sm font-medium text-gray-700">Category</label>
                  <select id="category" name="category" class="mt-1 block w-full border border-gray-300 rounded-md p-2 hover:border-indigo-700" required>
                    <option value="" disabled selected>Select a category</option>
                    <option value="electronics">Electronics</option>
                    <option value="fashion">Fashion</option>
                    <option value="home">Home</option>
                    <option value="beauty">Beauty</option>
                    <option value="sports">Sports</option>
                    <option value="toys">Toys</option>
                  </select>
                </div>
              </form>
            </div>
            <!-- Modal footer -->
            <div class="flex flex-col space-y-2 md:flex-row md:space-y-0 md:space-x-2 p-6 border-t border-gray-200 rounded-b justify-center md:justify-end">
              <button type="button" class="bg-gray-500 hover:bg-gray-600 text-white font-bold py-2 px-4 rounded-lg" id="cancelButton">Cancel</button>
              <button type="submit" id="submitProductEntry" form="productEntryForm" class="bg-indigo-700 hover:bg-indigo-600 text-white font-bold py-2 px-4 rounded-lg">Save</button>
            </div>
          </div>
        </div>
      </div>
   ```
2. Add the following JavaScript functions to make the modal work.
   ```
   <script>
   ...
     const modal = document.getElementById('crudModal');
     const modalContent = document.getElementById('crudModalContent');
   
     function showModal() {
         const modal = document.getElementById('crudModal');
         const modalContent = document.getElementById('crudModalContent');
   
         modal.classList.remove('hidden'); 
         setTimeout(() => {
           modalContent.classList.remove('opacity-0', 'scale-95');
           modalContent.classList.add('opacity-100', 'scale-100');
         }, 50); 
     }
   
     function hideModal() {
         const modal = document.getElementById('crudModal');
         const modalContent = document.getElementById('crudModalContent');
   
         modalContent.classList.remove('opacity-100', 'scale-100');
         modalContent.classList.add('opacity-0', 'scale-95');
   
         setTimeout(() => {
           modal.classList.add('hidden');
         }, 150); 
     }
   
     document.getElementById("cancelButton").addEventListener("click", hideModal);
     document.getElementById("closeModalBtn").addEventListener("click", hideModal);
   ...
   </script>
   ```
3. Add a button to perform data addition with AJAX
   ```
      <button data-modal-target="crudModal" data-modal-toggle="crudModal" class="btn bg-indigo-700 hover:bg-indigo-600 text-white font-bold py-2 px-4 rounded-lg transition duration-300 ease-in-out transform hover:-translate-y-1 hover:scale-105" onclick="showModal();">
         Add New Product by AJAX
       </button>
   ```
### Create a new view function to add a new mood entry to the database.
1. Import ```csrf_exempt``` and ```require_POST``` to ```views.py```
   ```
   from django.views.decorators.csrf import csrf_exempt
   from django.views.decorators.http import require_POST
   ```
2. Add a new function in ```views.py``` named ```add_product_entry_ajax```
   ```
   ...
   @csrf_exempt
   @require_POST
   def add_product_entry_ajax(request):
       name = strip_tags(request.POST.get("name"))
       description = strip_tags(request.POST.get("description"))
       price = strip_tags(request.POST.get("price"))
       category = strip_tags(request.POST.get("category"))
       user = request.user
   
       new_product = Product(
           name=name,
           description=description,
           price=price,
           user=user,
           category=category,
       )
       new_product.save()
   
       return HttpResponse(b"CREATED", status=201)
   ...
   ```
### Create a /create-ajax/ path that routes to the new view function you created.

1. Import the URL in ```urls.py```
   ```
   from main.views import ..., add_product_entry_ajax
   ```
2. Add the URL path to ```urlpatterns```
   ```
   urlpatterns = [
    ...
    path('create-product-entry-ajax', add_product_entry_ajax, name='add_product_entry_ajax'),
   ]
   ```
### Connect the form you created inside the modal to the /create-ajax/ path.
1. Add a new function in ```<script>``` named ```addProductEntry```.
   ```
   function addProductEntry() {
       const form = document.querySelector('#productEntryForm'); // Define the form variable
       const formProduct = new FormData(form);
   
       fetch("{% url 'main:add_product_entry_ajax' %}", {
         method: "POST",
         body: formProduct,
       })
       .then(response => {
         if (response.ok) {
           refreshProductEntries();
           form.reset();
         } else {
           alert('Failed to add product.');
         }
       })
       .catch(error => {
         console.error('Error:', error);
         alert('An error occurred.');
       });
   
       return false;
     }
   ```
2. Add an event listener to the form in the modal to run the ```addProductEntry()``` function with the following code.
   ```
   document.getElementById("productEntryForm").addEventListener("submit", (e) => {
       e.preventDefault();
       addProductEntry();
       hideModal();
   ```
   
