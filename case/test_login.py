# -*- coding:utf-8 -*-
"""
Created on 2017年5月5日
@author: lt
"""
import json
import unittest

import HTMLTestRunner
import ddt

from Common.check_result import check
from Common.requestSend import send_request


# 读取测试用例
with open("./case/Login.json", 'r', encoding="utf-8") as load_f:
    login_dict = json.load(load_f)


@ddt.ddt
class Login(unittest.TestCase):

    @ddt.data(*login_dict)
    def test_login(self, case_data):
        # 发送测试请求
        code, data = send_request(case_data)
        # 校验测试结果
        check(case_data, code, data)


if __name__ == '__main__':
    suite = unittest.defaultTestLoader.discover('.', 'test*.py')
    fp = open("1.html", 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp,
                                           title='test_report',
                                           description='mamainst_test_interface')
    runner.run(suite)

