from settings_base import *

ENVIRONMENT = 'DEV'

DEBUG = True
TEMPLATE_DEBUG = DEBUG
DAJAXICE_DEBUG = DEBUG

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': '%s' % PROJECT_DIR,
        'USER': '%s_admin' % PROJECT_DIR,
        'PASSWORD': 'localhost',
        'HOST': 'localhost',
        'PORT': '',
    }
}

STATIC_ROOT = os.path.join(PROJECT_ROOT, 'static')
STATIC_URL = '/static/'
MEDIA_ROOT = os.path.join(PROJECT_ROOT, 'media')
MEDIA_URL = '/media/'

FACEBOOK_APP_ID = '164671287034955'
FACEBOOK_APP_SECRET = 'ab27e31953712a42dd7e3e92a4dcbc60'
