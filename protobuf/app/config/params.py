#!/usr/bin/env python
# -*- coding: utf8 -*-

import os

params = {
    'app_dir_name': 'app',
    'app_root': os.path.abspath('..'),
}

settings = {
    'template_path': os.path.join(os.path.abspath('.'), params['app_dir_name'], 'views'),
    'static_path': os.path.join(os.path.abspath('.'), params['app_dir_name'], 'assets'),
}
