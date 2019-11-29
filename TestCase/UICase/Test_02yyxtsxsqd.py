# -*- coding: utf-8 -*-
# @Time    : 2019/11/22 15:23
# @Author  : 洋燚
# @Email   : jasonleeyag@163.com

# -*- coding: utf-8 -*-
# @Time    : 2019/10/29 17:42
# @Author  : 洋燚
# @Email   : jasonleeyag@163.com

import sys,os
import unittest

from Pages.dkPage import dkPage
from Base.BrowserDriver import BrowserDriver
import time

class Test_02yyxtsxsqd(unittest.TestCase):
    case_status = True
    global current_timestamp
    current_timestamp = str(int(time.time()))

    def setUp(self):
        driver = BrowserDriver(self)
        self.driver = driver.openbrowser(self)
        openresult = 0
        time.sleep(10)

    def test_1_yyxtsxsqd(self):
        """登录王良起草成员单位运维问题申请单

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
        dk.send_key(['css selector', '#searchForm_itemsList > div > input'], "WE应用系统上线申请单")
        dk.click(['css selector', '[title="WE应用系统上线申请单"]'])
        # 等待页面加载
        time.sleep(3)
        # 点击立即办理
        dk.click(['css selector', '#handle'])
        # 等待页面加载
        time.sleep(3)
        dk.change_to_window(2)
        # 填写表单
        dk.send_key(dkPage.yyxtsxsqd_bt,"应用系统上线申请单" + current_timestamp)
        dk.send_key(dkPage.yyxtsxsqd_xtmc,"WE" + current_timestamp)
        dk.send_key(dkPage.yyxtsxsqd_sqr,"王良" + current_timestamp)
        dk.send_key(dkPage.yyxtsxsqd_sxbb,"Version" + current_timestamp)
        dk.send_key(dkPage.yyxtsxsqd_sxnr,"Content" + current_timestamp)
        dk.send_key(dkPage.yyxtsxsqd_sxyx,"影响如下：" + current_timestamp)
        dk.send_key(dkPage.yyxtsxsqd_bz,"备注：" + current_timestamp)
        #选择申请日期
        dk.js_execute('''$('#onlineTime_view > span:nth-child(3) > span').click()''')
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
        #上传附件
        # dk.js_execute('''$('#attachment_view > div:nth-child(1) > div  > div >div > span > input').click()''')
        # op_file = BrowserDriver(self)
        # op_file.upload_file()
        # time.sleep(5)
        time.sleep(3)
        try:
            dk.click(['css selector','#control2_view > button:nth-child(4)'])
        except Exception as e:
            print(e)
        time.sleep(8)

        self.driver.quit()

    def test_2_yyxtsxsqd(self):
        """登录李媛填写意见并提交结束

        :return:
        """
        print("方法2：",self.case_status)
        dk = dkPage(self.driver)
        dk.input_office_username('liyuan1')
        dk.input_office_password('cetcwe123!')
        dk.click_office_btn()
        time.sleep(3)
        dk.click(['css selector', "#todo-section > a.more"])
        dk.change_to_window(1)
        dk.send_key(['css selector', '#search_div_active > input'], "应用系统上线申请单" + current_timestamp)
        dk.click(['css selector', '#searchButton_active'])
        temptitle = "应用系统上线申请单" + current_timestamp
        time.sleep(3)
        dk.click(['css selector', "[title=" + temptitle + "]"])
        # dk.click(['css selector', '[title=' + temptitle + ''])
        # self.driver.execute_script('''$([])''')
        dk.change_to_window(2)
        time.sleep(3)
        title1 = self.driver.find_element_by_id("docTitle").get_attribute("value")
        self.assertEqual(title1, temptitle)
        time.sleep(2)
        dk.send_key(['css selector', '#fgldyj\$_opinion_popup_content'], "我是李媛，同意，请继续流转！")
        #dk.js_execute('''$('#control2_view > div.workflowsubmit_content.workflowsubmit_content_executor > div > div > div.workflowsubmit_content_hxr > div > dd:nth-child(2)').click()''')
        dk.click(['css selector', '#control2_view > button:nth-child(4)'])
        time.sleep(8)

    def test_3_yyxtsxsqd(self):
        """登录许勇填写意见并提交结束

        :return:
        """
        dk = dkPage(self.driver)
        dk.input_office_username('xuyong')
        dk.input_office_password('cetcwe123!')
        dk.click_office_btn()
        time.sleep(3)
        dk.click(['css selector', "#todo-section > a.more"])
        dk.change_to_window(1)
        dk.send_key(['css selector', '#search_div_active > input'], "应用系统上线申请单" + current_timestamp)
        dk.click(['css selector', '#searchButton_active'])
        temptitle = "应用系统上线申请单" + current_timestamp
        time.sleep(3)
        dk.click(['css selector', "[title=" + temptitle + "]"])
        # dk.click(['css selector', '[title=' + temptitle + ''])
        # self.driver.execute_script('''$([])''')
        dk.change_to_window(2)
        time.sleep(3)
        title1 = self.driver.find_element_by_id("docTitle").get_attribute("value")
        self.assertEqual(title1, temptitle)
        time.sleep(2)
        dk.send_key(['css selector', '#jtldyj\$_opinion_popup_content'], "我是许勇，同意，请继续流转！")
        #dk.js_execute('''$('#control2_view > div.workflowsubmit_content.workflowsubmit_content_executor > div > div > div.workflowsubmit_content_hxr > div > dd:nth-child(2)').click()''')
        dk.click(['css selector', '#control2_view > button:nth-child(4)'])
        time.sleep(8)

    def test_4_yyxtsxsqd(self):
        """登录杨军填写意见并提交结束

        :return:
        """
        dk = dkPage(self.driver)
        dk.input_office_username('yangjun10')
        dk.input_office_password('cetcwe123!')
        dk.click_office_btn()
        time.sleep(3)
        dk.click(['css selector', "#todo-section > a.more"])
        dk.change_to_window(1)
        dk.send_key(['css selector', '#search_div_active > input'], "应用系统上线申请单" + current_timestamp)
        dk.click(['css selector', '#searchButton_active'])
        temptitle = "应用系统上线申请单" + current_timestamp
        time.sleep(3)
        dk.click(['css selector', "[title=" + temptitle + "]"])
        # dk.click(['css selector', '[title=' + temptitle + ''])
        # self.driver.execute_script('''$([])''')
        dk.change_to_window(2)
        time.sleep(3)
        title1 = self.driver.find_element_by_id("docTitle").get_attribute("value")
        self.assertEqual(title1, temptitle)
        time.sleep(2)
        dk.send_key(['css selector', '#jtldyj\$_opinion_popup_content'], "我是杨军，同意，请继续流转！")
        #dk.js_execute('''$('#control2_view > div.workflowsubmit_content.workflowsubmit_content_executor > div > div > div.workflowsubmit_content_hxr > div > dd:nth-child(2)').click()''')
        dk.click(['css selector', '#control2_view > button:nth-child(4)'])
        time.sleep(8)

    def test_5_yyxtsxsqd(self):
        """登录尚国平填写意见并提交结束

        :return:
        """
        dk = dkPage(self.driver)
        dk.input_office_username('shangguoping')
        dk.input_office_password('cetcwe123!')
        dk.click_office_btn()
        time.sleep(3)
        dk.click(['css selector', "#todo-section > a.more"])
        dk.change_to_window(1)
        dk.send_key(['css selector', '#search_div_active > input'], "应用系统上线申请单" + current_timestamp)
        dk.click(['css selector', '#searchButton_active'])
        temptitle = "应用系统上线申请单" + current_timestamp
        time.sleep(3)
        dk.click(['css selector', "[title=" + temptitle + "]"])
        # dk.click(['css selector', '[title=' + temptitle + ''])
        # self.driver.execute_script('''$([])''')
        dk.change_to_window(2)
        time.sleep(3)
        title1 = self.driver.find_element_by_id("docTitle").get_attribute("value")
        self.assertEqual(title1, temptitle)
        time.sleep(2)
        dk.send_key(['css selector', '#hjfzryj\$_opinion_popup_content'], "我是尚国平，流程结束！")
        #dk.js_execute('''$('#control2_view > div.workflowsubmit_content.workflowsubmit_content_executor > div > div > div.workflowsubmit_content_hxr > div > dd:nth-child(2)').click()''')
        dk.click(['css selector', '#control2_view > button:nth-child(4)'])
        time.sleep(8)

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()