# coding=utf-8

import tornado.ioloop
import tornado.web

from handler.task_handler import TaskListHandler


class TestHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello, world")


def make_app():
    return tornado.web.Application([
        (r'/', TestHandler),
        (r'/task/list', TaskListHandler),
    ])


if __name__ == "__main__":
    app = make_app()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()
