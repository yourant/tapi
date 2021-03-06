#!/usr/bin/python
# -*- coding:utf-8 _*-
"""
@author:TXU
@file:DingConfig.py
@time:2021/07/29
@email:xutao@dustess.com
@description:
"""
from crontab import CronTab
import sys


def task_end_timing():
    my_user_cron = CronTab(user=True)
    my_user_cron.remove_all(comment=sys.argv[1])
    my_user_cron.remove_all(comment=sys.argv[1]+"_开始")
    my_user_cron.remove_all(comment=sys.argv[1]+"_结束")
    my_user_cron.write()


if __name__ == '__main__':
    task_end_timing()
