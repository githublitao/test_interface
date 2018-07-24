# -*- coding:utf-8 -*-
"""
Created on 2017年5月5日

@author: lt
"""
import configparser
import logging

import Common.Path
logger = logging.getLogger(__name__)  # 这里使用 __name__ 动态搜索定义的 logger 配置，这里有一个层次关系的知识点。


class ConfigEmail:

    # 读取邮件发送配置信息
    def __init__(self, file=Common.Path.email_path()):
        config = configparser.ConfigParser()
        config.read(file)
        try:
            self.sender = config['email_address']['Sender']  # 发件人地址
            self.smtp = config['email_address']['smtp']  # 第三方smtp，例如网易的，smtp.163.com
            self.login = config['email_address']['login']  # 授权登录账号
            self.AuthorizationCode = config['email_address']['AuthorizationCode']  # 授权码
            self.to = config['email_address']['to']  # 收件人
        except Exception as e:
            print('%s', e)

    def get_sender(self):
        return self.sender

    def get_smtp(self):
        return self.smtp

    def get_login(self):
        return self.login

    def get_authorization_code(self):
        return self.AuthorizationCode

    def get_to(self):
        return self.to


if __name__ == '__main__':
    email = ConfigEmail("../email_address.ini")
    print(email.get_smtp())
    print(email.get_sender())
    print(email.get_login())
    print(email.get_authorization_code())
    print(email.get_to())
