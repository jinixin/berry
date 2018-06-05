# coding=utf-8

import os
import tornado.ioloop
import tornado.web

from handler.task_handler import TaskListHandler, IndexHandler
from handler.user_handler import UserLoginHandler


class TestHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello, world")


def make_app():
    base_path = os.getcwd()
    settings = {
        'template_path': os.path.join(base_path, 'view'),
        'static_path': os.path.join(base_path, 'view/static'),
    }
    return tornado.web.Application(
        handlers=[
            (r'/', IndexHandler),
            (r'/task/list', TaskListHandler),
            (r'/user/login', UserLoginHandler, None, 'user_login'),
        ],
        **settings,
    ).listen(8888)


if __name__ == "__main__":
    make_app()
    tornado.ioloop.IOLoop.current().start()
