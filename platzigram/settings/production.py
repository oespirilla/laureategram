import os

from .base import *


DEBUG = os.environ['DEBUG'] == 'True'
# A different Database for production
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases

SECRET_KEY = os.environ['SECRET_KEY']

DATABASES = {
    'default': {
        'NAME': os.environ['DB_NAME'],
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'HOST': os.environ['DB_HOST'],
        'USER': os.environ['DB_USER'],
        'PASSWORD': os.environ['DB_PASSWORD'],
    }
}