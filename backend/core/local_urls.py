from django.urls import include, path

from .local_conf import load_local_conf
from .settings import APPS_DIR,BASE_DIR
from .settings import SITE_ROOT


def extract_url(module):
    return path('%s%s/' % (SITE_ROOT(), module["name"]), include('%s.urls' % module["name"]))


def local_urls():
    LOCAL_CONF = load_local_conf(BASE_DIR)
    return [*map(extract_url, LOCAL_CONF["modules"])]