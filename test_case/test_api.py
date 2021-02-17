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
        # 写入文件对象
        self.writer = ReadCase()
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
        self.log.info(f'响应消息: {result}')
        try:
            self.log.info(f'响应结果断言: <响应结果>{result} == <预期结果>{except_result}')
            if except_result == "none":
                # 未指定预期结果的, 忽略
                self.writer.write_test_result(case_row, "IGNORE")
                self.log.info('写入测试结果: IGNORE')
            else:
                assert result == except_result
                # 写入测试结果
                self.writer.write_test_result(case_row, "PASS")
                self.log.info('写入测试结果: PASS')

        except:
            # 写入测试结果
            self.writer.write_test_result(case_row, "FAIL")
            self.log.error('写入测试结果: FAIL')
            raise

