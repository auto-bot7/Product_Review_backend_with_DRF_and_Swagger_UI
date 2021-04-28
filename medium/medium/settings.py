import os
from datetime import timedelta
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '&%tl2$7(5z(#(b07yl4i6y7u&w-+*l*xd#l6&54jx^=fr^59e6'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'reviews',
    'rest_framework',
    'django.contrib.staticfiles',
    'django_filters',
    'versatileimagefield',
    'corsheaders',
    'authe',
    'rest_framework_simplejwt.token_blacklist',
    'drf_yasg'
   
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    # CorsMiddleware should be placed before CommonMiddleware or any other Middleware
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'medium.urls'

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

WSGI_APPLICATION = 'medium.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATIC_URL = '/static/'

#PART 4----------SERIALIZERS AND FILTERS-----------------------------------------------------------------------------
REST_FRAMEWORK={
    'DEFAULT_FILTER_BACKENDS':['django_filters.rest_framework.DjangoFilterBackend'],
#PART 7 --------------------JWT-------------------------------------------------------------------------------------
    'DEFAULT_AUTHENTICATION_CLASSES':[
        'rest_framework_simplejwt.authentication.JWTAuthentication'
        ]
}

#PART 5-------------VERSATILE IMAGE FIELDS---------------------------------------------------------------------------
MEDIA_URL='/media/'
MEDIA_ROOT=os.path.join(BASE_DIR,'media')
#Global settings for image sizes field in seralizer class .
#Represents different image sizes in api call for following paraameters.
VERSATILEIMAGEFIELD_RENDITION_KEY_SETS = {
    'product_headshot': [
        ('full_size', 'url'),
        ('thumbnail', 'thumbnail__100x100'),
        ('medium_square_crop', 'crop__400x400'),
        ('small_square_crop', 'crop__50x50')
    ]
}

#PART 6--------------CROSS ORIGIN RESOURCE SHARING---------------------------https://pypi.org/project/django-cors-headers/


# CORS_ALLOWED_ORIGINS : A list of origins that are authorized to make cross-site HTTP requests.
# CORS_ALLOWED_ORIGINS = [
#     "https://www.safesite.com",
#                         ]

# CORS_ALLOW_ALL_ORIGINS : If True, all origins will be allowed. Setting this to True can be dangerous, 
# as it allows any website to make cross-origin requests to yours.
# CORS_ALLOW_ALL_ORIGINS = True

# CSRF_TRUSTED_ORIGINS : A list of hosts which are trusted origins for unsafe requests. 
# If you need cross-origin unsafe requests over HTTPS, continuing the example, add “subdomain.safesite.com” to this list.
# CSRF_TRUSTED_ORIGINS = [
#     'www.safesite.com',
#                        ]

# CORS_ALLOW_CREDENTIALS : If True, cookies will be allowed to be included in cross-site HTTP requests.
# CORS_ALLOW_CREDENTIALS = True
CORS_ALLOWED_ORIGINS=["https://www.test-cors.org",]
CSRF_TRUSTED_ORIGINS=["https://www.test-cors.org",]
CORS_ALLOWED_CREDENTIALS=[True]


#PART 7----------------SIMPLE_JWT----------------
SIMPLE_JWT={
    'ACCESS_TOKEN_LIFETIME':timedelta(hours=1),
    'REFRESH_TOKEN_LIFETIME':timedelta(hours=4),
    'ROTATE_REFRESH_TOKENS':True,
    'BLACKLIST_AFTER_ROTATION':True
}

SWAGGER_SETTINGS={
    'SECURITY_DEFINITIONS':{
        'Auth Token [Bearer (JWT)]':{
            "type":"apiKey",
            "name":"Authorization",
            "in":"header"
        }
    }
}