# coding=utf-8

from pymongo import MongoClient

client = MongoClient('localhost', 27018)
db = client.novel