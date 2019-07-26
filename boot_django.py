# File sets up the django environment, used by other scripts that need to
# execute in django land
import os
import django
from django.conf import settings

YASET_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), 'yaset'))

def boot_django():
    settings.configure(
        BASE_DIR=YASET_DIR,
        DEBUG=True,
        DATABASES={
            'default':{
                'ENGINE':'django.db.backends.sqlite3',
                'NAME': os.path.join(YASET_DIR, 'db.sqlite3'),
            }
        },
        INSTALLED_APPS=(
            'django.contrib.auth',
            'django.contrib.contenttypes',
            'django.contrib.sessions',

            'yaset',
            'yaset.tests',
        ),
    )
    django.setup()
