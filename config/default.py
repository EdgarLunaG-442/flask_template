import os
from datetime import timedelta

PROPAGATE_EXCEPTIONS = True
POSTGRES_USER = os.getenv('POSTGRES_USER', 'postgres')
POSTGRES_PWD = os.getenv('POSTGRES_PWD', 12345)
POSTGRES_HOST = os.getenv('POSTGRES_HOST', 'localhost')
POSTGRES_PORT = os.getenv('POSTGRES_PORT', '5432')
POSTGRES_DB = os.getenv('POSTGRES_DB', 'postgres')
LOCAL_DB_FILE = os.getenv('LOCAL_DB_FILE')
# Database configuration
if LOCAL_DB_FILE:
    SQLALCHEMY_DATABASE_URI = 'sqlite:///../test.db'
else:
    SQLALCHEMY_DATABASE_URI = f'postgresql://{POSTGRES_USER}:{POSTGRES_PWD}@{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_DB}'
SQLALCHEMY_TRACK_MODIFICATIONS = False
SHOW_SQLALCHEMY_LOG_MESSAGES = False