from settings_base import *

ENVIRONMENT = 'PROD'

ALLOWED_HOSTS = [
    'hackbase.herokuapp.com',
]

DEBUG = False
TEMPLATE_DEBUG = DEBUG
DAJAXICE_DEBUG = DEBUG

STATICFILES_STORAGE = 'storages.backends.s3boto.S3BotoStorage'
DEFAULT_FILE_STORAGE = 'storages.backends.s3boto.S3BotoStorage'
AWS_STORAGE_BUCKET_NAME = 'hackbase'
AWS_S3_FILE_OVERWRITE = True
AWS_QUERYSTRING_AUTH = False
AWS_HEADERS = {
    'Cache-Control': 'public, max-age=%s' % (30 * 24 * 60 * 60),
}
COMPRESS_STORAGE = STATICFILES_STORAGE

STATIC_URL = 'https://s3.amazonaws.com/hackbase/'
MEDIA_URL = 'https://s3.amazonaws.com/hackbase/'

# Facebook Information
FACEBOOK_APP_ID = ''
FACEBOOK_APP_SECRET = ''

# AWS Information
AWS_ACCESS_KEY_ID = ''
AWS_SECRET_ACCESS_KEY = ''
