import os
import dj_database_url
from django.contrib.messages import constants as messages

################################
##     BASE CONFIGURATION     ##
################################

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SECRET_KEY = 'gbgsg-!tp&cy&8@19mh@&#-1=k#kqg5^f)1=08zsmdy04i!k4c'
DEBUG = int(os.environ.get('DEBUG', default=1))
ALLOWED_HOSTS = ['localhost', '127.0.0.1', 'dj-property.herokuapp.com']


################################
##  APPLICATION CONFIGURATION ##
################################

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'pages.apps.PagesConfig',
    'accounts.apps.AccountsConfig',
    'contacts.apps.ContactsConfig',
    'listings.apps.ListingsConfig',
    'realtors.apps.RealtorsConfig'
]

###############################
##  MIDDLEWARE CONFIGURATION ##
###############################

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',  # whitenoise 
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'djproperty.urls'

################################
##    APPLICATION TEMPLATES   ##
################################

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [ os.path.join( BASE_DIR, 'templates' )],
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




################################
##      INTERNALIZATION       ##
################################

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


################################
##  STATIC FILE CONFIGURATION ##
################################

STATIC_URL = '/static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'assets')]
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')


################################
##      WSGI CONFIGURATION    ##
################################

WSGI_APPLICATION = 'djproperty.wsgi.application'

################################
##    DATABASE CONFIGURATION  ##
################################

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

################################
##    POSTGRES CONFIGURATION  ##
################################

DATABASE_URL = os.environ.get('DATABASE_URL')
db_from_env = dj_database_url.config(default=DATABASE_URL, conn_max_age=500, ssl_require=True)
DATABASES['default'].update(db_from_env)

# DATABASES = {
#     'default': {
#         'ENGINE': config('SQL_ENGINE'),
#         'NAME': config('SQL_DATABASE'),
#         'USER': config('SQL_USER'),
#         'PASSWORD': config('SQL_PASSWORD'),
#         'HOST': config('SQL_HOST'),
#         'PORT': config('SQL_PORT'),
#     }
# }

################################
##    MESSAGES CONFIGURATION  ##
################################

MESSAGE_TAGS = {
    messages.ERROR: 'danger'
}

################################
##     EMAIL CONFIGURATION    ##
################################

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = os.environ.get('EMAIL_HOST')
EMAIL_PORT = os.environ.get('EMAIL_PORT')
EMAIL_HOST_USER = os.environ.get('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_HOST_PASSWORD')
EMAIL_USE_TLS = True