"""
Django settings for MissingChild project.
"""

import pymysql
from pathlib import Path

pymysql.install_as_MySQLdb()  # Use PyMySQL instead of MySQLdb

# BASE_DIR using pathlib
BASE_DIR = Path(__file__).resolve().parent.parent

# SECURITY
SECRET_KEY = 'ipl393&tqan0#2u&e*y$y3#lfzi5&fejgd34s&x285#z+!l_*4'
DEBUG = True
ALLOWED_HOSTS = []

# Installed apps
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'MissingChildApp',  # your app
]

# Middleware
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'MissingChild.urls'

# Templates
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'MissingChildApp' / 'templates'],  # app templates
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

WSGI_APPLICATION = 'MissingChild.wsgi.application'

# Database (MySQL)
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'MissingChildDB',
        'USER': 'root',
        'PASSWORD': 'Shivaram,1',
        'HOST': '127.0.0.1',
        'PORT': '3306',
    }
}

# Media files
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'   # ✅ pathlib usage

# Password validation
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# Internationalization
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True

# Static files
STATIC_URL = '/static/'

# Multiple static directories
STATICFILES_DIRS = [
    BASE_DIR / 'static',                       # project-level static
    BASE_DIR / 'MissingChildApp' / 'static',   # app-level static
]

# Optional: static root for collectstatic
# STATIC_ROOT = BASE_DIR / 'staticfiles'
