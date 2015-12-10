import urllib

import dateFuctions
import tornado.ioloop
import tornado.web
import json
import os
import time
from platform import system

import flow

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        print("main.html")
        self.render("main.html")

class searchHandler(tornado.web.RequestHandler):
    def get(self):
        print("search handler")
        checkin = self.get_argument("checkIn")
        checkout = self.get_argument("checkOut")
        print("query from: " + dateFuctions.printTime(checkin))
        print("query until: " + dateFuctions.printTime(checkout))
        if int(checkin) >= time.time():
            result = flow.userQuery(checkin, checkout)
            result = json.dumps(result)
            # result = {'results':result}
        else:
            self.set_status(404)
            result = json.dumps("")
        self.finish(result)
        print('sent result')

settings = dict(
    static_path=os.path.join(os.path.dirname(__file__), "static")
)


def make_app():
    print("make_app")
    return tornado.web.Application([
        (r"/", MainHandler),
        (r"/search", searchHandler)
    ], **settings)


if __name__ == "__main__":
    if system() == "Windows":
        port = 8888
    else:
        port = 80
    app = make_app()
    app.listen(port)
    tornado.ioloop.IOLoop.current().start()
