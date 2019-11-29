# # -*- coding: utf-8 -*-
# # @Time    : 2019/11/29 9:49
# # @Author  : 洋燚
# # @Email   : jasonleeyag@163.com
# import sys,os
# import unittest
#
# from Pages.dkPage import dkPage
# from Base.BrowserDriver import BrowserDriver
# import time
#
# class Test_04jtzbyyxtsxsp(unittest.TestCase):
#
#     global current_timestamp
#     current_timestamp = str(int(time.time()))
#
#     @classmethod
#     def setUp(self):
#         driver = BrowserDriver(self)
#         self.driver = driver.openbrowser(self)
#         openresult = 0
#         time.sleep(5)
#
#
#     def test_2_jtzbyyxtsxsp(self):
#
#         """登录李明并查找待办,并且提交待办
#
#         :return:
#         """
#         dk = dkPage(self.driver)
#         dk.input_office_username('lim')
#         dk.input_office_password('cetcwe123!')
#         dk.click_office_btn()
#         time.sleep(2)
#         dk.click(['css selector', "#todo-section > a.more"])
#         dk.change_to_window(1)
#         try:
#             dk.send_key(['css selector', '#search_div_active > input'], "标题1575005525")
#             dk.click(['css selector', '#searchButton_active'])
#         except Exception as e:
#             print(e)
#             self.result['Status'] = True
#         temptitle = "标题" + current_timestamp
#         dk.click(['css selector', "[title=标题1575005525]"])
#         # self.driver.execute_script('''$([])''')
#         dk.change_to_window(2)
#         time.sleep(5)
#         dk.click(['xpath','//*[@id="control2_view"]/div[3]/div/div/div[3]/span[2]'])
#         dk.js_execute("""$('#tab_userSelectorTbs > div > div > li > ul > li:nth-child(3) > span:nth-child(1)').click()""")
#         time.sleep(1)
#         dk.js_execute("""$('#tab_userSelectorTbs > div > div > li > ul > li:nth-child(3) > ul > li:nth-child(24) > span').click()""")
#         time.sleep(1)
#         dk.js_execute("""$('#tab_userSelectorTbs > div > div > li > ul > li:nth-child(3) > ul > li:nth-child(24) >ul >li:nth-child(13) > span').click()""")
#         time.sleep(1)
#         dk.js_execute("""$('#tab_userSelectorTbs > div > div > li > ul > li:nth-child(3) > ul > li:nth-child(24) >ul >li:nth-child(13) > ul >li:nth-child(44) >a').dblclick()""")
#         time.sleep(1)
#         dk.js_execute("""$('div:nth-child(3) > div > div > div >div:nth-child(3) > button:nth-child(1)').click()""")
#
#         # groupTree = self.driver.find_elements_by_xpath("//*[@id='tab_userSelectorTbs']")
#         # print(type(groupTree))
#         # print(groupTree)
#         # list = []
#         # for x in groupTree:
#         #     a = x.text
#         #     list.append(a)
#         #     print(a)
#         # print(list[0].split('\n'))
#         # print(len(list[0].split('\n')))
#         # print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++=")
#         # print(list)
#
#             # if textE.text == "中国电子科技集团有限公司":
#             #     self.driver.find_element(textE).click()
#             #     break
#
#
#         # try:
#         #     dk.send_key(['css selector', '#deptOpinion\$_opinion_popup_content'], "我是李明，请继续流转")
#         #     #dk.click(['css selector', '#control2_view > div.workflowsubmit_content.workflowsubmit_content_executor > div > div > div.workflowsubmit_content_zxrtitle > span.workflowsubmit_content_zxrtitle_link'])
#         #     dk.js_execute('''$('#control2_view > div.workflowsubmit_content.workflowsubmit_content_executor > div > div > div.workflowsubmit_content_zxrtitle > span.workflowsubmit_content_zxrtitle_link').click()''')
#         #     time.sleep(1)
#         #     try:
#         #         dk.js_execute('''$('#userTab_4_switch').click()''')
#         #     except Exception as e:
#         #         print(e)
#         #     time.sleep(1)
#         #     try:
#         #         dk.js_execute('''$('#userTab_143_switch').click()''')
#         #     except Exception as e:
#         #         print(e)
#         #     time.sleep(1)
#         #     try:
#         #         dk.js_execute('''$('#userTab_158_switch').click()''')
#         #     except Exception as e:
#         #         print(e)
#         #     time.sleep(1)
#         #     try:
#         #         dk.js_execute('''$('#userTab_223_span').dblclick()''')
#         #     except Exception as e:
#         #         print(e)
#         #     time.sleep(1)
#         #     try:
#         #         dk.js_execute('''$('div:nth-child(3) > div > div > div >div:nth-child(3) > button:nth-child(1)').click()''')
#         #     except Exception as e:
#         #         print(e)
#         #     time.sleep(1)
#         #     dk.click(['css selector', '#control2_view > button:nth-child(4)'])
#         #     dk.get_screent_img()
#         # except Exception as e:
#         #     print(e)
#         time.sleep(120)
#
#
#     def tearDown(self):
#         self.driver.quit()
#
#     if __name__ == "__main__":
#         unittest.main()