# coding=utf-8

import time
from bson.objectid import ObjectId
from base.mongo_base import db


class Task(object):
    collection = db['task']

    task_id = '_id'
    title = 'ti'
    create_time = 'ct'
    start_time = 'st'
    end_time = 'et'
    status = 's'
    level = 'lv'
    own_user = 'ou'

    @classmethod
    def to_dict(cls, obj):
        if not obj:
            return {}

        return {
            'task_id': str(obj[cls.task_id]),
            'title': obj[cls.title],
            'create_time': obj[cls.create_time],
            'start_time': obj.get(cls.start_time, -1),
            'end_time': obj.get(cls.end_time, -1),
            'status': obj[cls.status],
            'level': obj[cls.level],
            'own_user': obj[cls.own_user]
        }

    @classmethod
    def insert(cls, user_id, title):
        ret = cls.collection.insert_one({
            cls.task_id: ObjectId(),
            cls.title: title,
            cls.create_time: int(time.time()),
            cls.status: 0,
            cls.level: 0,
            cls.own_user: user_id,
        })

        return ret.inserted_id if ret else None

    @classmethod
    def find(cls, task_id):
        ret = cls.collection.find_one(filter={cls.task_id: task_id})
        return cls.to_dict(ret)

    @classmethod
    def list(cls, page=0, count=20):
        ret = cls.collection.find(skip=page * count, limit=count)
        return [cls.to_dict(item) for item in ret]
