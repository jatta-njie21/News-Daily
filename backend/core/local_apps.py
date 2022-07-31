import os
from django.conf import settings
from django.core import management
from .local_conf import load_local_conf


def load_apps(BASE_DIR):
    items = load_local_conf(BASE_DIR)
    for item in items["modules"]:
        app_name = item["name"]
        if app_name not in settings.INSTALLED_APPS:
            settings.INSTALLED_APPS += (app_name, )


def extract_app(module):
    return "%s" % (module["name"])


def local_apps(BASE_DIR):
    LOCAL_CONF = load_local_conf(BASE_DIR)
    return [*map(extract_app, LOCAL_CONF["modules"])]