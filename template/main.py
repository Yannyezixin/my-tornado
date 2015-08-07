import os.path
import tornado.web
import tornado.httpserver
import tornado.ioloop
import tornado.options

from tornado.options import define, options
define("port", default=8080, help="run on the server", type=int)

class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        self.render('index.html')

class JobPageHandler(tornado.web.RequestHandler):
    def post(self):
        name = self.get_argument('name')
        age = self.get_argument('age')
        job = self.get_argument('job')
        self.render('job.html', name = name, age = age, job = job)

if __name__ == "__main__":
    tornado.options.parse_command_line()
    app = tornado.web.Application(
        handlers = [
            (r'/', IndexHandler),
            (r'/job', JobPageHandler)
        ],
        template_path=os.path.join(os.path.dirname(__file__), "templates")
    )
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()
