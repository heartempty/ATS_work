# -*- conding : utf-8 -*-
"""
@author : wangjing
@time : 2018/4/15 0:48

"""
from selenium import webdriver
from pageObject.page_login import PageLogin
from commonMethod.get_login_data import login_data
from commonMethod.web_driver_method import WebDriverMethod
import unittest
import os
import time

class MyTestCases(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.get("https://atstest.xiaoyuanzhao.com/login?next=%2Fmanagecenter")
        self.driver.maximize_window()
        # time.sleep(4)
        self.driver.implicitly_wait(30)

    def tearDown(self):
        # time.sleep(2)

        self.driver.close()

    def test_page_login_1(self):

        i = 1
        while i > 6:

            for j in range(0,6):
                login = PageLogin(self.driver)
                login_user1 = login_data().get_login_data()
                num1 = login_user1[j]["编号"]
                username1 = login_user1[j]["用户名"]
                password1 = login_user1[j]["密码"]
                # print(type(password1))
                login.LoginOn(num1, username1, int(password1))
                time.sleep(2)
                self.assertEqual(login.Title(), "管理中心", msg="测试通过")

            i += 1
            print("testend......")



                # login_result = login_data().write_result(1, "pass")
                # self.driver.back()
                # time.sleep(2)
                # login.LoginOn('222', '123', '123')

    def test_page_login_2(self):
        login = PageLogin(self.driver)
        login_user1 = login_data().get_login_data()
        # login_result = login_data().write_result(2, "pass")
        num2 = login_user1[1]["编号"]
        username2 = login_user1[1]["用户名"]
        password2 = login_user1[1]["密码"]
        login.LoginOn(num2, username2, password2)
        time.sleep(2)
        self.assertEqual(login.Text_1(r'//div[@class="layui-layer-content layui-layer-padding"]'),
                         "必填项不能为空", msg="测试通过")
        # self.assertEqual(login.Title(),"管理中心",msg="不测试通过")
        login_result = login_data().write_result(2, "pass")

    def test_page_login_3(self):
        login = PageLogin(self.driver)
        login_user1 = login_data().get_login_data()
        # login_result = login_data().write_result(3, "pass")
        num3 = login_user1[2]["编号"]
        username3 = login_user1[2]["用户名"]
        password3 = login_user1[2]["密码"]
        login.LoginOn(num3, int(username3), int(password3))
        time.sleep(2)
        self.assertEqual(login.Text_1(r'//div[@class="layui-layer-content"]'),
                         "账号或者密码错误!", msg="测试通过")
        # self.assertEqual(login.Title(),"管理中心",msg="不测试通过")
        login_result = login_data().write_result(3, "pass")

    def test_page_login_4(self):
        login = PageLogin(self.driver)
        login_user1 = login_data().get_login_data()
        # login_result = login_data().write_result(4, "pass")
        num4 = login_user1[3]["编号"]
        username4 = login_user1[3]["用户名"]
        password4 = login_user1[3]["密码"]
        login.LoginOn(num4, username4, password4)
        time.sleep(2)
        self.assertEqual(login.Text_1(r'//div[@class="layui-layer-content"]'),
                         "账号或者密码错误!", msg="测试通过")
        # self.assertEqual(login.Title(),"管理中心",msg="不测试通过")
        login_result = login_data().write_result(4, "pass")

    def test_page_login_5(self):
        login = PageLogin(self.driver)
        login_user1 = login_data().get_login_data()
        # login_result = login_data().write_result(5, "pass")
        num5 = login_user1[4]["编号"]
        username5 = login_user1[4]["用户名"]
        password5 = login_user1[4]["密码"]
        login.LoginOn(num5, username5, password5)
        time.sleep(2)
        login_result = login_data().write_result(5, "fail")
        self.assertEqual(login.Text_1(r'//div[@class="layui-layer-content"]'),
                         "账号或者密码错误! ", msg="测试不通过")
        print("-" * 50)
        # self.assertEqual(login.Title(),"管理中心",msg="不测试通过")

    def test_page_login_6(self):
        login = PageLogin(self.driver)
        login_user1 = login_data().get_login_data()
        num1 = login_user1[0]["编号"]
        username1 = login_user1[0]["用户名"]
        password1 = login_user1[0]["密码"]
        login.LoginOn(num1, username1, int(password1))
        time.sleep(2)
        login.Back()
        time.sleep(2)
        self.assertEqual(login.Get_att(r'//input[@class="layui-input"]', 'value'), '007')
        # self.assertIs(login.Get_att(r'//input[@class="layui-input"]','value'),'007')
        # self.assertEqual(login.Get_att(r'//input[@id="userName"]','value'),"wangjing")
        # login_result = login_data.write_result(6,"pass")


if __name__ == "__main__":
    unittest.main()
