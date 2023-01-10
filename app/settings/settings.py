from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.

BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-#&%k9ghvo!@#$%^kirm8!12su%w5!c8a@kijyz$957doifq2+)ga%4o5w'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'currency',
    'accounts',
    'django_extensions',
    'rest_framework',
    'API',


]

MIDDLEWARE = [

    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'currency.middleware.RateTimeMiddleware',
    'currency.middleware.GclidMiddleware',
    'currency.middleware.AdMiddleware',

]

ROOT_URLCONF = 'settings.urls'

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

WSGI_APPLICATION = 'settings.wsgi.application'

# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Europe/Kiev'

USE_I18N = True

USE_TZ = False

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

INTERNAL_IPS = [
    "127.0.0.1",
]

# DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
# EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
# # EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"
# EMAIL_HOST = "smtp.gmail.com"
# EMAIL_USE_TLS = True
#
# EMAIL_PORT = 587
# # http - 80
# # https - 443
# # smtp - 587
#
# EMAIL_HOST_USER = "879846test@gmail.com"
# EMAIL_HOST_PASSWORD = "lqglrhauktgpzdry"
# # EMAIL_HOST_PASSWORD = "246813579qwerty__"
# SUPPORT_EMAIL = "879846test@gmail.com"

AUTH_USER_MODEL = "accounts.User"

from django.urls import reverse_lazy

LOGIN_REDIRECT_URL = reverse_lazy('index-link')
LOGOUT_REDIRECT_URL = reverse_lazy('index-link')

HTTP_SCHEMA = 'http'
DOMAIN = "localhost:8000"

CELERY_BROKER_URL = 'amqp://localhost'

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
EMAIL_HOST = "smtp.gmail.com"
EMAIL_PORT = 587
EMAIL_HOST_USER = "879846test@gmail.com"
EMAIL_HOST_PASSWORD = "lqglrhauktgpzdry"
EMAIL_USE_TLS = True

from celery.schedules import crontab

CELERY_BEAT_SCHEDULE = {
    "debug": {
        "task": "currency.tasks.minfin_parse",
        "schedule": crontab(minute="*/1")
    },
    # "debug1": {
    #     "task": "currency.tasks.send_mail",
    #     "schedule": crontab(minute="*/1")
    # }
}
