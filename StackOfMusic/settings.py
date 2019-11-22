"""
Django settings for StackOfMusic project.

Generated by 'django-admin startproject' using Django 2.2.5.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

import os
import json
import djcelery


# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CONFIG_SECRET_DIR = os.path.join(BASE_DIR, 'config/')
CONFIG_SETTINGS_COMMON_FILE = os.path.join(CONFIG_SECRET_DIR, 'settings_common.json')

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'h9e@=*_df72)j3pz$20n!vsgi$_gad6ychvdeiyfw9sb)pdze6'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['localhost', '127.0.0.1', '13.209.15.144']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'accounts.apps.AccountsConfig',
    'instrument.apps.InstrumentConfig',
    'bank.apps.BankConfig',
    'music.apps.MusicConfig',
    'createmusic.apps.CreatemusicConfig',
    'rest_framework',
    'corsheaders',
    'storages',
    's3direct',
    'rest_framework.authtoken',
    'oauth2_provider',
    'djcelery',
    'celery',
    'django_celery_results',
    # 'cachalot',
    # 'debug_toolbar',
]

REST_FRAMEWORK = {
    'DEFAULT_RENDERER_CLASSES': (
        'rest_framework.renderers.JSONRenderer',
        'rest_framework.renderers.BrowsableAPIRenderer',
    ),
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'oauth2_provider.contrib.rest_framework.OAuth2Authentication',
        'rest_framework.authentication.BasicAuthentication',
        'rest_framework.authentication.SessionAuthentication',
    ),
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',
    )

}

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'corsheaders.middleware.CorsPostCsrfMiddleware',
]

ROOT_URLCONF = 'StackOfMusic.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
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

WSGI_APPLICATION = 'StackOfMusic.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'OPTIONS': {
            'read_default_file': os.path.join(CONFIG_SECRET_DIR, 'mysql.cnf'),
            'charset': 'utf8mb4',
        }
    }
}

CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        # "LOCATION": 'redis://54.180.115.149/1',
        "LOCATION": 'redis://127.0.0.1/1',
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
            'PICKLE_VERSION': 2,
        }
    }
}

# Worker broker settings

CELERY_CACHE_BACKEND = 'django-cache'

# BROKER_URL = 'amqp://chaemoon:chaemoon@13.125.169.112:5672/default'
BROKER_URL = 'amqp://chaemoon:chaemoon@127.0.0.1:5672/default'
CELERY_ACCEPT_CONTENT = ['application/json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'
CELERY_TIMEZONE = 'Asia/Seoul'


# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Seoul'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

AUTH_USER_MODEL = 'accounts.User'
LOGIN_REDIRECT_URL = '/'

CORS_ORIGIN_ALLOW_ALL = True
CORS_ORIGIN_WHITELIST = [
    'http://localhost:8000',
    'http://127.0.0.1:8000',
    'http://13.209.15.144',
]
CORS_ALLOW_CREDENTIALS = True

CORS_ALLOW_METHOD = [
    'GET',
    'POST',
]

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static')
]

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

if DEBUG:
    STATIC_URL = '/static/'
    # STATIC_ROOT = os.path.join(BASE_DIR, 'static')

    MEDIA_URL = '/media/'

else:

    config_secret = json.loads(open(CONFIG_SETTINGS_COMMON_FILE).read())
    AWS_REGION = 'ap-northeast-2'
    AWS_S3_REGION_NAME = 'ap-northeast-2'
    AWS_STORAGE_BUCKET_NAME = config_secret['aws']['s3_bucket_name']
    AWS_QUERYSTRING_AUTH = False
    AWS_S3_HOST = 's3.%s.amazonaws.com' % AWS_STORAGE_BUCKET_NAME
    AWS_ACCESS_KEY_ID = config_secret['aws']['access_key_id']
    AWS_SECRET_ACCESS_KEY = config_secret['aws']['access_secret_key_id']
    AWS_S3_CUSTOM_DOMAIN = '%s.s3.amazonaws.com' % AWS_STORAGE_BUCKET_NAME
    AWS_S3_OBJECT_PARAMETERS = {
        'CacheControl': 'max-age=86400'
    }
    AWS_LOCATION = 'static'

    STATIC_URL = "http://%s/" % AWS_S3_CUSTOM_DOMAIN
    STATICFILES_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
    STATICFILES_LOCATION = 'static'

    MEDIA_URL = 'http://%s/' % AWS_S3_CUSTOM_DOMAIN
    DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
    MEDIAFILES_LOCATION = 'media'

    AWS_DEFAULT_ACL = None
    S3DIRECT_DESTINATIONS = {
        'example_destination': {
            # "key" [required] The location to upload file
            #       1. String: folder path to upload to
            #       2. Function: generate folder path + filename using a function
            'key': 'uploads/images',

            # "auth" [optional] Limit to specfic Django users
            #        Function: ACL function
            'auth': lambda u: u.is_staff,

            # "allowed" [optional] Limit to specific mime types
            #           List: list of mime types
            'allowed': ['image/jpeg', 'image/png', 'video/mp4'],

            # "bucket" [optional] Bucket if different from AWS_STORAGE_BUCKET_NAME
            #          String: bucket name
            'bucket': 'stackofmusic',

            # "endpoint" [optional] Endpoint if different from AWS_S3_ENDPOINT_URL
            #            String: endpoint URL
            'endpoint': 'http://stackofmusic.s3-website.ap-northeast-2.amazonaws.com',

            # "region" [optional] Region if different from AWS_S3_REGION_NAME
            #          String: region name
            'region': 'ap-northeast-2',  # Default is 'AWS_S3_REGION_NAME'

            # "acl" [optional] Custom ACL for object, default is 'public-read'
            #       String: ACL
            'acl': 'private',

            # "cache_control" [optional] Custom cache control header
            #                 String: header
            'cache_control': 'max-age=2592000',

            # "content_disposition" [optional] Custom content disposition header
            #                       String: header
            'content_disposition': lambda x: 'attachment; filename="{}"'.format(x),

            # "content_length_range" [optional] Limit file size
            #                        Tuple: (from, to) in bytes
            'content_length_range': (5000, 20000000),

            # "server_side_encryption" [optional] Use serverside encryption
            #                          String: encrytion standard
            'server_side_encryption': 'AES256',

            # "allow_existence_optimization" [optional] Checks to see if file already exists,
            #                                returns the URL to the object if so (no upload)
            #                                Boolean: True, False
            'allow_existence_optimization': False,
        },
        'example_destination_two': {
            'key': lambda filename, args: args + '/' + filename,
            'key_args': 'uploads/images',
        }
    }

APPEND_SLASH = True
