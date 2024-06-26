"""
Django settings for reflekt_io project.

Generated by 'django-admin startproject' using Django 3.2.8.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""

import os
from pathlib import Path
import environ

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

env = environ.Env(
    DEBUG=(bool, False)
)

# Set the project base directory
# BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Take environment variables from .env file
environ.Env.read_env()

# Quick-start development settings
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/
# for best-practices.

# SECURITY WARNING: keep the secret key used in production secret!
# Please set SECRET_KEY environment variable in your production environment
# (e.g. Heroku).
SECRET_KEY = env.str('SECRET_KEY', 'django-insecure-)&n4fpdxxruqo49e!gn^^bvr9k726ldxx6k$wwpf)(e(%orpz9')

# Automatically determine environment by detecting if DATABASE_URL variable.
# DATABASE_URL is provided by Heroku if a database add-on is added
# (e.g. Heroku Postgres).
DB_HOST = env.bool('DB_HOST', False)

# SECURITY WARNING: don't run with debug turned on in production!
# If you want to enable debugging on Heroku for learning purposes,
# set this to True.

DEBUG = env.bool('DEBUG', True)

APP_NAME = env.str('APP_NAME', '')

ALLOWED_HOSTS = ['*']

# if PRODUCTION:
#     ALLOWED_HOSTS += [f'{APP_NAME}.pbp.cs.ui.ac.id']
# else:
#     ALLOWED_HOSTS += ['.localhost', '127.0.0.1', '[::1]']

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'corsheaders',
    'main',
    'journal',
    'pojok_curhat',
    'tembok_harapan',
    'kutipan_penyemangat',
    'deteksi_depresi',
    'refleksi',
    'about_us',
]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'corsheaders.middleware.CorsMiddleware',
]

CORS_ALLOW_ALL_ORIGINS = True
CORS_ORIGIN_ALLOW_ALL = True
CORS_ALLOW_CREDENTIALS = True
CORS_ALLOW_METHODS = [
    'GET',
    'POST',
]

CSRF_COOKIE_SECURE = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SAMESITE = 'None'
SESSION_COOKIE_SAMESITE = 'None'

ROOT_URLCONF = 'reflekt_io.urls'

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

WSGI_APPLICATION = 'reflekt_io.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }

# # Set database settings automatically using DATABASE_URL.
# if DB_HOST:
#     DATABASES = {
#         'default': {
#             'ENGINE': 'django.db.backends.postgresql_psycopg2',
#             'NAME': env("DB_NAME"),
#             'USER': env("DB_USER"),
#             'PASSWORD': env("DB_PASSWORD"),
#             'HOST': env("DB_HOST"),
#             'PORT': env("DB_PORT"),
#         }
#     }
#     DATABASES["default"]["ATOMIC_REQUESTS"] = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': env("DB_NAME"),
        'USER': env("DB_USER"),
        'PASSWORD': env("DB_PASSWORD"),
        'HOST': env("DB_HOST"),
        'PORT': env("DB_PORT"),
    }
}
DATABASES["default"]["ATOMIC_REQUESTS"] = True

# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.2/topics/i18n/
# Feel free to change these according to your needs.

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Jakarta'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'

# This is the directory for storing `collectstatic` results.
# This shouldn't be included in your Git repository.
STATIC_ROOT = os.path.join(BASE_DIR, 'static')

# You can use this directory to store project-wide static files.
# STATICFILES_DIRS = [
#     BASE_DIR / 'static',
# ]

# Make sure the directories exist to prevent errors when doing `collectstatic`.
# for directory in [*STATICFILES_DIRS, STATIC_ROOT]:
#     directory.mkdir(exist_ok=True)

# Enable compression and caching features of whitenoise.
# You can remove this if it causes problems on your setup.
STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.StaticFilesStorage'
