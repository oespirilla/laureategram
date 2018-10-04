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

# Static files (CSS, JavaScript, Images)
STATIC_URL = os.environ['STATIC_URL']

# collectstatic directory (located OUTSIDE the base directory)
# TODO: configure the name and path to your static bucket directory (where collectstatic will copy to)
STATIC_ROOT = os.path.join(os.path.dirname(BASE_DIR), 'static')

DEFAULT_FILE_STORAGE = 'storages.backends.gcloud.GoogleCloudStorage'
GS_BUCKET_NAME = os.environ['GS_BUCKET_NAME']
GS_DEFAULT_ACL = 'publicRead'


