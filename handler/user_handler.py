# coding=utf-8

from handler.main_handler import BaseHandler
from model import User


class UserLoginHandler(BaseHandler):
    def _post(self):
        email = self.get_argument('email')
        password = self.get_argument('password')

        ret = int(User.login(email, password))

        self.write({'ret': ret})

    _get = _post
