from .base import *

DEBUG = False

ADMINS = (
    ('nyrag', 'nyrag1993@gmail.com'),
)

ALLOWED_HOSTS = ['*']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'mylearn',
        'USER': 'mylearn',
        'PASSWORD': 'mylearn',
    }
}
