# -*- coding: utf-8 -*-
"""
 @Time    : 2021/2/7 12:15
 @Author  : GeHH
 功能 : 路径配置
"""
import os


class Config:
    # 项目根目录
    projectDir = os.path.abspath(os.path.dirname(__file__))

    # 测试用例目录
    testCaseDir = os.path.join(projectDir, 'test_case')

    # 测试报告目录
    reportDir = os.path.join(projectDir, 'report')

    # 日志文件目录
    logDir = os.path.join(projectDir, 'log')

    # 接口测试用例数据
    dataDir = os.path.join(projectDir, 'data')






