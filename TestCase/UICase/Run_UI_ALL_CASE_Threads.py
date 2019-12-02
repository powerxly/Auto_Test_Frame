# -*- coding: utf-8 -*-
# @Time    : 2019/12/2 10:33
# @Author  : 洋燚
# @Email   : jasonleeyag@163.com
# coding=utf-8
import threading
import unittest
import os,time
from BeautifulReport import BeautifulReport
from multiprocessing import Process
from report.Runner.HTMLTestRunner3 import HTMLTestRunner
import datetime
from tomorrow3 import threads
curpath = os.path.dirname(os.path.realpath(__file__))
casepath = os.path.join(curpath)
reportpath = os.path.join(os.path.dirname(os.path.dirname(os.getcwd())),"report")


def add_case(case_path=casepath, rule="Test_*.py"):
    '''加载所有的测试用例'''
    discover = unittest.defaultTestLoader.discover(case_path,
                                                   pattern=rule,
                                                   top_level_dir=None)
    return discover

@threads(5)
def run_case(all_case, report_path=reportpath, nth=0):
    '''执行所有的用例, 并把结果写入测试报告'''
    now = time.strftime("%Y-%m-%d_%H_%M_%S_")
    report_name = now+'result.html'
    # report_abspath = os.path.join(report_path, "result%s.html" % nth)
    # fp = open(report_abspath, "wb")
    result = BeautifulReport(all_case)
    result.report(filename=report_name, description='自动化测试报告AION', log_path=report_path)
    #runner = BeautifulReport(stream=fp, title='自动化测试报告,测试结果如下：', description='用例执行情况：')
    # 调用add_case函数返回值
    # runner.run(all_case)
    # fp.close()

# if __name__ == "__main__":
#
#     cases = add_case()
#     # 之前是批量执行，这里改成for循环执行
#     for i, j in zip(cases, range(len(list(cases)))):
#         run_case(i, nth=j)  # 执行用例，生成报告
if __name__ == "__main__":
    cases = add_case()
    print(cases)
    for i in cases:
        print(i)
        run_case(i)

