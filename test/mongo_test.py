# coding=utf-8

import time

import unittest

from model.task import Task


class TestMongo(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_insert(self):
        title = '[TEST]后台修复日程表异常%s' % int(time.time())
        magic = Task.insert(1, title)
        task = Task.find(magic)
        self.assertEqual(title, task['title'])


if __name__ == '__main__':
    unittest.main()
