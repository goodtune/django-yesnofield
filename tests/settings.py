# -*- coding: utf-8
from __future__ import absolute_import, unicode_literals

import django

DEBUG = True
USE_TZ = True

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "de(r3ql+ps7i+#akjf1=8#(u&7kc2_x&ih=8h_*0hc_a^@fh7_"

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": ":memory:",
    }
}

ROOT_URLCONF = "tests.urls"

INSTALLED_APPS = [
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sites",
    "django_yesnofield",
]

SITE_ID = 1

if django.VERSION >= (1, 10):
    MIDDLEWARE = ()
else:
    MIDDLEWARE_CLASSES = ()
