# OTA Insight - Technical Interview

This is the code for the Technical Interview Process of Alejandro Álvarez Pavón.

## Installation

Create a new Python 3 virtual enviroment and istall the requirements using pip:

```bash
pip install -r requiremens.txt 
```

Activate the virtual enviroment and run the migrations to create a sqlite3 database to test the application.

```bash
python manage.py migrate
```

## Usage

Create a superuser with:

```bash
python manage.py createsuperuser
```

Run the application with django runserver:

```bash
python manage.py runserver 0.0.0.0:8000
```

Now you can navigate through the admin panel and create users, currencies and invoices.

API urls are under "/api". To consult the unpaid invoices of a user access "/api/users/<user_id>/unpaid_invoices"