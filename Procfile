release: sh -c 'python manage.py migrate && python manage.py loaddata */fixtures/*.json'
web: gunicorn project_django.wsgi --log-file -