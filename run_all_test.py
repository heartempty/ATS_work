# -*- conding : utf-8 -*-
"""
@author : wangjing
@time : 2018/4/15 1:48

"""
from commonMethod import HTMLTestRunner
from time import strftime, localtime, time
from unittest import defaultTestLoader
import os

if __name__ == "__main__":
    testcase_path = os.path.abspath("testCase")
    report_path = os.path.abspath("testReport")
    dis = defaultTestLoader.discover(testcase_path, pattern='*test.py', top_level_dir=None)
    now = strftime("%Y%m%d%H%M%S", localtime(time()))
    filename = report_path + '\\' + now + "ats_test_report.html"
    fb = open(filename, "wb")
    runner = HTMLTestRunner.HTMLTestRunner(stream=fb,
                                           verbosity=2,
                                           title="ats登陆测试报告",
                                           description="首页登陆测试详情")
    runner.run(dis)
    fb.close()
