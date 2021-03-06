# -*- coding: utf-8 -*-
"""
 @Time    : 2021/2/6 19:03
 @Author  : GeHH
 功能 : 组装requests请求的测试数据
"""
from public.read_case import ReadCase
from public.log import SysLogger
import requests


class AssemblyRequest:

    def __init__(self):
        self.__reader = ReadCase()
        # 测试用例数据
        self.cases = self.__reader.get_case_data()
        # 接口请求对象
        self.request = requests.Session()
        # 获取日志器
        self.log = SysLogger().get_logger()

    # 选择请求方法
    def request_method(self, method, url, **kwargs):
        # 转小写
        method = method.lower()
        response = None
        if method == 'post':
            response = self.request.post(url, **kwargs)
        elif method == 'get':
            response = self.request.get(url, **kwargs)
        elif method == 'delete':
            response = self.request.delete(url, **kwargs)
        elif method == 'put':
            response = self.request.put(url, **kwargs)
        else:
            # 待补充测试方法
            ...
        return response

    def api_request(self, req_url, req_method, req_header, req_params_type, req_params_locate, req_params):

        self.log.info(f'请求url: {req_url}')
        self.log.info(f'请求方法: {req_method}')
        self.log.info(f'请求头: {req_header}')
        self.log.info(f'请求参数类型: {req_params_type}')
        self.log.info(f'请求参数: {req_params}')

        response = None
        # 请求参数格式为x-www-form-urlencoded
        if req_params_type == 'x-www-form-urlencoded':
            # 请求参数放置在消息体中
            if req_params_locate == 'body':
                response = self.request_method(method=req_method,
                                               url=req_url,
                                               data=req_params,
                                  )
            # 请求参数位置在url中
            elif req_params_locate == 'url':
                response = self.request_method(method=req_method,
                                               url=req_url,
                                               params=req_params,
                                               headers=req_header)
        # 请求头格式为json
        elif req_params_type == 'application/json':
            response = self.request_method(method=req_method,
                                           url=req_url,
                                           json=req_params)

        return response


