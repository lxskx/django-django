import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'blog',
    'pages',
]

TEMPLATES = [
    {
        'DIRS': [BASE_DIR / 'templates'],
        # ...
    },
]

STATICFILES_DIRS = [
    BASE_DIR / 'static_dev',
]
