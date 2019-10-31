# -*- coding: utf-8 -*-
# @Time    : 2019/10/29 17:42
# @Author  : 洋燚
# @Email   : jasonleeyag@163.com

import sys,os
import unittest

from Pages.dkPage import dkPage
from Base.BrowserDriver import BrowserDriver
import time

class Test_dwcjxtba(unittest.TestCase):
    global current_timestamp
    current_timestamp = str(int(time.time()))

    def setUp(self):
        driver = BrowserDriver(self)
        self.driver = driver.openbrowser(self)
        openresult = 0
        time.sleep(10)

    def test_1_dwcjxtba(self):
        """登录马骏起草集团下属单位对外承建系统备案表

        :return:
        """
        dk = dkPage(self.driver)
        dk.input_office_username('majun1')
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
        dk.send_key(['css selector', '#searchForm_itemsList > div > input'], "成员单位对外承建系统备案")
        dk.click(['css selector', '[title="成员单位对外承建系统备案"]'])
        # 等待页面加载
        time.sleep(5)
        # 点击立即办理
        dk.click(['css selector', '#handle'])
        # 等待页面加载
        time.sleep(3)
        dk.change_to_window(2)
        # 填写表单
        dk.send_key(dkPage.jtxsdwdwcjxtbab_sxbt, "标题" + current_timestamp)
        dk.send_key(dkPage.jtxsdwdwcjxtbab_badwbm, "单位" + current_timestamp)
        dk.send_key(dkPage.jtxsdwdwcjxtbab_babh, "编号" + current_timestamp)
        dk.send_key(dkPage.jtxsdwdwcjxtbab_lxr, "联系人" + current_timestamp)
        dk.send_key(dkPage.jtxsdwdwcjxtbab_lxdh, "联系电话" + current_timestamp)
        dk.send_key(dkPage.jtxsdwdwcjxtbab_yyxtmc, "系统名称" + current_timestamp)
        dk.send_key(dkPage.jtxsdwdwcjxtbab_xtjsf, "系统名称" + current_timestamp)
        dk.send_key(dkPage.jtxsdwdwcjxtbab_xtym, "系统域名" + current_timestamp)
        dk.send_key(dkPage.jtxsdwdwcjxtbab_ip, "127.0.0.1")
        dk.js_execute('''$('#startUpTime_view > span:nth-child(3) > span').click()''')
        dk.js_execute('''$('body > div.datetimepicker.datetimepicker-dropdown-bottom-left.dropdown-menu > div.datetimepicker-days > table > thead > tr:nth-child(1) > th.next > i').click()''')
        dk.js_execute('''$('body > div.datetimepicker.datetimepicker-dropdown-bottom-left.dropdown-menu > div.datetimepicker-days > table > tbody > tr:nth-child(3) > td:nth-child(4)').click()''')
        dk.send_key(dkPage.jtxsdwdwcjxtbab_bsfs, "部署方式" + current_timestamp)
        dk.send_key(dkPage.jtxsdwdwcjxtbab_bswzwlqy, "网络区域" + current_timestamp)
        dk.send_key(dkPage.jtxsdwdwcjxtbab_xtjj, "系统简介" + current_timestamp)
        dk.send_key(dkPage.jtxsdwdwcjxtbab_bz, "备注" + current_timestamp)
        dk.js_execute('$("#framework-content > table > tbody > tr:nth-child(15) > td:nth-child(2) > div > div >div > div > div > span > input").click()')
        time.sleep(5)
        #上传附件
        op_file = BrowserDriver(self)
        op_file.upload_file()
        time.sleep(3)
        self.driver.quit()
        time.sleep(20)

    def test_2_dwcjxtba(self):
        """登录盖建军处理待办

        :return:
        """
        dk = dkPage(self.driver)
        dk.input_office_username('gaijianjun1')
        dk.input_office_password('cetcwe123!')
        dk.click_office_btn()
        time.sleep(15)
        dk.click(['css selector', "#todo-section > a.more"])
        dk.change_to_window(1)
        dk.send_key(['css selector', '#search_div_active > input'], "标题" + current_timestamp)
        dk.click(['css selector', '#searchButton_active'])
        temptitle = "标题" + current_timestamp
        dk.click(['css selector', '[title=' + temptitle + ''])
        # self.driver.execute_script('''$([])''')
        dk.change_to_window(2)
        time.sleep(15)
        title = self.driver.find_element_by_css_selector("#docTitle").get_attribute("value")
        self.assertEqual(title, temptitle)
        dk.click(['css selector', '#control2_view > button:nth-child(4)'])
        time.sleep(40)


    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()