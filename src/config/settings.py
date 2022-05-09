import os

from dotenv import load_dotenv

load_dotenv()

API_V1_PREFIX = '/api/v1'
SITE_DOMAIN = os.environ.get('SITE_DOMAIN', 'localhost:8000')
DATABASE_URL = os.environ.get('DATABASE_URL', 'sqlite:///db.sqlite')
ORIGINS = [
    "http://localhost",
    "http://127.0.0.1",
    "http://localhost:8080",
    "http://127.0.0.1:8080",
]


ALGORITHM = 'HS256'

ACCESS_TOKEN_TYPE = os.environ.get('ACCESS_TOKEN_TYPE', 'atoken')
ACCESS_TOKEN_EXPIRE_MINUTES = 15
ACCESS_TOKEN_SECRET_KEY = os.environ.get(
    'ACCESS_TOKEN_SECRET_KEY',
    '3fe69992d6b2e6a58beb46d715167876a5832544b9025e2b78eaaf40084a46be'
)
REFRESH_TOKEN_TYPE = os.environ.get(
    'REFRESH_TOKEN_TYPE',
    'rtoken'
)
REFRESH_TOKEN_EXPIRE_MINUTES = 60 * 24 * 30
REFRESH_TOKEN_SECRET_KEY = os.environ.get(
    'REFRESH_TOKEN_SECRET_KEY',
    '3fe69992d6b2e6a58beb46d715167876a5832544b9025e2b78eaaf40084a46be'
)
EMAIL_CONFIRMATION_TOKEN_TYPE = os.environ.get(
    'EMAIL_CONFIRMATION_TOKEN_TYPE',
    'etoken'
)
EMAIL_CONFIRMATION_TOKEN_EXPIRE_MINUTES = 60 * 24 * 2
EMAIL_CONFIRMATION_TOKEN_SECRET_KEY = os.environ.get(
    'EMAIL_CONFIRMATION_TOKEN_SECRET_KEY',
    '3fe69992d6b2e6a58beb46d715167876a5832544b9025e2b78eaaf40084a46be'
)
PASSWORD_RESET_TOKEN_TYPE = os.environ.get(
    'PASSWORD_RESET_TOKEN_TYPE',
    'ptoken'
)
PASSWORD_RESET_TOKEN_EXPIRE_MINUTES = 60 * 24 * 2
PASSWORD_RESET_TOKEN_SECRET_KEY = os.environ.get(
    'PASSWORD_RESET_TOKEN_SECRET_KEY',
    '3fe69992d6b2e6a58beb46d715167876a5832544b9025e2b78eaaf40084a46be'
)


ALLOWED_IMAGE_FORMAT_EXTENSIONS = 'jpg', 'jpeg', 'png'
ALLOWED_AUDIO_FORMAT_EXTENSIONS = 'mp3',


MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
MAIL_FROM = os.environ.get('MAIL_FROM')
MAIL_PORT = os.environ.get('MAIL_PORT', 587)
MAIL_SERVER = os.environ.get('MAIL_SERVER')
MAIL_FROM_NAME = "FastAPI Music"
MAIL_TLS = True
MAIL_SSL = False
TEMPLATE_FOLDER = 'src/templates'
VALIDATE_CERTS = True
