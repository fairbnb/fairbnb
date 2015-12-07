import urllib

import tornado.ioloop
import tornado.web
import json
import os
import random
from platform import system

import flow

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("main.html")

class searchHandler(tornado.web.RequestHandler):
    def get(self):
        print(flow.userQuery())

class getInfo(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        (movie_name, movie_image) = movies[random.randrange(20)]
        (food_name, food_image) = foods[random.randrange(20)]
        json_dict = {"movieId": random.randrange(5), "movieName": movie_name, "movieImage": movie_image,
                     "recipeId": random.randrange(5), "recipeName": food_name, "recipeImage": food_image}
        self.finish(json.dump(json_dict, self))

settings = dict(
    static_path=os.path.join(os.path.dirname(__file__), "static")
)


def make_app():
    return tornado.web.Application([
        (r"/", MainHandler),
        (r"/search", searchHandler)
    ], **settings)


if __name__ == "__main__":
    if system() == "Windows":
        port = 8888
    else:
        port = 8000
    app = make_app()
    app.listen(port)
    tornado.ioloop.IOLoop.current().start()
