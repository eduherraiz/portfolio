# -*- coding: utf-8 -*-

import os

from configurations import Settings
from apconf.mixins import CachesMixin, DatabasesMixin, PathsMixin, LogsMixin
from apconf.mixins import SecurityMixin, DebugMixin, CompressMixin

from apconf import Options

opts = Options()


class Base(CachesMixin, DatabasesMixin, PathsMixin, LogsMixin, SecurityMixin,
           DebugMixin, CompressMixin, Settings):

    BASE_DIR = os.path.dirname(os.path.dirname(__file__))

    INSTALLED_APPS = (
        'modeltranslation',
        'django.contrib.admin',
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.messages',
        'django.contrib.staticfiles',
        'django.contrib.sites',
        'django_extensions',
        'zinnia_bootstrap',
        'apconf',
        'raven.contrib.django.raven_compat',
        'crispy_forms',
        'floppyforms',
        'captcha',
        'compressor',
        'home',
        'django_comments',
        'tagging',
        'mptt',
        'ckeditor',
        'tinymce',
        'zinnia',
        'zinnia_ckeditor',
        'constance',
        'constance.backends.database',
    )

    MIDDLEWARE_CLASSES = (
        'django.contrib.sessions.middleware.SessionMiddleware',
        'django.middleware.common.CommonMiddleware',
        'django.middleware.csrf.CsrfViewMiddleware',
        'django.contrib.auth.middleware.AuthenticationMiddleware',
        'django.middleware.locale.LocaleMiddleware',
        'django.contrib.messages.middleware.MessageMiddleware',
        'django.middleware.clickjacking.XFrameOptionsMiddleware',
    )

    TEMPLATE_CONTEXT_PROCESSORS = (
        'django.contrib.auth.context_processors.auth',
        'django.core.context_processors.i18n',
        'django.core.context_processors.request',
        'django.core.context_processors.media',
        'django.core.context_processors.static',
        'django.core.context_processors.debug',
        'django.core.context_processors.tz',
        'django.contrib.messages.context_processors.messages',
        'zinnia.context_processors.version',  # Optional
        'django.core.context_processors.request',
        'constance.context_processors.config',
    )

    TEMPLATE_LOADERS = (
         'app_namespace.Loader',
         'django.template.loaders.filesystem.Loader',
         'django.template.loaders.app_directories.Loader',
     )

    ROOT_URLCONF = 'main.urls'

    WSGI_APPLICATION = 'main.wsgi.application'

    gettext = lambda s: s
    LANGUAGES = (
        ('es', gettext('Castellano')),
        ('ca', gettext('Català')),
        ('en', gettext('English')),
    )

    LANGUAGE_CODE = 'es'

    TIME_ZONE = 'Europe/Madrid'
    USE_I18N = True
    USE_L10N = True
    USE_TZ = True

    APP_SLUG = opts.get('APP_SLUG', '')
    TEMPLATE_DIRS = ('templates', )

    CRISPY_TEMPLATE_PACK = 'bootstrap3'

    # Django toolbar
    INTERNAL_IPS = ['127.0.0.1']
    LOGIN_URL = '/login'
    LOGIN_REDIRECT_URL = '/'

    SITE_ID = 1

    # # Captcha

    EMAIL_FROM = opts.get("EMAIL_FROM", "no-reply@domain.com")
    LIST_OF_EMAIL_RECIPIENTS = opts.get("LIST_OF_EMAIL_RECIPIENTS", "myemail@mydomain.com")

    CKEDITOR_UPLOAD_PATH = "uploads/"

    AKISMET_API_KEY = opts.get("AKISMET_API_KEY", "")

    # Zinnia antispam
    ZINNIA_SPAM_CHECKER_BACKENDS = (
    'zinnia_akismet.akismet',
    )

    CONSTANCE_CONNECTION = {
        'host': 'localhost',
        'port': 6379,
        'db': 0,
    }

    CONSTANCE_CONFIG = {
        'BLOG_NAME' : ("Blog name", u"Blog name"),
        'LOGO' : ( "zinnia_bootstrap/img/zinnia.png", u"Static path for the logo"),
        'GOOGLE_ANALYTICS_CODE' : ("", u"Google analytics code to track the visits"),
    }

    CONSTANCE_BACKEND = 'constance.backends.database.DatabaseBackend'

    CKEDITOR_CONFIGS = {
        'default': {
            'toolbar': 'Full',
            'height': 300,
            'width': '100%',
            'removePlugins': 'stylesheetparser',
            'allowedContent': True,
        },
    }

    RECAPTCHA_PUBLIC_KEY = opts.get("RECAPTCHA_PUBLIC_KEY", "")
    RECAPTCHA_PRIVATE_KEY = opts.get("RECAPTCHA_PRIVATE_KEY", "")
    RECAPTCHA_USE_SSL = True

    TWITTER_CONSUMER_KEY = opts.get("TWITTER_CONSUMER_KEY", "")
    TWITTER_CONSUMER_SECRET = opts.get("TWITTER_CONSUMER_SECRET", "")
    TWITTER_ACCESS_KEY = opts.get("TWITTER_ACCESS_KEY", "")
    TWITTER_ACCESS_SECRET = opts.get("TWITTER_ACCESS_SECRET", "")

    ZINNIA_PING_EXTERNAL_URLS = False
    ZINNIA_SAVE_PING_DIRECTORIES = False