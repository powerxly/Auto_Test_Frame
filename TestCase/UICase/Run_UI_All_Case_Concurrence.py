# -*- coding: utf-8 -*-
# @Time    : 2019/12/2 10:33
# @Author  : 洋燚
# @Email   : jasonleeyag@163.com
#并发执行某一个用例
import os
import sys
import time
import unittest
from multiprocessing.dummy import Pool as ThreadPool
import random,time
sys.path.append("F:\\CODE\\Auto_Test_Framework")
from report.Runner.HTMLTestRunner3 import HTMLTestRunner
#并发数
threadNum = 5
# 用例路径
case_path = os.path.join(os.getcwd())
# 报告存放路径
report_path = os.path.join(os.getcwd(), "report")
def create_suite():
    TestSuite = unittest.TestSuite()  # 测试集
    test_dir = os.path.dirname(os.getcwd()) + '\\UICase\\'
    discover = unittest.defaultTestLoader.discover(start_dir=test_dir,pattern='Test_*.py',top_level_dir=None)
    for test_case in discover:
        TestSuite.addTests(test_case)
        # print(test_case)
    return TestSuite

def report():
    if len(sys.argv) > 1:
        report_name = os.path.dirname(os.getcwd()) + '\\UICase\\report\\' + sys.argv[1] + '_result.html'
    else:
        now = time.strftime("%Y-%m-%d_%H_%M_%S_")
        # 需要查看每段时间的测试报告，可以这样写：
        report_name = os.path.dirname(os.path.dirname(os.getcwd())) + '\\report\\'+now+'result.html'
    return report_name

def run_case(case_id):
    run_time = random.randrange(1,10)
    time.sleep(run_time)
    TestSuite = create_suite()
    fp = open(report(), 'wb')
    Runner = HTMLTestRunner(stream=fp,title='测试报告',description='测试用例执行情况')
    Runner.run(TestSuite)
    fp.close()

pool = ThreadPool(threadNum)
pool.map(run_case, create_suite())
pool.close()
pool.join()