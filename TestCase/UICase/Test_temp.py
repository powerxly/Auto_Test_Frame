# # -*- coding: utf-8 -*-
# # __author__ = jason
# # __date: 2019/6/24
#
# import unittest
# import sys,os
# sys.path.append("F:\\CODE\\Auto_Test_Framework")
# from Pages.dkPage import dkPage
# from Base.BrowserDriver import BrowserDriver
# from selenium.webdriver import ActionChains
# import time
# import datetime
# class Test_aionwfwj1(unittest.TestCase):
#     global current_timestamp
#     current_timestamp = str(int(time.time()))
#     def setUp(self):
#         driver = BrowserDriver(self)
#         self.driver = driver.openbrowser(self)
#         openresult = 0
#         dk = dkPage(self.driver)
#         #dk.input_office_username('tianj')
#         #dk.input_office_password('cetcwe123!')
#         #dk.click_office_btn()
#         time.sleep(5)
#
#     def test_aionwfwj1(self):
#         dk = dkPage(self.driver)
#         dk.input_office_username('sunbusheng')
#         dk.input_office_password('cetcwe123!')
#         dk.click_office_btn()
#         time.sleep(15)
#         dk.click(['css selector',"#waitDo > a"])
#         dk.change_to_window(1)
#         dk.send_key(['css selector','#search_div_active > input'],"测试1572243820")
#         time.sleep(3)
#         dk.click(['css selector','#searchButton_active'])
#         #temptitle = "测试" + current_timestamp
#         time.sleep(3)
#         dk.click(['css selector',"[title='测试1572243820']"])
#         #self.driver.execute_script('''$([])''')
#         dk.change_to_window(2)
#         time.sleep(30)
#         title1 = self.driver.find_element_by_id("docTitle").get_attribute("value")
#         self.assertEqual(title1, "测试1572243820")
#         #dk.click(['css selector','#control2_view > button:nth-child(4)'])
#         #dk.get_screent_img()
#         dk.send_key(['css selector','#jjjczyj\$_opinion_popup_content'],"同意，请继续流转")
#         time.sleep(100)
#
#
#     def tearDown(self):
#         pass
#
#
# if __name__ == "__main__":
#     unittest.main()
#
#
# #  To Liu Yue
# # $("#businessTypeChoose").contents().find("#flow-name").text("部门函发文流程");$("#businessTypeChoose").contents().find("#docTypeId").val("101");$("#businessTypeChoose").contents().find("#flowName").val("G2442_JITUAN_BUMEN")
