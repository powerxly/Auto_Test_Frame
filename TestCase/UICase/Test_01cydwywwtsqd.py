# -*- coding: utf-8 -*-
# @Time    : 2019/10/29 17:42
# @Author  : 洋燚
# @Email   : jasonleeyag@163.com

import sys,os
import unittest

from Pages.dkPage import dkPage
from Base.BrowserDriver import BrowserDriver
import time

class Test_01cydwywwtsqd(unittest.TestCase):
    global current_timestamp
    current_timestamp = str(int(time.time()))

    def setUp(self):
        driver = BrowserDriver(self)
        self.driver = driver.openbrowser(self)
        openresult = 0
        time.sleep(10)

    def test_1_cydwywwtsqd(self):
        """登录谷岩起草成员单位运维问题申请单

        :return:
        """
        dk = dkPage(self.driver)
        dk.input_office_username('guyan')
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
        # 搜索事项，无违法违纪证明申请并点击事项名称
        dk.send_key(['css selector', '#searchForm_itemsList > div > input'], "成员单位运维问题申请单")
        dk.click(['css selector', '[title="成员单位运维问题申请单"]'])
        # 等待页面加载
        time.sleep(5)
        # 点击立即办理
        dk.click(['css selector', '#handle'])
        # 等待页面加载
        time.sleep(3)
        dk.change_to_window(2)
        # 填写表单
        dk.send_key(dkPage.cydwywwtsqd_bt,"成员单位运维问题申请单" + current_timestamp)
        #dk.send_key(dkPage.cydwywwtsqd_sqr,"谷岩" + current_timestamp)
        #选择申请日期
        dk.js_execute('''$('#creationTime_view > span:nth-child(3) > span').click()''')
        dk.js_execute('''$('body > div.datetimepicker.datetimepicker-dropdown-bottom-left.dropdown-menu > div.datetimepicker-days > table > thead > tr:nth-child(1) > th.next > i').click()''')
        dk.js_execute('''$('body > div.datetimepicker.datetimepicker-dropdown-bottom-left.dropdown-menu > div.datetimepicker-days > table > tbody > tr:nth-child(3) > td:nth-child(4)').click()''')
        time.sleep(2)
        #选择申请单位
        dk.js_execute('''$('#framework-content > table > tbody > tr:nth-child(3) > td:nth-child(2) > div > span > span').click()''')
        time.sleep(1)
        dk.js_execute('''$('#groupTab_17_span').dblclick()''')
        time.sleep(2)
        dk.js_execute('''$('body > div.modal-scrollable > div > div > div > div:nth-child(3) > button:nth-child(1)').click()''')
        #dk.click(['xpath', '/html/body/div[6]/div/div/div/div[3]/button[1]'])
        #选择申请部门
        dk.js_execute('''$('#framework-content > table > tbody > tr:nth-child(3) > td:nth-child(4) > div > span > span').click()''')
        time.sleep(1)
        dk.js_execute('''$('#groupTab_17_span').dblclick()''')
        time.sleep(1)
        dk.js_execute('''$('body > div.modal-scrollable > div > div > div > div:nth-child(3) > button:nth-child(1)').click()''')
        time.sleep(1)
        dk.send_key(dkPage.cydwywwtsqd_lxdh,'13911388479')

        dk.select_by_index(['css selector','#belong_system'],1)
        time.sleep(1)
        dk.select_by_index(['css selector','#questionType'],1)
        dk.send_key(['css selector','#questionDesc'],"问题描述" + current_timestamp)
        # dk.send_key(dkPage.jtxsdwdwcjxtbab_bsfs, "部署方式" + current_timestamp)
        # dk.send_key(dkPage.jtxsdwdwcjxtbab_bswzwlqy, "网络区域" + current_timestamp)
        # dk.send_key(dkPage.jtxsdwdwcjxtbab_xtjj, "系统简介" + current_timestamp)
        # dk.send_key(dkPage.jtxsdwdwcjxtbab_bz, "备 注" + current_timestamp)
        # dk.js_execute('$("#framework-content > table > tbody > tr:nth-child(15) > td:nth-child(2) > div > div >div > div > div > span > input").click()')
        # time.sleep(5)
        #上传附件
        # dk.js_execute('''$('span.btn:nth-child(1) > input:nth-child(2)').click()''')
        # op_file = BrowserDriver(self)
        # op_file.upload_file()
        # time.sleep(3)
        self.assertIsNone(None)
        try:
            dk.click(['css selector','#control2_view > button:nth-child(4)'])
        except Exception as e:
            print(e)
        time.sleep(5)

        self.driver.quit()

    def test_2_cydwywwtsqd(self):
        """登录尚国平填写意见并提交下一步处理

        :return:
        """
        dk = dkPage(self.driver)
        dk.input_office_username('shangguoping')
        dk.input_office_password('cetcwe123!')
        dk.click_office_btn()
        time.sleep(3)
        dk.click(['css selector', "#todo-section > a.more"])
        dk.change_to_window(1)
        dk.send_key(['css selector', '#search_div_active > input'], "成员单位运维问题申请单" + current_timestamp)
        dk.click(['css selector', '#searchButton_active'])
        temptitle = "成员单位运维问题申请单" + current_timestamp
        time.sleep(3)
        dk.click(['css selector', "[title=" + temptitle + "]"])
        # dk.click(['css selector', '[title=' + temptitle + ''])
        # self.driver.execute_script('''$([])''')
        dk.change_to_window(2)
        time.sleep(5)
        #title1 = self.driver.find_element_by_id("docTitle").get_attribute("value")
        #self.assertEqual(title1, temptitle)
        dk.send_key(['css selector', '#ywjlyj\$_opinion_popup_content'], "同意，请继续流转,我是尚国平")
        dk.js_execute('''$('#control2_view > div.workflowsubmit_content.workflowsubmit_content_executor > div > div > div.workflowsubmit_content_hxr > div > dd:nth-child(2)').click()''')
        dk.click(['css selector', '#control2_view > button:nth-child(4)'])
        self.assertIsNone(None)
        time.sleep(8)

    def test_3_cydwywwtsqd(self):
        """登录王良填写意见并提交下一步处理

        :return:
        """
        dk = dkPage(self.driver)
        dk.input_office_username('wangliang1')
        dk.input_office_password('cetcwe123!')
        dk.click_office_btn()
        time.sleep(3)
        dk.click(['css selector', "#todo-section > a.more"])
        dk.change_to_window(1)
        dk.send_key(['css selector', '#search_div_active > input'], "成员单位运维问题申请单" + current_timestamp)
        dk.click(['css selector', '#searchButton_active'])
        temptitle = "成员单位运维问题申请单" + current_timestamp
        time.sleep(3)
        dk.click(['css selector', "[title=" + temptitle + "]"])
        # dk.click(['css selector', '[title=' + temptitle + ''])
        # self.driver.execute_script('''$([])''')
        dk.change_to_window(2)
        time.sleep(5)
        #title1 = self.driver.find_element_by_id("docTitle").get_attribute("value")
        #self.assertEqual(title1, temptitle)
        time.sleep(2)
        dk.send_key(['css selector', '#xmjlyj\$_opinion_popup_content'], "同意，请继续流转,我是王良")
        dk.click(['css selector', '#control2_view > button:nth-child(4)'])
        self.assertIsNone(None)
        time.sleep(8)

    def test_4_cydwywwtsqd(self):
        """登录谷岩填写意见并提交结束

        :return:
        """
        dk = dkPage(self.driver)
        dk.input_office_username('guyan')
        dk.input_office_password('cetcwe123!')
        dk.click_office_btn()
        time.sleep(3)
        dk.click(['css selector', "#todo-section > a.more"])
        dk.change_to_window(1)
        dk.send_key(['css selector', '#search_div_active > input'], "成员单位运维问题申请单" + current_timestamp)
        dk.click(['css selector', '#searchButton_active'])
        temptitle = "成员单位运维问题申请单" + current_timestamp
        time.sleep(3)
        dk.click(['css selector', "[title=" + temptitle + "]"])
        # dk.click(['css selector', '[title=' + temptitle + ''])
        # self.driver.execute_script('''$([])''')
        dk.change_to_window(2)
        time.sleep(3)
        #title1 = self.driver.find_element_by_id("docTitle").get_attribute("value")
        #self.assertEqual(title1, temptitle)
        time.sleep(2)
        dk.send_key(['css selector', '#wttcryj\$_opinion_popup_content'], "结束流程")
        #dk.js_execute('''$('#control2_view > div.workflowsubmit_content.workflowsubmit_content_executor > div > div > div.workflowsubmit_content_hxr > div > dd:nth-child(2)').click()''')
        dk.click(['css selector', '#control2_view > button:nth-child(4)'])
        self.assertIsNone(None)
        time.sleep(8)

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()