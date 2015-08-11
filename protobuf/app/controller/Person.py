import tornado.web

class PersonHandler(tornado.web.RequestHandler):
    def get(self):
        self.render('helloworld.html')
