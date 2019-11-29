# -*- coding: utf-8 -*-
# @Time    : 2019/11/29 9:49
# @Author  : 洋燚
# @Email   : jasonleeyag@163.com
import sys,os
import unittest

from Pages.dkPage import dkPage
from Base.BrowserDriver import BrowserDriver
import time

class Test_04jtzbyyxtsxsp(unittest.TestCase):

    global current_timestamp
    current_timestamp = str(int(time.time()))

    @classmethod
    def setUp(self):
        driver = BrowserDriver(self)
        self.driver = driver.openbrowser(self)
        openresult = 0
        time.sleep(10)


    def test_1_jtzbyyxtsxsp(self):
        """登录许培伦集团总部应用系统上线审批

        :return:
        """
        dk = dkPage(self.driver)
        dk.input_office_username('xupeilun')
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
        # 搜索事项，集团总部应用系统上线审批并点击事项名称
        dk.send_key(['css selector', '#searchForm_itemsList > div > input'], "集团总部应用系统上线审批")
        dk.click(['css selector', '[title="集团总部应用系统上线审批"]'])
        # 等待页面加载
        time.sleep(5)
        # 点击立即办理
        dk.click(['css selector', '#handle'])
        # 等待页面加载
        time.sleep(3)
        dk.change_to_window(2)
        # 填写表单
        dk.send_key(dkPage.jtzbyyxtsxsp_bt,"集团总部应用系统上线" + current_timestamp)
        dk.send_key(dkPage.jtzbyyxtsxsp_zrr,"王良")
        dk.send_key(dkPage.jtzbyyxtsxsp_dh,"13901234567")
        dk.send_key(dkPage.jtzbyyxtsxsp_xtmc,"系统名称" + current_timestamp)
        dk.send_key(dkPage.jtzbyyxtsxsp_dmyj,"定密依据" + current_timestamp)
        dk.send_key(dkPage.jtzbyyxtsxsp_zygn,"主要功能" + current_timestamp)
        dk.send_key(dkPage.jtzbyyxtsxsp_yhfw,"用户范围" + current_timestamp)

        # dk.js_execute('''$('span.btn:nth-child(1) > input:nth-child(2)').click()''')
        # op_file = BrowserDriver(self)
        # op_file.upload_file()
        # time.sleep(3)
        try:
            dk.click(['css selector','#control2_view > button:nth-child(4)'])
            #self.driver.find_element_by_css_selector('#control2_view > button:nth-child(41)').click()
        except Exception as e:
            print(e)

        time.sleep(5)



    def test_2_jtzbyyxtsxsp(self):

        """登录李明并查找待办,并且提交待办

        :return:
        """
        dk = dkPage(self.driver)
        dk.input_office_username('lim')
        dk.input_office_password('cetcwe123!')
        dk.click_office_btn()
        time.sleep(5)
        dk.click(['css selector', "#todo-section > a.more"])
        dk.change_to_window(1)
        try:
            dk.send_key(['css selector', '#search_div_active > input'], "集团总部应用系统上线" + current_timestamp)
            dk.click(['css selector', '#searchButton_active'])
        except Exception as e:
            print(e)
            self.result['Status'] = True
        temptitle = "集团总部应用系统上线" + current_timestamp
        dk.click(['css selector', "[title=" + temptitle + "]"])
        # self.driver.execute_script('''$([])''')
        dk.change_to_window(2)
        time.sleep(5)
        # title = self.driver.find_element_by_css_selector("#docTitle").get_attribute("value")
        # self.assertEqual(title, temptitle)
        try:
            dk.send_key(['css selector', '#deptOpinion\$_opinion_popup_content'], "我是李明，请继续流转")
            #dk.click(['css selector', '#control2_view > div.workflowsubmit_content.workflowsubmit_content_executor > div > div > div.workflowsubmit_content_zxrtitle > span.workflowsubmit_content_zxrtitle_link'])
            dk.click(['xpath', '//*[@id="control2_view"]/div[3]/div/div/div[3]/span[2]'])
            dk.js_execute(
                """$('#tab_userSelectorTbs > div > div > li > ul > li:nth-child(3) > span:nth-child(1)').click()""")
            time.sleep(1)
            dk.js_execute(
                """$('#tab_userSelectorTbs > div > div > li > ul > li:nth-child(3) > ul > li:nth-child(24) > span').click()""")
            time.sleep(1)
            dk.js_execute(
                """$('#tab_userSelectorTbs > div > div > li > ul > li:nth-child(3) > ul > li:nth-child(24) >ul >li:nth-child(13) > span').click()""")
            time.sleep(1)
            dk.js_execute(
                """$('#tab_userSelectorTbs > div > div > li > ul > li:nth-child(3) > ul > li:nth-child(24) >ul >li:nth-child(13) > ul >li:nth-child(44) >a').dblclick()""")
            time.sleep(1)
            dk.js_execute("""$('div:nth-child(3) > div > div > div >div:nth-child(3) > button:nth-child(1)').click()""")
            time.sleep(2)
        except Exception as e:
            print(e)
            time.sleep(5)
        dk.click(['xpath', '/html/body/div/form/div/div[3]/div/div/div[2]/div/div[2]/div[1]/button[1]'])
        dk.get_screent_img()
        # time.sleep(15)
        # dk.change_to_window(1)
        # dk.close()
        # dk.change_to_window(0)
        # dk.click(['xpath', '/html/body/div[3]/form/div[1]/div/div[3]/div[1]/ul/li[1]/i'])
        # dk.click(['css selector', '#control2_view > button:nth-child(4)'])
        time.sleep(10)



    def test_3_jtzbyyxtsxsp(self):
        """登录王良并查找待办,并且提交待办

        :return:
        """
        dk = dkPage(self.driver)
        dk.input_office_username('wangliang1')
        dk.input_office_password('cetcwe123!')
        dk.click_office_btn()
        time.sleep(5)
        dk.click(['css selector', "#todo-section > a.more"])
        dk.change_to_window(1)
        try:
            dk.send_key(['css selector', '#search_div_active > input'], "集团总部应用系统上线" + current_timestamp)
            dk.click(['css selector', '#searchButton_active'])
        except Exception as e:
            print(e)

        temptitle = "集团总部应用系统上线" + current_timestamp
        dk.click(['css selector', "[title=" + temptitle + "]"])
        # self.driver.execute_script('''$([])''')
        dk.change_to_window(2)
        time.sleep(5)
        # title = self.driver.find_element_by_css_selector("#docTitle").get_attribute("value")
        # self.assertEqual(title, temptitle)
        try:
            dk.send_key(['css selector', '#deptOpinion\$_opinion_popup_content'], "我是王良，请继续流转")
            dk.click(['css selector', '#control2_view > button:nth-child(4)'])
            dk.get_screent_img()
        except Exception as e:
            print(e)

        time.sleep(10)


    def test_4_jtzbyyxtsxsp(self):
        """登录尚国平并查找待办,并且提交待办

        :return:
        """
        dk = dkPage(self.driver)
        dk.input_office_username('shangguoping')
        dk.input_office_password('cetcwe123!')
        dk.click_office_btn()
        time.sleep(5)
        dk.click(['css selector', "#todo-section > a.more"])
        dk.change_to_window(1)
        try:
            dk.send_key(['css selector', '#search_div_active > input'], "集团总部应用系统上线" + current_timestamp)
            dk.click(['css selector', '#searchButton_active'])
        except Exception as e:
            print(e)
            self.result['Status'] = True
        temptitle = "集团总部应用系统上线" + current_timestamp
        dk.click(['css selector', "[title=" + temptitle + "]"])
        # self.driver.execute_script('''$([])''')
        dk.change_to_window(2)
        time.sleep(5)
        # title = self.driver.find_element_by_css_selector("#docTitle").get_attribute("value")
        # self.assertEqual(title, temptitle)
        dk.send_key(['css selector','#testRport'],"通过！！！")
        dk.send_key(['css selector','#ipAddress'],"10.254.0.246")
        try:
            dk.send_key(['css selector', '#ywhcOpinion\$_opinion_popup_content'], "我是尚国平，请继续流转")
            dk.click(['css selector', '#control2_view > button:nth-child(4)'])
            dk.get_screent_img()
        except Exception as e:
            print(e)

        time.sleep(10)


    def test_5_jtzbyyxtsxsp(self):
        """登录李明并查找待办,并且提交待办

        :return:
        """
        dk = dkPage(self.driver)
        dk.input_office_username('lim')
        dk.input_office_password('cetcwe123!')
        dk.click_office_btn()
        time.sleep(5)
        dk.click(['css selector', "#todo-section > a.more"])
        dk.change_to_window(1)
        try:
            dk.send_key(['css selector', '#search_div_active > input'], "集团总部应用系统上线" + current_timestamp)
            dk.click(['css selector', '#searchButton_active'])
        except Exception as e:
            print(e)

        temptitle = "集团总部应用系统上线" + current_timestamp
        dk.click(['css selector', "[title=" + temptitle + "]"])
        # self.driver.execute_script('''$([])''')
        dk.change_to_window(2)
        time.sleep(5)
        # title = self.driver.find_element_by_css_selector("#docTitle").get_attribute("value")
        # self.assertEqual(title, temptitle)
        try:
            dk.send_key(['css selector', '#xxhdeptOpinion\$_opinion_popup_content'], "我是李明，流程结束")
            dk.click(['css selector', '#control2_view > button:nth-child(4)'])
            dk.get_screent_img()
        except Exception as e:
            print(e)

        time.sleep(10)

    def test_6_jtzbyyxtsxsp(self):
        """登录严义军并查找待办,并且提交待办

        :return:
        """
        dk = dkPage(self.driver)
        dk.input_office_username('yanyijun')
        dk.input_office_password('cetcwe123!')
        dk.click_office_btn()
        time.sleep(8)
        dk.click(['css selector', "#waitDo > a"])
        dk.change_to_window(1)
        try:
            dk.send_key(['css selector', '#search_div_active > input'], "集团总部应用系统上线" + current_timestamp)
            dk.click(['css selector', '#searchButton_active'])
        except Exception as e:
            print(e)

        temptitle = "集团总部应用系统上线" + current_timestamp
        dk.click(['css selector', "[title=" + temptitle + "]"])
        # self.driver.execute_script('''$([])''')
        dk.change_to_window(2)
        time.sleep(5)
        # title = self.driver.find_element_by_css_selector("#docTitle").get_attribute("value")
        # self.assertEqual(title, temptitle)
        try:
            dk.send_key(['css selector', '#xxhdeptOpinion\$_opinion_popup_content'], "我是严义军，流程结束")
            dk.click(['css selector', '#control2_view > button:nth-child(4)'])
            dk.get_screent_img()
        except Exception as e:
            print(e)

        time.sleep(10)

    def test_7_jtzbyyxtsxsp(self):
        """登录王旭并查找待办,并且提交待办

        :return:
        """
        dk = dkPage(self.driver)
        dk.input_office_username('wangxu15')
        dk.input_office_password('cetcwe123!')
        dk.click_office_btn()
        time.sleep(5)
        dk.click(['css selector', "#todo-section > a.more"])
        dk.change_to_window(1)
        try:
            dk.send_key(['css selector', '#search_div_active > input'], "集团总部应用系统上线" + current_timestamp)
            dk.click(['css selector', '#searchButton_active'])
        except Exception as e:
            print(e)

        temptitle = "集团总部应用系统上线" + current_timestamp
        dk.click(['css selector', "[title=" + temptitle + "]"])
        # self.driver.execute_script('''$([])''')
        dk.change_to_window(2)
        time.sleep(5)
        #title = self.driver.find_element_by_css_selector("#docTitle").get_attribute("value")
        #self.assertEqual(title, temptitle)
        try:
            dk.send_key(['css selector', '#ywglyjlOpinion\$_opinion_popup_content'], "我是严义军，流程结束")
            dk.click(['css selector', '#control2_view > button:nth-child(4)'])
            dk.get_screent_img()
        except Exception as e:
            print(e)

        time.sleep(10)
    def tearDown(self):
        self.driver.quit()

    if __name__ == "__main__":
        unittest.main()