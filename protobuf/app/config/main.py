#!/usr/bin/env python
# -*- coding: utf8 -*-

from routes import routes
import params
import tornado.web

class Application(tornado.web.Application):
    def __init__(self):
        handers = routes
        self.config = params.params
        settings = {
            "template_path": params.settings['template_path'],
            "static_path": params.settings['static_path'],
        }
        tornado.web.Application.__init__(self, handers, debug = True, **settings)
