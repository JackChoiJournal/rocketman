from .base import *

DEBUG = False

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '1m)*b1u&+436bs=8al%2wsow3_)n4$*$&^(scgxp&12d8+$fm2'

# SECURITY WARNING: define the correct hosts in production!
ALLOWED_HOSTS = ['localhost', 'rocketmane.learwagtail.com', 'digitalocean.ip']

CACHES = {
     "default":{
         "BACKEND": "django.core.cache.backends.filebased.FileBasedCache",
         "LOCATION": os.path.join(BASE_DIR, ".cache"),
     }
}

# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'rocketman',
        'USER': 'rocketman',
        'PASSWORD': 'scgxp12d8fm2wad',
        'HOST': 'locathost',
        'PORT': '5432',
    }
}

import sentry_sdk
from sentry_sdk.integrations.django import DjangoIntegration

sentry_sdk.init(
    dsn="https://56708b8888dd42a8a316db3b52d88269@o349765.ingest.sentry.io/5778319",
    integrations=[DjangoIntegration()],

    # Set traces_sample_rate to 1.0 to capture 100%
    # of transactions for performance monitoring.
    # We recommend adjusting this value in production.
    traces_sample_rate=1.0,

    # If you wish to associate users to errors (assuming you are using
    # django.contrib.auth) you may enable sending PII data.
    send_default_pii=True
)

try:
    from .local import *
except ImportError:
    pass
