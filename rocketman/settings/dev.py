from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '1m)*b1u&+436bs=8al%2wsow3_)n4$*$&^(scgxp&12d8+$fm2'

# SECURITY WARNING: define the correct hosts in production!
ALLOWED_HOSTS = ['*']

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

INSTALLED_APPS += [
    'debug_toolbar',
]

MIDDLEWARE += [
    'debug_toolbar.middleware.DebugToolbarMiddleware',
]

INTERNAL_IPS = [
    '127.0.0.1',
]

CACHES = {
     "default":{
         "BACKEND": "django.core.cache.backends.filebased.FileBasedCache",
         "LOCATION": os.path.join(BASE_DIR, ".cache"),
     }
}

try:
    from .local import *
except ImportError:
    pass
