release: python manage.py migrate
web: daphne django_netflix.wsgi:application --port $PORT --bind 0.0.0.0 -v2
worker: python manage.py runworker channels --settings=django_netflix.settings -v2