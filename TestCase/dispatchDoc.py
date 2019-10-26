# -*- coding: utf-8 -*-
# __author__ = jason
# __date: 2019/6/10

import unittest
from Pages.officePage import officePage
from Base.BrowserDriver import BrowserDriver
from selenium.webdriver import ActionChains
import time
import datetime
class Test_findUser_pc(unittest.TestCase):

    def setUp(self):
        driver = BrowserDriver(self)
        self.driver = driver.openbrowser(self)
        openresult = 0
        office = officePage(self.driver)
        office.input_office_username('liyang')
        office.input_office_password('123456')
        office.click_office_btn()
        time.sleep(2)
        office.change_to_oa_link()
        #切换到最右窗口
        office.change_to_window(1)
        #windows = self.driver.window_handles
        #self.driver.switch_to.window(windows[-1])

    def test_findUser_pc(self):
        #print(int(time.time()))
        office = officePage(self.driver)
        office.click(['css','#nav_sub > ul > li:nth-child(1) > h1 > span'])
        #self.driver.find_element_by_css_selector('#applicationManageId').click()
        #self.driver.find_element_by_css_selector('#nav_sub > ul > li:nth-child(1) > h1 > i').click()
        #self.driver.find_element_by_css_selector('#nav_sub > ul > li:nth-child(1) > div > div > dl:nth-child(1) > dd > a:nth-child(1)').click()
        ActionChains(self.driver).move_to_element(self.driver.find_element_by_css_selector('#nav_sub > ul > li:nth-child(1) > h1 > span')).perform()
        time.sleep(1)
        self.driver.find_element_by_link_text("发文起草").click()
        office.change_to_window(2)
        office.send_key(['css','#tel_num'],"13901234567")
        office.send_key(['css','#doc_title'],"测试"+str(int(time.time())))
        office.click(['css','#framework-content > table > tbody > tr:nth-child(14) > td.tdContent.lastCol > div > span > span'])
        office.click()
        time.sleep(20)

        time.sleep(10)


    def tearDown(self):
        pass


if __name__ == "__main__":
    unittest.main()