# Emerald Shopper
Simple todo/shopping list in Django

## How install
The instructions below assumes you're already familiar with Python/Django

1. Download and clone this project's repository
2. Create a new virtual environment and activate it (Tested with Python 3.8, but should work with any newer version of Python 3)
3. Navigate to the project directory inside your terminal
4. run ``pip install -r requirements.txt`` to install all the project's dependencies
5. Ensure you have a local instance of the database by running:
        ``python manage.py makemigrations`` and
        ``python manage.py migrate``
6. run ``python manage.py runserver`` to run the project & open in the browser
7. run ``python manage.py test`` to run the tests

Have fun creating, editing and deleting items from the shopping list !!
