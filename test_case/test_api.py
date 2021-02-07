# -*- coding: utf-8 -*-
"""
 @Time    : 2021/2/6 23:16
 @Author  : GeHH
 功能 : 
"""
import pytest
from public.web_api import AssemblyRequest
from public.read_case import ReadCase
from public.log import SysLogger
import time


# 测试参数化数据及测试用例编号
def params():
    case_reader = ReadCase()
    return case_reader.get_params(), case_reader.get_case_id()

class TestAPI:

    def setup_class(self):
        self.reader = ReadCase()
        self.request = AssemblyRequest()
        self.log = SysLogger.get_logger()

    @pytest.mark.parametrize(
        "case_row, req_url, req_method, req_header, req_params_type, req_params_locate, req_params, except_result",
        params()[0],
        ids=params()[1]
    )
    def test_api(self, case_row, req_url, req_method, req_header, req_params_type, req_params_locate, req_params, except_result):
        response = self.request.api_request(req_url, req_method, req_header, req_params_type, req_params_locate, req_params)
        result = response.json()
        # try:
        self.log.info(f'响应结果断言: {result} == {except_result}')
        try:
            assert result == except_result
            # 写入测试结果
            self.reader.write_test_result(case_row, "PASS")
            self.log.info('写入测试结果: PASS')
            self.log.info('测试通过')
        except PermissionError:
            self.log.error('测试用例文件处于打开状态, 请关闭')
        except:
            self.log.info('测试不通过')
            # 写入测试结果
            self.reader.write_test_result(case_row, "FAIL")
            self.log.error('写入测试结果: FAIL')
            raise

