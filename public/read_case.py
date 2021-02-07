# -*- coding: utf-8 -*-
"""
 @Time    : 2021/2/6 18:00
 @Author  : GeHH
 功能 : 封装从测试用例excel文件中读取案例的方法
"""
from public.excel_library import ExcelLibrary
from config import Config
import os


class ReadCase:

    def __init__(self):
        self.filepath = Config.dataDir + os.sep + 'testcases.xlsx'

        # excel文件读取对象
        self.xlsx_reader = ExcelLibrary(self.filepath)

    # 读取带行号的用例编号
    def get_case_id_and_row(self):
        """
        :return: 所有测试用例编号及对应行号, 类型为列表
        """
        # 用例起始行
        start_rows = 2
        # 总行数
        max_rows = self.xlsx_reader.get_maxrows()
        # 用例编号所在列
        case_id_column = 3

        cases = self.xlsx_reader.extract_the_column(start_rows, max_rows, case_id_column)

        return cases

    # 读取用例行号
    def get_case_rows(self):
        case_row = list()
        cases = self.get_case_id_and_row()
        for case in cases:
            case_row.append(case[0])
        return case_row

    # 读取用例编号
    def get_case_id(self):
        case_id = list()
        cases = self.get_case_id_and_row()
        for case in cases:
            case_id.append(case[1])
        return case_id

    # 根据用例标题, 读取每一行测试用例数据
    def get_case_data(self):
        # 定义字典存储用例数据
        case_datas = {}
        # 获取用例编号
        case_id_list = self.get_case_id_and_row()
        for case in case_id_list:
            # 根据case_id所在的行数, 来获取改行的测试数据
            # 用例对应行
            case_row = case[0]
            # 用例编号
            case_id = case[1]
            # 数据开始列
            start_column = 5
            # 数据结束列
            end_column = self.xlsx_reader.get_maxcolumn()
            # 获取用例行数据
            datas = self.xlsx_reader.extract_the_row(start_column, end_column, case_row)

            # 数据序列化(部分字符串转化为字典)
            # 新数据
            new_data = list()
            for data in datas:
                try:
                    if data.startswith('{') and data.endswith('}'):
                        # str转化成字典
                        new_data.append(eval(data))
                    else:
                        new_data.append(data)
                except:
                    continue
            # 用例数据首位添加行号
            new_data.insert(0, case_row)
            case_datas[case_id] = new_data

        return case_datas

    # 获取符合pytest参数化的数据
    def get_params(self):
        params = list()

        cases = self.get_case_data()

        for case in cases.values():
            params.append(tuple(case[:8]))

        return params

    # 写入测试结果
    def write_test_result(self, row, status):
        # 用例测试结果列
        test_result_column = 12

        self.xlsx_reader.write_to_unit(row, test_result_column, status)


if __name__ == '__main__':
    rd = ReadCase()
    print(rd.get_case_id())


