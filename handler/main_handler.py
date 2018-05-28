# coding=utf-8

import json

import tornado.ioloop
import tornado.web


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        return self.finish(json.dumps(self._get()))

    def post(self):
        return self.finish(json.dumps(self._post()))

    def _get(self):
        pass

    def _post(self):
        pass
