# -*- coding: utf-8 -*-
# @Time    : 2019/10/29 17:42
# @Author  : 洋燚
# @Email   : jasonleeyag@163.com

import sys,os
import unittest

from Pages.dkPage import dkPage
from Base.BrowserDriver import BrowserDriver
import time

class Test_03lwsjzxwhd(unittest.TestCase):
    #result = {'Status': False}
    global current_timestamp
    current_timestamp = str(int(time.time()))

    def setUp(self):
        driver = BrowserDriver(self)
        self.driver = driver.openbrowser(self)
        openresult = 0
        time.sleep(10)

    def test_1_lwsjzxwhd(self):
        """登录王良起草蓝网数据中心维护单

        :return:
        """
        dk = dkPage(self.driver)
        dk.input_office_username('wangliang1')
        dk.input_office_password('cetcwe123!')
        dk.click_office_btn()
        time.sleep(8)
        # 点击一网通办
        dk.click(['css selector',
                  'body > div.container.normaluser > form > div.usercontent.container-fluid > div > div.col-md-1.leftarea > div.nav > ul > li:nth-child(4) > a'])
        # 等待页面加载
        time.sleep(5)
        # 切换到一网通办首页
        dk.change_to_window(1)
        dk.get_screent_img()
        # 点击事项列表
        dk.click(['css selector', '#itemsList'])
        # 等待页面加载
        time.sleep(1)
        # 搜索事项，蓝网数据中心维护单并点击事项名称
        dk.send_key(['css selector', '#searchForm_itemsList > div > input'], "蓝网数据中心维护单")
        dk.click(['css selector', '[title="蓝网数据中心维护单"]'])
        # 等待页面加载
        time.sleep(5)
        # 点击立即办理
        dk.click(['css selector', '#handle'])
        # 等待页面加载
        time.sleep(3)
        dk.change_to_window(2)
        # 填写表单
        dk.send_key(dkPage.lwsjzxwhd_sxbt,"蓝网数据中心维护单" + current_timestamp)
        dk.send_key(dkPage.lwsjzxwhd_sqr,"王良")
        dk.send_key(dkPage.lwsjzxwhd_whnr,"维护内容" + current_timestamp)
        dk.send_key(dkPage.lwsjzxwhd_bz,"备注" + current_timestamp)

        # #dk.send_key(dkPage.cydwywwtsqd_sqr,"谷岩" + current_timestamp)
        #选择申请日期
        dk.js_execute('''$('#creationTime_view > span:nth-child(3) > span').click()''')
        dk.js_execute('''$('body > div.datetimepicker.datetimepicker-dropdown-bottom-left.dropdown-menu > div.datetimepicker-days > table > thead > tr:nth-child(1) > th.next > i').click()''')
        dk.js_execute('''$('body > div.datetimepicker.datetimepicker-dropdown-bottom-left.dropdown-menu > div.datetimepicker-days > table > tbody > tr:nth-child(3) > td:nth-child(4)').click()''')
        time.sleep(2)
        #选择申请单位#modifyTime_view > span:nth-child(3) > span
        dk.js_execute('''$('#framework-content > table > tbody > tr:nth-child(3) > td:nth-child(2) > div > span > span').click()''')
        time.sleep(1)
        dk.js_execute('''$('#groupTab_17_span').dblclick()''')
        # 选择维护日期
        dk.js_execute('''$('#modifyTime_view > span:nth-child(3) > span').click()''')
        dk.js_execute(
            '''$('body > div.datetimepicker.datetimepicker-dropdown-bottom-left.dropdown-menu > div.datetimepicker-days > table > thead > tr:nth-child(1) > th.next > i').click()''')
        dk.js_execute(
            '''$('body > div.datetimepicker.datetimepicker-dropdown-bottom-left.dropdown-menu > div.datetimepicker-days > table > tbody > tr:nth-child(3) > td:nth-child(4)').click()''')
        time.sleep(2)
        # dk.js_execute('''$('span.btn:nth-child(1) > input:nth-child(2)').click()''')
        # op_file = BrowserDriver(self)
        # op_file.upload_file()
        time.sleep(3)
        try:
            dk.click(['css selector','#control2_view > button:nth-child(4)'])
        except Exception as e:
            print(e)
            self.result['Status'] = True
        time.sleep(10)

    #@unittest.skipIf(result['Status'] == True, '上一条执行失败，跳过此用例')
    def test_2_lwsjzxwhd(self):
        """登录尚国平并查找待办,并且提交待办

        :return:
        """
        dk = dkPage(self.driver)
        dk.input_office_username('shangguoping')
        dk.input_office_password('cetcwe123!')
        dk.click_office_btn()
        time.sleep(15)
        dk.click(['css selector', "#todo-section > a.more"])
        dk.change_to_window(1)
        try:
            dk.send_key(['css selector', '#search_div_active > input'], "蓝网数据中心维护单" + current_timestamp)
            dk.click(['css selector', '#searchButton_active'])
        except Exception as e:
            print(e)
            self.result['Status'] = True
        temptitle = "蓝网数据中心维护单" + current_timestamp
        dk.click(['css selector', "[title=" + temptitle + "]"])
        # self.driver.execute_script('''$([])''')
        dk.change_to_window(2)
        time.sleep(5)
        #title = self.driver.find_element_by_css_selector("#docTitle").get_attribute("value")
        #self.assertEqual(title, temptitle)
        try:
            dk.send_key(['css selector', '#fgldyj\$_opinion_popup_content'], "我是尚国平，请继续流转")
            dk.click(['css selector', '#control2_view > button:nth-child(4)'])
            dk.get_screent_img()
        except Exception as e:
            print(e)
            #self.result['Status'] = True
        # time.sleep(15)
        # dk.change_to_window(1)
        # dk.close()
        # dk.change_to_window(0)
        # dk.click(['xpath', '/html/body/div[3]/form/div[1]/div/div[3]/div[1]/ul/li[1]/i'])
        # dk.click(['css selector', '#control2_view > button:nth-child(4)'])
        time.sleep(10)


    #@unittest.skipIf(result['Status'] == True, '上一条执行失败，跳过此用例')
    def test_3_lwsjzxwhd(self):
        """登录许勇并查找待办,并且提交待办

        :return:
        """
        dk = dkPage(self.driver)
        dk.input_office_username('xuyong')
        dk.input_office_password('cetcwe123!')
        dk.click_office_btn()
        time.sleep(15)
        dk.click(['css selector', "#todo-section > a.more"])
        dk.change_to_window(1)
        try:
            dk.send_key(['css selector', '#search_div_active > input'], "蓝网数据中心维护单" + current_timestamp)
            dk.click(['css selector', '#searchButton_active'])
        except Exception as e:
            print(e)
            self.result['Status'] = True
        temptitle = "蓝网数据中心维护单" + current_timestamp
        dk.click(['css selector', "[title=" + temptitle + "]"])
        # self.driver.execute_script('''$([])''')
        dk.change_to_window(2)
        time.sleep(5)
        #title = self.driver.find_element_by_css_selector("#docTitle").get_attribute("value")
        #self.assertEqual(title, temptitle)
        try:
            dk.send_key(['css selector', '#jtldyj\$_opinion_popup_content'], "我是许勇，请继续流转")
            dk.click(['css selector', '#control2_view > button:nth-child(4)'])
            dk.get_screent_img()
        except Exception as e:
            print(e)
            #self.result['Status'] = True
        time.sleep(10)

    #@unittest.skipIf(result['Status'] == True, '上一条执行失败，跳过此用例')
    def test_4_lwsjzxwhd(self):
        """登录杨军并查找待办,并且提交待办

        :return:
        """
        dk = dkPage(self.driver)
        dk.input_office_username('yangjun10')
        dk.input_office_password('cetcwe123!')
        dk.click_office_btn()
        time.sleep(15)
        dk.click(['css selector', "#todo-section > a.more"])
        dk.change_to_window(1)
        try:
            dk.send_key(['css selector', '#search_div_active > input'], "蓝网数据中心维护单" + current_timestamp)
            dk.click(['css selector', '#searchButton_active'])
        except Exception as e:
            print(e)
            #self.result['Status'] = True
        temptitle = "蓝网数据中心维护单" + current_timestamp
        dk.click(['css selector', "[title=" + temptitle + "]"])
        # self.driver.execute_script('''$([])''')
        dk.change_to_window(2)
        time.sleep(5)
        title = self.driver.find_element_by_css_selector("#docTitle").get_attribute("value")
        self.assertEqual(title, temptitle)
        try:
            dk.send_key(['css selector', '#jtldyj\$_opinion_popup_content'], "我是杨军，请继续流转")
            dk.click(['css selector', '#control2_view > button:nth-child(4)'])
            dk.get_screent_img()
        except Exception as e:
            print(e)
            #self.result['Status'] = True
        time.sleep(10)

    #@unittest.skipIf(result['Status'] == True, '上一条执行失败，跳过此用例')
    def test_5_lwsjzxwhd(self):
        """登录尚国平并查找待办,并且提交待办

        :return:
        """
        dk = dkPage(self.driver)
        dk.input_office_username('shangguoping')
        dk.input_office_password('cetcwe123!')
        dk.click_office_btn()
        time.sleep(15)
        dk.click(['css selector', "#todo-section > a.more"])
        dk.change_to_window(1)
        try:
            dk.send_key(['css selector', '#search_div_active > input'], "蓝网数据中心维护单" + current_timestamp)
            dk.click(['css selector', '#searchButton_active'])
        except Exception as e:
            print(e)
            #self.result['Status'] = True
        temptitle = "蓝网数据中心维护单" + current_timestamp
        dk.click(['css selector', "[title=" + temptitle + "]"])
        # self.driver.execute_script('''$([])''')
        dk.change_to_window(2)
        time.sleep(5)
        title = self.driver.find_element_by_css_selector("#docTitle").get_attribute("value")
        self.assertEqual(title, temptitle)
        try:
            dk.send_key(['css selector', '#jtldyj\$_opinion_popup_content'], "我是尚国平，流程结束")
            dk.click(['css selector', '#control2_view > button:nth-child(4)'])
            dk.get_screent_img()
        except Exception as e:
            print(e)
            #self.result['Status'] = True
        time.sleep(10)

    def tearDown(self):
        self.driver.quit()

    if __name__ == "__main__":
        unittest.main()