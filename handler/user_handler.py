# coding=utf-8

from handler.main_handler import BaseHandler
from rpc.account_client import AccountOp


class UserLoginHandler(BaseHandler):
    def _post(self):
        email = self.get_argument('email')
        password = self.get_argument('password')

        ret = AccountOp.login(email, password)

        self.write({'ret': ret})

    _get = _post
