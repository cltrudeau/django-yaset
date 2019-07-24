# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'ry+vd%uy1j2q6z6i3*%x2df_*%7y*!e1x%r-7()5&rmqt*_y#0'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['localhost', ]


# Application definition

INSTALLED_APPS = (
    'yaset',
)

TIME_ZONE = 'UTC'

from yaset import import_settings

import_settings(globals())
