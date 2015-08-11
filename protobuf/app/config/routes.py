#!/usr/bin/env python
# -*- coding: utf8 -*-

from .. import controller

routes = [
    (r"/", controller.PersonHandler),
    (r"/add", controller.PersonHandler), # post
]
