"""
Django settings for app project.

Generated by 'django-admin startproject' using Django 3.0.7.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.0/ref/settings/
"""

import os
import datetime
from rest_framework import permissions
import django
from django.utils.encoding import smart_str
django.utils.encoding.smart_text = smart_str




from dotenv import load_dotenv
load_dotenv()


def get_env_variable(name):
    try:
        return os.environ[name]
    except KeyError:
        message = "Expected environment variable '{}' not set.".format(name)
        raise Exception(message)


# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = get_env_variable("SECRET_KEY")
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ["127.0.0.1", "localhost", "0.0.0.0", "*"]


# Application definition

INSTALLED_APPS = [
    "jazzmin",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "drf_yasg",
    "corsheaders",
    "rest_framework",
    "import_export",
    "user",
    "frontend",
    "feed",
    "media",
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

ROOT_URLCONF = "app.urls"

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

WSGI_APPLICATION = "app.wsgi.application"


# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        # os.environ.get  => get variables from environment (of docker-compose)
        # all variables comes from docker-compose.yml
        "HOST": get_env_variable("DB_HOST"),
        "NAME": get_env_variable("DB_NAME"),
        "USER": get_env_variable("DB_USER"),
        "PASSWORD": get_env_variable("DB_PASS"),
    },
    "annotation_db": {
        "ENGINE": "django.db.backends.postgresql",
        "HOST": get_env_variable("DB_HOST"),
        "NAME": get_env_variable("DB_NAME"),
        "USER": get_env_variable("DB_USER"),
        "PASSWORD": get_env_variable("DB_PASS"),
        "PORT": os.environ.get("ANNOTATION_DB_PORT", 5432),
    }
}

DATABASE_ROUTERS = ["feed.routers.AnnotationRouter"]

# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

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

APPEND_SLASH = False

REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": (
        "rest_framework_jwt.authentication.JSONWebTokenAuthentication",
        "rest_framework.authentication.SessionAuthentication",
        "rest_framework.authentication.BasicAuthentication",


    ),
    # 'DEFAULT_SCHEMA_CLASS': 'drf_spectacular.openapi.AutoSchema',
    "DEFAULT_PAGINATION_CLASS": "rest_framework.pagination.LimitOffsetPagination",
    "PAGE_SIZE": 1000,
}


JWT_AUTH = {
    "JWT_EXPIRATION_DELTA": datetime.timedelta(seconds=259200),
    "JWT_ALLOW_REFRESH": True,
    # 3 days
    "JWT_REFRESH_EXPIRATION_DELTA": datetime.timedelta(seconds=259200),
    "JWT_AUTH_COOKIE": "JWT",
}




# Internationalization
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

STATIC_URL = "/static/"
MEDIA_URL = "/media/"

# These directories comes from Dockerfile
MEDIA_ROOT = os.path.join(BASE_DIR, "media")
# with these config, we can access django admin in production due to storing CSS/HTML in static root!
# STATIC_ROOT = '/app/static'
STATIC_ROOT = os.path.join(BASE_DIR, "static_cdn")

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static"),
]


JAZZMIN_SETTINGS = {
    # title of the window
    "site_title": "MeetAll Admin Panel",
    # Title on the brand, and the login screen (19 chars max)
    "site_header": "MeetAll",
    # square logo to use for your site, must be present in static files, used for favicon and brand on top left
    "site_logo": "",
    # Welcome text on the login screen
    "welcome_sign": "Welcome to MeetAll",
    # Copyright on the footer
    "copyright": "ilaydakurt",
    # The model admin to search from the search bar, search bar omitted if excluded
    "search_model": "auth.User",
    # Field name on user model that contains avatar image
    "user_avatar": None,
    ############
    # Top Menu #
    ############
    # Links to put along the top menu
    "topmenu_links": [
        # Url that gets reversed (Permissions can be added)
        {"name": "Home", "url": "admin:index", "permissions": ["auth.view_user"]},
        # external url that opens in a new window (Permissions can be added)
        # {'name': 'Support', 'url': 'https://google.com',
        #     'new_window': True},
        # model admin to link to (Permissions checked against model)
        {"model": "auth.User"},
        # App with dropdown menu to all its models pages (Permissions checked against models)
        # {'app': 'fair'},
        # {'app': 'field'},
        # {'model': 'core.UserManager'}
    ],
    #############
    # User Menu #
    #############
    # Additional links to include in the user menu on the top right ('app' url type is not allowed)
    "usermenu_links": [
        {
            "name": "Support",
            "url": "https://github.com/farridav/django-jazzmin/issues",
            "new_window": True,
        },
        {"model": "auth.User"},
    ],
    #############
    # Side Menu #
    #############
    # Whether to display the side menu
    "show_sidebar": True,
    # Whether to aut expand the menu
    "navigation_expanded": True,
    # Hide these apps when generating side menu e.g (auth)
    "hide_apps": [],
    # Hide these models when generating side menu (e.g auth.user)
    "hide_models": [],
    # List of apps (and/or models) to base side menu ordering off of (does not need to contain all apps/models)
    "order_with_respect_to": ["auth", "auth.User"],
    # Custom links to append to app groups, keyed on app name
    # 'custom_links': {
    #     'fair': [{
    #         'name': 'Make Messages',
    #         'url': 'fair',
    #         'icon': 'fas fa-comments',
    #         'permissions': ['permissions.AllowAny']
    #     }]
    # },
    # Custom icons for side menu apps/models See https://fontawesome.com/icons?d=gallery&m=free
    # for a list of icon classes
    "icons": {
        "auth": "fas fa-users-cog",
        "auth.user": "fas fa-user",
        "auth.Group": "fas fa-users",
    },
    # Icons that are used when one is not manually specified
    "default_icon_parents": "fas fa-chevron-circle-right",
    "default_icon_children": "fas fa-circle",
    #############
    # UI Tweaks #
    #############
    # Relative paths to custom CSS/JS scripts (must be present in static files)
    "custom_css": None,
    "custom_js": None,
    # Whether to show the UI customizer on the sidebar
    "show_ui_builder": True,
    ###############
    # Change view #
    ###############
    # Render out the change view as a single form, or in tabs, current options are
    # - single
    # - horizontal_tabs (default)
    # - vertical_tabs
    # - collapsible
    # - carousel
    "changeform_format": "collapsible",
    # override change forms on a per modeladmin basis
    "changeform_format_overrides": {
        "auth.user": "collapsible",
        "auth.group": "vertical_tabs",
    },
    # Add a language dropdown into the admin
    "language_chooser": True,
}

FIXTURE_DIRS = [
    os.path.join(BASE_DIR, 'fixtures')
]

EMAIL_HOST = get_env_variable("EMAIL_HOST")
EMAIL_HOST_USER = get_env_variable("EMAIL_HOST_USER")
EMAIL_HOST_PASSWORD = get_env_variable("EMAIL_HOST_PASSWORD")
EMAIL_PORT = 587
EMAIL_BACKEND = get_env_variable("EMAIL_BACKEND")
EMAIL_TIMEOUT = 60
EMAIL_USE_TLS = True

DOMAIN_URL = get_env_variable("DOMAIN_URL")
