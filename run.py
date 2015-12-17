import os
from django.core.management import execute_from_command_line

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "webtest.settings")

def runserver():
    args = ['name', 'runserver', '0.0.0.0:8000']
    execute_from_command_line(args)

def migrate():
    args = ['name', 'migrate']
    execute_from_command_line(args)

if __name__ == "__main__":
    migrate()
    runserver()