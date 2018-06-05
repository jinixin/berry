# coding=utf-8

import hashlib

from base.mongo_base import db


class User(object):
    collection = db['user']

    id = '_id'
    email = 'el'
    password = 'pd'
    role = 'rl'  # "0000 0000"八位二进制形式，拥有某项权力，则对应位为1

    @classmethod
    def login(cls, email, pwd):
        target_pwd = hashlib.md5(bytes(pwd, 'utf-8')).hexdigest()
        doc = {
            cls.email: email,
            cls.password: target_pwd,
        }
        ret = cls.collection.count(filter=doc)

        return True if ret else False

    @classmethod
    def register(cls, email, pwd, role=0):
        pwd_md5 = hashlib.md5(bytes(pwd, 'utf-8')).hexdigest()
        doc = {
            cls.email: email,
            cls.password: pwd_md5,
            cls.role: role,
        }
        ret = cls.collection.insert_one(document=doc)

        return True if ret else False
