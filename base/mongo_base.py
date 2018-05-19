# coding=utf-8

from pymongo import MongoClient

client = MongoClient('localhost', 27019)
db = client.novel