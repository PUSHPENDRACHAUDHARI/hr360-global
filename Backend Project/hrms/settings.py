from pathlib import Path
import os
import pymysql

pymysql.install_as_MySQLdb()

BASE_DIR = Path(__file__).resolve().parent.parent

# ===============================
# SECURITY SETTINGS
# ===============================

SECRET_KEY = os.environ.get("SECRET_KEY", "django-insecure-change-this")

DEBUG = False   # IMPORTANT: False in production

ALLOWED_HOSTS = [
    "31.97.203.68",
    "hr360.kavyainfoweb.com",
    "localhost",
    "127.0.0.1",
]

CSRF_TRUSTED_ORIGINS = [
    "http://31.97.203.68",
    "http://31.97.203.68:8878",
    "http://hr360.kavyainfoweb.com",
]

# ===============================
# APPLICATIONS
# ===============================

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "app",   # your main app
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "hrms.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "hrms.wsgi.application"

# ===============================
# DATABASE (Docker MySQL)
# ===============================

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.mysql",
        "NAME": os.environ.get("MYSQL_DATABASE", "hr360"),
        "USER": os.environ.get("MYSQL_USER", "hr360user"),
        "PASSWORD": os.environ.get("MYSQL_PASSWORD", "Hr360@123"),
        "HOST": "db",   # IMPORTANT for Docker
        "PORT": "3306",
    }
}

# ===============================
# STATIC FILES (IMPORTANT FIX)
# ===============================

STATIC_URL = "/static/"
STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "app/static"),
]

# ===============================
# DEFAULT SETTINGS
# ===============================

LANGUAGE_CODE = "en-us"
TIME_ZONE = "Asia/Kolkata"
USE_I18N = True
USE_TZ = True

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

