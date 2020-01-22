import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SECRET_KEY = ''

ALLOWED_HOSTS = []

# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': '',
        'USER': '',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '',
    }
}

from .settings import INSTALLED_APPS
INSTALLED_APPS +=['item', 'solutions_page', 'process_page', 'project_page', 'aboutus_page', 'contact_page']


SEND_ACTIVATION_EMAIL = True
ACCOUNT_ACTIVATION_DAYS = 30
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = ''
EMAIL_HOST_PASSWORD = ''

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/

STATIC_URL = '/static/'
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
# uncomment below in development
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static"),
]

# use in deployment
# STATIC_ROOT = os.path.join(BASE_DIR, 'static')
