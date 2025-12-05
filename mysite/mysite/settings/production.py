from .base import *
import os
import dj_database_url

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get("SECRET_KEY", "default-insecure-key-for-dev")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = 'RENDER' not in os.environ

# Allowed Hosts
RENDER_EXTERNAL_HOSTNAME = os.environ.get('RENDER_EXTERNAL_HOSTNAME')
if RENDER_EXTERNAL_HOSTNAME:
    ALLOWED_HOSTS = [RENDER_EXTERNAL_HOSTNAME]
else:
    ALLOWED_HOSTS = []

# Database
DATABASES = {
    "default": dj_database_url.config(
        default="sqlite:///" + str(BASE_DIR / "db.sqlite3"),
        conn_max_age=600,
    )
}

# Static Files (WhiteNoise)
MIDDLEWARE.insert(1, "whitenoise.middleware.WhiteNoiseMiddleware")

STORAGES = {
    "default": {
        "BACKEND": "django.core.files.storage.FileSystemStorage",
    },
    "staticfiles": {
        "BACKEND": "whitenoise.storage.CompressedManifestStaticFilesStorage",
    },
}
