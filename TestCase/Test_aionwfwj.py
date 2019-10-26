# -*- coding: utf-8 -*-
# __author__ = jason
# __date: 2019/6/24

import unittest
from Pages.dkPage import dkPage
from Base.BrowserDriver import BrowserDriver
from selenium.webdriver import ActionChains
import time
import datetime
class Test_aionwfwj(unittest.TestCase):
    global current_timestamp
    current_timestamp = str(int(time.time()))
    def setUp(self):
        driver = BrowserDriver(self)
        self.driver = driver.openbrowser(self)
        openresult = 0
        dk = dkPage(self.driver)
        dk.input_office_username('tianjie')
        dk.input_office_password('cetcwe123!')
        dk.click_office_btn()
        time.sleep(5)

    def test_aionwfwj(self):
        #print(int(time.time()))
        dk = dkPage(self.driver)
        #点击一网通办
        dk.click(['css selector','body > div.container.normaluser > form > div.usercontent.container-fluid > div > div.col-md-1.leftarea > div.nav > ul > li:nth-child(4) > a'])
        #等待页面加载
        time.sleep(5)
        #切换到一网通办首页
        dk.change_to_window(1)
        #点击事项列表
        dk.click(['css selector','#itemsList'])
        #等待页面加载
        time.sleep(1)
        #搜索事项，无违法违纪证明申请并点击事项名称
        dk.send_key(['css selector','#searchForm_itemsList > div > input'],"无违法违纪证明申请")
        dk.click(['css selector','[title="无违法违纪证明申请"]'])
        #等待页面加载
        time.sleep(3)
        #点击立即办理
        dk.click(['css selector','#handle'])
        #等待页面加载
        time.sleep(3)
        #切换到最右侧窗口
        dk.change_to_window(2)
        #填写表单
        dk.send_key(['css selector', '#docTitle'], "测试" + current_timestamp)
        dk.send_key(['css selector', '#legalRepresentative'], "法人" + current_timestamp)
        dk.send_key(['css selector', '#unitAddress'], "地址" + current_timestamp)
        dk.send_key(['css selector', '#reasonApplication'], "原因" + current_timestamp)
        dk.send_key(['css selector', '#remarks'], "备注" + current_timestamp)
        time.sleep(1)
        dk.click(['css selector','#noFlowSaveAndClose > button.btn.btn-success'])
        #alter = self.driver.switch_to_alert()
        #alter.accept()
        time.sleep(20)
        dk.change_to_window(1)
        dk.close()
        dk.change_to_window(0)
        dk.click(['xpath','/html/body/div[3]/form/div[1]/div/div[3]/div[1]/ul/li[1]/i'])
        dk.js_execute('$(".confimBtn button:eq(0)").click()')
        #self.driver.execute_script('$(".confimBtn button:eq(0)").click()')
        time.sleep(2)
        #dk.click(['xpath','/html/body/div[5]/div/div[1]/div[3]/button[1]'])
        #登录田婕并查找待办
        time.sleep(60)
        dk.input_office_username('tianj')
        dk.input_office_password('cetcwe123!')
        dk.click_office_btn()
        time.sleep(5)
        dk.click(['css selector',"#todo-section > a.more"])
        dk.change_to_window(1)
        dk.send_key(['css selector','#search_div_active > input'],"测试" + current_timestamp)
        dk.click(['css selector','#searchButton_active'])
        temptitle = "测试" + current_timestamp
        dk.click(['css selector','[title='+temptitle+''])
        #self.driver.execute_script('''$([])''')
        dk.change_to_window(2)
        time.sleep(15)
        title = self.driver.find_element_by_css_selector("#docTitle").get_attribute("value")
        self.assertEqual(title, temptitle)
        dk.click(['css selector','#control2_view > button:nth-child(4)'])
        dk.get_screent_img()
        time.sleep(10)


    def tearDown(self):
        pass


if __name__ == "__main__":
    unittest.main()


#  To Liu Yue
# $("#businessTypeChoose").contents().find("#flow-name").text("部门函发文流程");$("#businessTypeChoose").contents().find("#docTypeId").val("101");$("#businessTypeChoose").contents().find("#flowName").val("G2442_JITUAN_BUMEN")
# test
