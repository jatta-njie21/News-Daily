import json
import os
from django.conf import settings


def load_local_conf(BASE_DIR, conf_file_param = "local_setup.json" ):

    conf_file_path = os.path.join(BASE_DIR,conf_file_param)
    with open(conf_file_path) as conf_file:
        return json.load(conf_file)