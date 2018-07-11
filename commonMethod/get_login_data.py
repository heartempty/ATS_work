# -*- conding : utf-8 -*-
"""
@author : wangjing
@time : 2018/4/15 16:15

"""
import testData
from xlutils.copy import copy
import xlrd
import os


class login_data(object):

    def __init__(self):

        self.file_name = r"login_data.xls"
        self.file_path = os.path.join(os.path.dirname(testData.__file__), self.file_name)

    def get_login_data(self):

        # file_name = "login_data.xlsx"
        #    获取testData路径
        # file_path = os.path.join(os.path.dirname(testData.__file__), file_name)
        # print(file_path)
        dataResult = []
        dictResult = []
        xl = xlrd.open_workbook(self.file_path)
        # s = xl.sheet_names()
        # print(s)
        sheet1 = xl.sheet_by_name("Sheet1")
        # sheet1.nrows 获取sheet行数
        for i in range(0, sheet1.nrows):
            dataResult.append(sheet1.row_values(i))
        for i in range(1, len(dataResult)):
            temp = dict(zip(dataResult[0], dataResult[i]))
            dictResult.append(temp)

        return dictResult
        # print(dictResult)


    # cat = login_data()
    # cat.get_login_data()
    def write_result(self, num, result):
        rb = xlrd.open_workbook(self.file_path)
        rs = rb.sheet_by_index(0)
        wb = copy(rb)
        ws = wb.get_sheet(0)
        # num = 1
        # while num <= 6:
        #     ws.write(num, 3, result)
        #     num += 1
        ws.write(num, 3, result)
        wb.save(self.file_path)
# cat = login_data().write_result(1,"ppp")
# cat = login_data().get_login_data()
# cat = login_data()
# cat.write_result('qwe')

# print(dictResult)
# print(dictResult[0]["编号"])

# print(dataResult)
# print(sheet1.row_values(1))

# num_1 = sheet1.cell_value(1, 0)
# uname_1 = sheet1.cell_value(1, 1)
# password_1 = sheet1.cell_value(1, 2)
# print(num_1)
# print(uname_1)
# print(password_1)
