# -*- coding:utf-8 -*-
"""
Created on 2017年5月5日

@author: lt
"""
# coding:utf-8
import unittest
import os
# 用例路径
import time

from Common.HTMLTestRunner_PY3 import HTMLTestRunner
from testreport.Send_report import send_email

case_path = os.path.join(os.getcwd())

if __name__ == '__main__':
    run_time = time.strftime('%Y-%m-%d_%H_%M_%S', time.localtime(time.time()))
    suite = unittest.defaultTestLoader.discover('.', 'test*.py')
    fp = open(os.getcwd()+"/Report/"+run_time+".html", 'wb')
    runner = HTMLTestRunner(stream=fp,
                            title='自动化测试报告',
                            description='测试报告')
    runner.run(suite)
    fp.close()
    send_email(run_time)
