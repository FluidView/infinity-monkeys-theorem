from pathlib import Path
import pyodbc

BASE_DIR = Path(__file__).resolve().parent.parent.parent
from decouple import config

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    },
    # "nch_db_main": {
    #     "ENGINE": config('SQL_NCH_ENGINE'),
    #     "NAME": config('SQL_NCH_NAME'),
    #     "USER": config('SQL_NCH_USER'),
    #     "PASSWORD": config('SQL_NCH_PASSWORD'),
    #     "HOST": config('SQL_NCH_HOST'),
    #     "PORT": config('SQL_NCH_PORT', cast=int),
    #     "OPTIONS": {"driver": config('SQL_NCH_OPTIONS_DRIVE'),
    #     },
    # },
}

DATABASE_CONNECTION_POOLING = False