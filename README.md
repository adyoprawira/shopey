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
### Upload Project To Github
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
##  Perform routing in the project so that the application main can run
1. Register ```main``` app on the project by adding it to ```INSTALLED_APPS``` on ```settings.py```
   ```
   INSTALLED_APPS = [
      ...,
      'main'
   ]
   ```

   
