from . base import *
# SECURITY WARNING: don't run with debug turned on in production!
#hola 1
DEBUG = True

ALLOWED_HOSTS = ['retocumplo.herokuapp.com']


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}