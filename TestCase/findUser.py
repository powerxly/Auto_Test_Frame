# -*- coding: utf-8 -*-
# __author__ = jason
# __date: 2019/6/10

#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author  : 洋燚
# @Email   : 394856389@qq.com

import unittest
from Pages.officePage import officePage
from Base.BrowserDriver import BrowserDriver
from selenium.webdriver import ActionChains
import time
class Test_findUser_pc(unittest.TestCase):

    def setUp(self):
        driver = BrowserDriver(self)
        self.driver = driver.openbrowser(self)
        openresult = 0
        office = officePage(self.driver)
        office.input_office_username('admin')
        office.input_office_password('admin')
        office.click_office_btn()
        time.sleep(2)
        office.change_to_oa_link()
        #切换到最右窗口
        office.change_to_window(1)
        #windows = self.driver.window_handles
        #self.driver.switch_to.window(windows[-1])

    def test_findUser_pc(self):
        office = officePage(self.driver)
        office.click(['id','applicationManageId'])
        #self.driver.find_element_by_css_selector('#applicationManageId').click()
        #self.driver.find_element_by_css_selector('#nav_sub > ul > li:nth-child(1) > h1 > i').click()
        #self.driver.find_element_by_css_selector('#nav_sub > ul > li:nth-child(1) > div > div > dl:nth-child(1) > dd > a:nth-child(1)').click()
        ActionChains(self.driver).move_to_element(self.driver.find_element_by_css_selector('#nav_sub > ul > li:nth-child(1) > h1 > i')).perform()
        time.sleep(1)
        self.driver.find_element_by_link_text("用户管理").click()
        ActionChains(self.driver).move_to_element(self.driver.find_element_by_css_selector('#user-content > div > ul > li:nth-child(4) > div'))

        time.sleep(10)


    def tearDown(self):
        pass


if __name__ == "__main__":
    unittest.main()