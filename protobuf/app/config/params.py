#!/usr/bin/env python
# -*- coding: utf8 -*-

import os

params = {
    'app_dir_name': 'app',
    'app_root': os.path.abspath('..'),
    'data_dir': os.path.join(os.path.abspath('.'), 'app', 'data'),
    'data_file': os.path.join(os.path.abspath('.'), 'app', 'data', 'proto.data'),
}

settings = {
    'template_path': os.path.join(os.path.dirname(__file__), '..', 'views'),
    'static_path': os.path.join(os.path.dirname(__file__), '..', 'assets'),
}

