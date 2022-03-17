"""Gunicorn *development* config file"""
# file from https://realpython.com/django-nginx-gunicorn/#replacing-wsgiserver-with-gunicorn
from multiprocessing import cpu_count


def max_workers():
    return cpu_count()


# Django WSGI application path in pattern MODULE_NAME:VARIABLE_NAME
wsgi_app = "django_celery_redis_boilerplate.wsgi:application"
# request handling workers
workers = max_workers()
# The socket to bind
bind = "0.0.0.0:8000"
# Restart workers when code changes (development only!)
reload = True
# Daemonize the Gunicorn process (detach & enter background)
# daemon = True
