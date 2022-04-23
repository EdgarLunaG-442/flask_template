import os

PROPAGATE_EXCEPTIONS = True
SQLALCHEMY_TRACK_MODIFICATIONS = False
SHOW_SQLALCHEMY_LOG_MESSAGES = False

# Database configuration
POSTGRES_USER = os.getenv('POSTGRES_USER', 'postgres')
POSTGRES_PWD = os.getenv('POSTGRES_PWD', 'BJM3akVphB3MQcyzrykWxQfbzEwFSm')
POSTGRES_HOST = os.getenv('POSTGRES_HOST', 'blacklist.csakqsft2dm2.us-east-1.rds.amazonaws.com')
POSTGRES_PORT = os.getenv('POSTGRES_PORT', '5432')
POSTGRES_DB = os.getenv('POSTGRES_DB', 'blacklist')
LOCAL_DB_FILE = os.getenv('LOCAL_DB_FILE')

if LOCAL_DB_FILE:
    SQLALCHEMY_DATABASE_URI = 'sqlite:///../test.db'
else:
    SQLALCHEMY_DATABASE_URI = f'postgresql://{POSTGRES_USER}:{POSTGRES_PWD}@{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_DB}'

# JWT Configuration
SECRET_KEY = os.getenv('SECRET_KEY', 'blacklist-app')
API_UUID = os.getenv('API_UUID', '84e532cb-0788-4729-a379-1f667f18a443')
