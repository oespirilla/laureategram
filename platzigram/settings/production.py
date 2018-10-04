import os

from .base import *


DEBUG = True
# A different Database for production
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases


DATABASES = {
    'default': {
        'NAME': 'laureategram',
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'HOST': 'YOUR_HOST',
        'USER': 'YOUR_USER',
        'PASSWORD': 'YOUR_PASSWORD',    
    }
}