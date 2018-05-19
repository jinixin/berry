# coding=utf-8

from base.mongo_base import db


class User(object):
    collection = db['user']

    id = '_id'
    email = 'el'
    password = 'pd'
    role = 'rl'
