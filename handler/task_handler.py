# coding=utf-8

from handler.main_handler import BaseHandler
from model import Task
from tool import NumTool


class TaskListHandler(BaseHandler):
    def _get(self):
        page = NumTool.str2int(self.get_argument('page', 0))  # 默认会去除前后的空格
        count = NumTool.str2int(self.get_argument('count', 50))

        self.render('task_list.html', task_list=Task.list(page=page, count=count))
