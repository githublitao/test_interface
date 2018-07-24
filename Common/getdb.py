# -*- coding:utf-8 -*-
"""
Created on 2017年6月1日

@author: lt
"""
import logging

import MySQLdb
import configparser

from Common import Path
logger = logging.getLogger(__name__)  # 这里使用 __name__ 动态搜索定义的 logger 配置，这里有一个层次关系的知识点。


# 连接MySql数据库
class MySqlDB:
    def __init__(self):
        config = configparser.ConfigParser()
        config.read(Path.get_db())
        try:
            self.host = config['MySqlDB']['host']
            self.port = config['MySqlDB']['port']
            self.port = int(self.port)
            self.user = config['MySqlDB']['user']
            self.pwd = config['MySqlDB']['pwd']
            self.dateBase = config['MySqlDB']['db']
        except Exception as e:
            logging.error(e)
        try:
            self.db = MySQLdb.connect(self.host+":"+self.port, self.user, self.pwd, self.dateBase, charset='utf8')
        except Exception as e:
            logging.error(e)

    def db_operation(self, sql):
        cursor = self.db.cursor()
        try:
            # 执行sql语句
            cursor.execute(sql)
            # 提交到数据库执行
            self.db.commit()
        except Exception as e:
            # Rollback in case there is any error
            self.db.rollback()
            logging.exception(e)

        # 关闭数据库连接
        self.db.close()
