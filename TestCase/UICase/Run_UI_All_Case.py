#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author  : Vant
# @Email   : 944921374@qq.com

import os
import sys
import time
import unittest
from tomorrow import threads

sys.path.append("F:\\CODE\\Auto_Test_Framework")
from report.Runner.HTMLTestRunner3 import HTMLTestRunner

def create_suite():
    TestSuite = unittest.TestSuite()  # 测试集
    test_dir = os.path.dirname(os.getcwd()) + '\\UICase\\'
    # print(test_dir)

    discover = unittest.defaultTestLoader.discover(
        start_dir=test_dir,
        pattern='Test_*.py',
        top_level_dir=None
    )

    for test_case in discover:
        TestSuite.addTests(test_case)
        # print(test_case)
    return TestSuite

def report():
    if len(sys.argv) > 1:
        report_name = os.path.dirname(os.getcwd()) + '\\UICase\\report\\' + sys.argv[1] + '_result.html'
        #parent_path = os.path.dirname(os.path.dirname(os.getcwd()))
    else:
        now = time.strftime("%Y-%m-%d_%H_%M_%S_")
        # 需要查看每段时间的测试报告，可以这样写：
        #report_name = os.getcwd() + '\\report\\'+now+'result.html'
        report_name = os.path.dirname(os.path.dirname(os.getcwd())) + '\\report\\'+now+'result.html'
        #report_name = os.path.dirname(os.getcwd()) + '\\UICase\\report\\result.html'
        #report_name = os.path.dirname(os.path.dirname(os.getcwd())) + '\\report\\UIAutoTest_result.html'
    return report_name

if __name__ == '__main__':
    TestSuite = create_suite()
    fp = open(report(), 'wb')
    Runner = HTMLTestRunner(
        stream=fp,
        title='测试报告',
        description='测试用例执行情况'
    )
    Runner.run(TestSuite)
    fp.close()
# @threads(3)
# def run_case(create_suite,report,nth=0):
#     fp = open(report(), 'wb')
#     Runner = HTMLTestRunner(
#         stream=fp,
#         title='测试报告',
#         description='测试用例执行情况'
#     )
#     Runner.run(create_suite)
#     fp.close()
#
# if __name__ == '__main__':
#     cases = create_suite()
#
#     for i, j in zip(cases, range(len(list(cases)))):
#         run_case(i, nth=j) # 执行用例，生成报告