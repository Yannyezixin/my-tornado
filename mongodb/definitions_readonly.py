import tornado.httpserver
import tornado.web
import tornado.options
import tornado.ioloop
import pymongo

from tornado.options import options, define
define("port", default=8080, help="run on the given port", type=int)

class Application(tornado.web.Application):
    def __init__(self):
        handlers = [
            (r"/(\w+)", WordHandler)
        ]
        conn = pymongo.MongoClient("localhost", 27017)
        self.db = conn.book
        tornado.web.Application.__init__(self, handlers, debug = True)


class WordHandler(tornado.web.RequestHandler):
    def get(self, word):
        coll = self.application.db.book
        word_doc = coll.find_one({"word": word})
        if word_doc:
            del word_doc['_id']
            self.write(word_doc)
        else:
            self.set_status(404)
            self.write({"error": "word not found"})

if __name__ == "__main__":
    tornado.options.parse_command_line()
    http_server = tornado.httpserver.HTTPServer(Application())
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()

