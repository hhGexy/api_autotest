# -*- coding: utf-8 -*-
"""
 @Time    : 2021/2/7 14:17
 @Author  : GeHH
 功能 : 用例执行前置操作
"""

import pytest
from config import Config
import os


# 检查接口测试用例文件是否打开
@pytest.fixture(scope='session', autouse=True)
def check_file_status():
    file_path = Config.dataDir
    file_name = 'testcases.xlsx'
    temp_file = file_path + os.sep + '~$' + file_name

    if os.path.exists(temp_file):
        raise PermissionError('接口测试用例文件处于打开状态, 请关闭')




