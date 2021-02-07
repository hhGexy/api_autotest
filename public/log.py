# -*- coding: utf-8 -*-
"""
 @Time    : 2021/2/6 23:39
 @Author  : GeHH
 功能 : 
"""
import logging
import logging.handlers
from config import Config
import os


class SysLogger:

    # 日志存放文件
    LOG_FILE = Config.logDir + os.sep + 'log.log'

    # 新建一个日志器变量
    __logger = None

    @classmethod
    def get_logger(cls):
        # 判断日志器是否为空
        if  not cls.__logger:
            cls.__logger = logging.getLogger('updateSecurity')   # updateSecurity
            cls.__logger.setLevel('DEBUG')  # 设置了这个才会把debug以上的输出到控制台

            # file_handler = logging.FileHandler(cls.LOG_FILE) #输出到文件
            file_handler = logging.handlers.TimedRotatingFileHandler(filename=cls.LOG_FILE,
                                                           when="midnight",
                                                           interval=1,
                                                           backupCount=3,
                                                           encoding="utf-8")

            console_handler = logging.StreamHandler()  #输出到控制台
            file_handler.setLevel('ERROR')     #error以上才输出到文件
            console_handler.setLevel('INFO')   #info以上才输出到控制台

            fmt = '%(asctime)s - %(funcName)s - %(lineno)s - %(levelname)s - %(message)s'
            formatter = logging.Formatter(fmt)
            file_handler.setFormatter(formatter) #设置输出内容的格式
            console_handler.setFormatter(formatter)

            cls.__logger.addHandler(file_handler)    #添加handler
            cls.__logger.addHandler(console_handler)
        return cls.__logger


if __name__ == '__main__':

    SysLogger.get_logger().info('1234')
    SysLogger.get_logger().warning('find warring1')
    SysLogger.get_logger().error('find_error1')

