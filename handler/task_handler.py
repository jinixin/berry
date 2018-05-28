# coding=utf-8

from handler.main_handler import MainHandler
from model import Task
from tool import NumTool


class TaskListHandler(MainHandler):
    def _get(self):
        page = NumTool.str2int(self.get_argument('page', 0))  # 默认会去除前后的空格
        count = NumTool.str2int(self.get_argument('count', 50))

        return self.write({'ret': Task.list(page=page, count=count)})
