# coding=utf-8

from thrift.transport import TTransport, TSocket
from thrift.protocol import TBinaryProtocol

from rpc.iaccount import AccountService
from rpc.iaccount.ttypes import AccountInfo


class wget_client(object):
    def __init__(self):
        self.transport = None

    def __enter__(self):
        socket = TSocket.TSocket('127.0.0.1', 8801)
        self.transport = TTransport.TBufferedTransport(socket)
        protocol = TBinaryProtocol.TBinaryProtocol(self.transport)
        client = AccountService.Client(protocol)
        self.transport.open()

        return client

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.transport.close()


def get_client():
    socket = TSocket.TSocket('127.0.0.1', 8801)
    transport = TTransport.TBufferedTransport(socket)
    protocol = TBinaryProtocol.TBinaryProtocol(transport)
    client = AccountService.Client(protocol)
    transport.open()

    return client


class AccountOp(object):
    owner = 'BERRY'
    rpc_client = None

    @classmethod
    def refresh_client(cls):
        if cls.rpc_client is None:
            cls.rpc_client = get_client()

    @classmethod
    def login(cls, email, pwd):
        account = AccountInfo()
        account.auth_id = email
        account.password = pwd
        account.type = cls.owner

        cls.refresh_client()
        return cls.rpc_client.do_login(account)

    @classmethod
    def register(cls, email, pwd, permit=0):
        account = AccountInfo()
        account.auth_id = email
        account.password = pwd
        account.permit = permit
        account.type = cls.owner

        cls.refresh_client()
        return cls.rpc_client.do_register(account)
