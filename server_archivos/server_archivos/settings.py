import datetime
import os
import sys
from pathlib import Path

from decouple import Csv, config


BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = config("SECRET_KEY")

ENVIRONMENT = config("ENVIRONMENT", "local")

DEBUG = config("DEBUG", default=False, cast=bool)  # NOSONAR


ALLOWED_HOSTS = ["*"]

APP_LOGLEVEL = config("APP_LOGLEVEL", default="INFO")

# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    # Apps Locales
    "usuario",
    "repositorio",
    "core",
    "rest",
    # Apps Externas
    "drf_yasg",
    "rest_framework",
    "rest_framework_simplejwt",
    "corsheaders",
    "simple_history",
    "debug_toolbar",
    "django_celery_beat",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    # Cors configurados para admitir distintos destinos
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.common.CommonMiddleware",
    # Cors simple history
    "simple_history.middleware.HistoryRequestMiddleware",
    # Cors para verificar velocidad de querys
    "debug_toolbar.middleware.DebugToolbarMiddleware",
    # Cors para servir media en local
    "whitenoise.middleware.WhiteNoiseMiddleware",
]

ROOT_URLCONF = "server_archivos.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],
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

WSGI_APPLICATION = "server_archivos.wsgi.application"


# Database

DATABASES = {
    "default": {
        "ENGINE": config("DB_ENGINE", default="django.db.backends.postgresql"),
        "NAME": config("DB_NAME"),
        "USER": config("DB_USER"),
        "PASSWORD": config("DB_PASSWORD"),
        "HOST": config("DB_HOST"),
        "PORT": config("DB_PORT", default="5432"),
    },
}


# Password validation

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Internationalization

LANGUAGE_CODE = "es-mx"

TIME_ZONE = "America/Mexico_City"

USE_I18N = True

USE_TZ = True

DEFAULT_CHARSET = "utf-8"

# Storage Local config
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"
# Static files (CSS, JavaScript, Images)
STATIC_ROOT = os.path.join(BASE_DIR, "static")
STATIC_URL = "static/"

# Media Config
MEDIA_URL = "/media/"
MEDIA_ROOT = os.path.join(BASE_DIR, "media")

# Default primary key field type
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# REST Config
REST_FRAMEWORK = {
    "DEFAULT_RENDERER_CLASSES": [
        "rest_framework.renderers.JSONRenderer",
    ],
    "DEFAULT_AUTHENTICATION_CLASSES": (
        "rest_framework_simplejwt.authentication.JWTAuthentication",
        "rest_framework.authentication.SessionAuthentication",
    ),
    "DEFAULT_PERMISSION_CLASSES": [],
    # https://www.django-rest-framework.org/api-guide/exceptions/#custom-exception-handling
    # "EXCEPTION_HANDLER": "rest.exception_handler.custom_exception_handler",
    "DEFAULT_PARSER_CLASSES": [
        "rest_framework.parsers.JSONParser",
        "rest_framework.parsers.FormParser",
        "rest_framework.parsers.MultiPartParser",
    ],
}

# JWT headers
SIMPLE_JWT = {
    "ACCESS_TOKEN_LIFETIME": datetime.timedelta(days=1),
    "REFRESH_TOKEN_LIFETIME": datetime.timedelta(days=1),
}

CORS_ORIGIN_ALLOW_ALL = config("CORS_ORIGIN_ALLOW_ALL", default=DEBUG, cast=bool)

CORS_ALLOW_HEADERS = [
    "accept",
    "accepts",
    "accept-encoding",
    "authorization",
    "content-type",
    "dnt",
    "origin",
    "user-agent",
    "x-csrftoken",
    "x-requested-with",
]

# Swagger Settings
SWAGGER_SETTINGS = {
    "USE_SESSION_AUTH": config(
        "SWAGGER_USE_SESSION_AUTH", default=False, cast=bool
    ),  # Desactiva la autenticación por sesión
    "SECURITY_DEFINITIONS": {
        "Bearer": {
            "type": "apiKey",
            "name": "Authorization",
            "in": "header",
        },
    },
    "LOGIN_URL": "rest_framework:login",
    "LOGOUT_URL": "rest_framework:logout",
}

# Permite modificar el tamanio del campo history_change_reason a cualquier tamanio
# https://django-simple-history.readthedocs.io/en/latest/historical_model.html#textfield-as-history-change-reason
SIMPLE_HISTORY_HISTORY_CHANGE_REASON_USE_TEXT_FIELD = True

# Auth custom model
AUTH_USER_MODEL = "usuario.User"


# Toolbar debug
SHOW_DJANGO_DEBUG_TOLBAR = config("SHOW_DJANGO_DEBUG_TOLBAR", default=False, cast=bool)


def show_toolbar(_):
    return DEBUG and SHOW_DJANGO_DEBUG_TOLBAR and "test" not in sys.argv


DEBUG_TOOLBAR_CONFIG = {
    "DISABLE_PANELS": ["debug_toolbar.panels.redirects.RedirectsPanel"],
    "SHOW_TEMPLATE_CONTEXT": True,
    "SHOW_TOOLBAR_CALLBACK": show_toolbar,
}
# https://django-debug-toolbar.readthedocs.io/en/latest/installation.html#internal-ips
INTERNAL_IPS = [
    "127.0.0.1",
]
if config("USE_DOCKER", default=False, cast=bool):
    import socket

    hostname, _, ips = socket.gethostbyname_ex(socket.gethostname())
    INTERNAL_IPS += [".".join(ip.split(".")[:-1] + ["1"]) for ip in ips]

# Redis Configuration
REDIS_HOST = config("REDIS_HOST", default="localhost")
REDIS_PORT = config("REDIS_PORT", default=6379, cast=int)

# Celery Configuration
CELERY_BROKER_URL = config("CELERY_BROKER_URL", "redis://localhost:6379/0")
CELERY_RESULT_BACKEND = config("CELERY_RESULT_BACKEND", "redis://localhost:6379/0")
CELERY_ACCEPT_CONTENT = ["application/json"]
CELERY_TASK_SERIALIZER = "json"
CELERY_RESULT_SERIALIZER = "json"
CELERY_TIMEZONE = "America/Mexico_City"
