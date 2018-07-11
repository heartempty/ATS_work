# -*- conding : utf-8 -*-
"""
@author : wangjing
@time : 2018/4/15 0:04

"""
from selenium import webdriver


class WebDriverMethod(object):

    def __init__(self, driver):
        self.driver = driver

    def open(self):
        self.driver.get(self.url)

    def ClearAndInput(self, loc, value):
        element = self.driver.find_element_by_xpath(loc)
        element.clear()

    def Send_key(self, loc, value):
        self.driver.find_element_by_xpath(loc).send_keys(value)

    # def Send_key_Username(self, loc, value):
    #     self.driver.find_element_by_xpath(loc).send_keys(value)
    #
    # def Send_key_Password(self, loc, value):
    #     self.driver.find_element_by_xpath(loc).send_keys(value)

    def Click(self, loc):
        self.driver.find_element_by_xpath(loc).click()

    # def Text_info(self):
    # self.driver.find_element_by_xpath("//")

    def Text(self):
        return self.driver.text

    def Text_1(self, loc):
        return self.driver.find_element_by_xpath(loc).text

    def Title(self):
        return self.driver.title

    def Remember(self, loc):
        if self.driver.find_element_by_xpath(loc).is_selected():
            return
        else:
            self.driver.find_element_by_xpath(loc).click()

    def Back(self):
        self.driver.back()

    def Get_att(self, loc, value):
        self.driver.find_element_by_xpath(loc).get_attribute(value)
        print(self.driver.find_element_by_xpath(loc).get_attribute(value))


if __name__ == "__main__":
    cat = WebDriverMethod()
