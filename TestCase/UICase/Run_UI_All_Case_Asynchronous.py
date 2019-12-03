# -*- coding: utf-8 -*-
# @Time    : 2019/12/2 10:33
# @Author  : 洋燚
# @Email   : jasonleeyag@163.com
# coding=utf-8
import threading
import unittest
import os,time
from BeautifulReport import BeautifulReport
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
    result = BeautifulReport(all_case)
    result.report(filename=report_name, description='自动化测试报告AION', log_path=report_path)

if __name__ == "__main__":
    cases = add_case()
    print(cases)
    for i in cases:
        print(i)
        run_case(i)

