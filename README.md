# About
A Platform designed to track different products on the biggest Ecommerce in MENA region Amazon (Souq formerly), Jumia, and noon and match similar products to gather into one product to provide the user with the best price available on the three Ecommerce also providing a price history for every product to discover fake offers. Notifying the user if the price reaches a lower price. 

## Built using:
    - Django
    - Django Rest Framework (DRF)
    - Celery
    - PostgreSQL
    - Scrapy

## How to install Django on Windows?
#### First: Install Python

Django is a Python web framework, thus requiring Python to be installed on your machine. At the time of writing, Python 3.8 is the latest version.

To install Python on your machine go to https://www.python.org/downloads/. The website should offer you a download button for the latest Python version. Download the executable installer and run it. Check the boxes next to “Install launcher for all users (recommended)” then click “Install Now”.

After installation, open the command prompt and check that the Python version matches the version you installed by executing:


> py --version 


#### Second: Setting up a virtual environment
Let’s start by creating a folder for our project.

> mkdir myproject   #creating our project folder

> cd myproject      #changing into our project folder directory

A virtual environment helps create an isolated Python environment that will contain all that packages that our Django project will need. Let’s create a virtual environment named venv.

> pip install virtualenv

> virtualen env

When we activate our virtual environment, any Python packages installed will only be available for our Django project.

To activate the venv virtual environment, run:

> source venv/bin/activate

Let’s install django and psycopg2 using pip. psycopg2 is a popular PostgreSQL database adapter for Python.
> pip install django

> pip install django psycopg2

Let’s create our Django project.

> django-admin startproject projectName .

> django-admin startapp appName

Change your current directory into our Django project django_app.

> cd django_app

Add the app name to the installed apps section of the file.
> ...
INSTALLED_APPS = [
    ...
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'appName',  # registering the appName app
]


Creating a Django App Using PostgreSQL Database


Django is a high-level Python Web framework that encourages rapid development, clean, and pragmatic design. Built by experienced developers, it takes care of much of the hassle of web development, so you can focus on writing your app without needing to reinvent the wheel. Best of all, it’s free and open-source.

PostgreSQL is a powerful, open-source object-relational database system that uses and extends the SQL language combined with many features that safely store and scale the most complicated data workloads.

Prerequisites

#### Third: Creating our database through the command line

> Open the PostgreSQL shell. You can find the PSQL Shell in the Start Menu.

> access psql

The shell will prompt you for Server, Database, Port, and Username details. You can set it to default by clicking on the Enter button in the keyboard without providing any value. Finally, the shell will prompt you for the Password.

You should provide the password that you used during the PostgreSQL installation. You will see a similar result in your PSQL shell like the one the above image if correctly implemented.

> psql_shell

#### forth: Creating a virtual environment & installing necessary Python packages


Set up your project to use PostgreSQL database

SQlite is the default database that comes with Django. We need to change the database configurations to use PostgreSQL.

Let’s navigate to django_app/settings.py. In the DATABASES section, you’ll see the code snippet below.

> DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

Change the above code snippet to this:

> DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'Name',
        'USER': '<yourname>',
        'PASSWORD': 'password',
        'HOST': 'localhost',
        'PORT': '',
    }
}


## Also need to install
    - celery
    - requests 
