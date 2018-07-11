# -*- conding : utf-8 -*-
"""
@author : wangjing
@time : 2018/4/15 0:13

"""
from selenium import webdriver
from commonMethod.web_driver_method import WebDriverMethod


class PageLogin(WebDriverMethod):
    num_input = r'//input[@class="layui-input"]'
    username_input = r'//input[@id="userName"]'
    password_input = r'//input[@id="password"]'
    # remember_click = r'//i[@class="layui-icon"]'
    remember_click = r'//div[@class ="sign"]'
    login_button = r'//button[@class="layui-btn layui-btn-fluid"]'

    def LoginOn(self, num, uname, pw):
        self.ClearAndInput(self.num_input, num)
        self.Send_key(self.num_input, num)
        self.ClearAndInput(self.username_input, uname)
        self.Send_key(self.username_input, uname)
        self.ClearAndInput(self.password_input, pw)
        self.Send_key(self.password_input, pw)
        self.Remember(self.remember_click)
        self.Click(self.login_button)


    # def Clear(self, num, uname, pw):
    #     self.ClearAndInput(self.num_input, num)
    #     self.num_input
    # def LoginOn(self,loc,value):
    #     self.ClearAndInput(self.num_input, value)
    #     self.Send_key(self.num_input, value)
    #     self.ClearAndInput(self.username_input, value)
    #     self.Send_key(self.username_input, value)
    #     self.ClearAndInput(self.password_input, value)
    #     self.Send_key(self.password_input, value)
    #     self.Click(self.remember_click)
    #     self.Click(self.login_button)
