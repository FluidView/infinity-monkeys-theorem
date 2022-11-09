from .middleware_settings import * # noqa: ignore=F401 isort:skip
from .installed_apps_settings import * # noqa: ignore=F401 isort:skip
from .internationalizations_settings import * # noqa: ignore=F401 isort:skip
from .auth_settings import * # noqa: ignore=F401 isort:skip
from .host_settings import * # noqa: ignore=F401 isort:skip
from .media_settings import * # noqa: ignore=F401 isort:skip
from .database_settings import * # noqa: ignore=F401 isort:skip

from decouple import config

DEBUG = config('DEBUG', default=False, cast=bool)

DJANGO_SETTINGS_MODULE = config('DJANGO_SETTINGS_MODULE')

ROOT_URLCONF = 'configuration.urls'

WSGI_APPLICATION = 'configuration.wsgi.application'
