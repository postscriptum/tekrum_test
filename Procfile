release: python manage.py migrate
release: python manage.py loaddata products.json
web: gunicorn my_project.wsgi --log-file -
