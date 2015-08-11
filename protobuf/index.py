import tornado.httpserver
import tornado.web
import tornado.options
import tornado.ioloop
from app import Application
from tornado.options import options, define

define("port", default=8080, help="run on the given port", type=int)


if __name__ == "__main__":
    tornado.options.parse_command_line()
    http_server = tornado.httpserver.HTTPServer(Application())
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()

