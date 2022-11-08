"""
Django settings for MustardServer project.

Generated by 'django-admin startproject' using Django 4.1.2.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/
"""
import os.path
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-qxoa+ar#vxvbtqix+-)r*zv&8o4uf8)er16#$2=krf!ah301l$'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']

# Application definition

INSTALLED_APPS = [
    'daphne',
    'channels',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'app',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'MustardServer.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'MustardServer.wsgi.application'

# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Internationalization
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

USERNAME_MAX_LENGTH = 25

PASSWORD_MAX_LENGTH = 50

# Sets the minimun password length
PASSWORD_MINIMUM_LENGTH = 6

ASGI_APPLICATION = "MustardServer.asgi.application"

SETTINGS_FILE = "development_settings.txt"

# Default values for the redis service
DEFAULT_REDIS_SERVICE_IP = "127.0.0.1"
DEFAULT_REDIS_SERVICE_PORT = "6379"

# Path for the development settings files
DEVELOPMENT_SETTINGS_FILE = os.path.join(BASE_DIR, 'development_settings.txt')

# Checks if the file does not exist, if it does not, creates it with a default set of values
if not os.path.isfile(DEVELOPMENT_SETTINGS_FILE):
    with open(DEVELOPMENT_SETTINGS_FILE, 'w') as settings_file:
        settings_file.write("REDIS_SERVICE_IP=" + DEFAULT_REDIS_SERVICE_IP + "\n")
        settings_file.write("REDIS_SERVICE_PORT=" + DEFAULT_REDIS_SERVICE_PORT)

# Dictionary to store the settings
settings = {}

# Reads the values from the file
with open(DEVELOPMENT_SETTINGS_FILE, 'r') as settings_file:
    line = settings_file.readline()

    while line != '':
        try:
            # Splits the values using '=' as separator
            values = line.split('=')

            # Stores the value in the dictionary, removes any possible line break char
            settings[values[0]] = values[1].replace('\n', '')

        except IndexError:
            print("Invalid setting skipped")

        # Reads the next line
        line = settings_file.readline()

print("Redis connection: " + settings['REDIS_SERVICE_IP'] + ":" + settings['REDIS_SERVICE_PORT'])

# Redis configuration
CHANNEL_LAYERS = {
    "default": {
        "BACKEND": "channels_redis.core.RedisChannelLayer",
        "CONFIG": {
            "hosts": [(settings['REDIS_SERVICE_IP'], settings['REDIS_SERVICE_PORT'])],
        },
    },
}
