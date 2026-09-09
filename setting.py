
import os
from decouple import config
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
SECRET_KEY = config('SECRET_KEY', default='django-insecure-change-me')
DEBUG = config('DEBUG', default=True, cast=bool)
ALLOWED_HOSTS = config('ALLOWED_HOSTS', default='localhost,127.0.0.1').split(',')

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # Third-party
    'crispy_forms',
    'crispy_bootstrap5',
    'storages',
    # Local
    'accounts',
    'courses',
    'payments',
    'quizzes',
]

CRISPY_TEMPLATE_PACK = 'bootstrap5'

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'techki_masti.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
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

WSGI_APPLICATION = 'techki_masti.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

AUTH_USER_MODEL = 'accounts.CustomUser'

LOGIN_URL = 'accounts:login'
LOGIN_REDIRECT_URL = 'dashboard'
LOGOUT_REDIRECT_URL = 'index'

# ── Media Files (Videos / PDFs / Images) ──────────────────────
# Local Development
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

# ── Production: AWS S3 (uncomment when deploying) ────────────
# AWS_ACCESS_KEY_ID = config('AWS_ACCESS_KEY_ID')
# AWS_SECRET_ACCESS_KEY = config('AWS_SECRET_ACCESS_KEY')
# AWS_STORAGE_BUCKET_NAME = config('AWS_STORAGE_BUCKET_NAME')
# AWS_S3_REGION_NAME = config('AWS_S3_REGION_NAME', default='ap-south-1')
# AWS_S3_CUSTOM_DOMAIN = f'{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com'
# DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
# MEDIA_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/'

STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / 'static']
STATIC_ROOT = BASE_DIR / 'staticfiles'

# ── Stripe Payment Keys ─────────────────────────────────────
STRIPE_PUBLISHABLE_KEY = config('STRIPE_PUBLISHABLE_KEY', default='')
STRIPE_SECRET_KEY = config('STRIPE_SECRET_KEY', default='')
STRIPE_WEBHOOK_SECRET = config('STRIPE_WEBHOOK_SECRET', default='')

# ── Email (for password reset etc.) ─────────────────────────
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
