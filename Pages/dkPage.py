# -*- coding: utf-8 -*-
# __author__ = jason
# __date: 2019/6/24

from selenium.webdriver.common.by import By
from Base.Selenium2 import BasePage
import os
class dkPage(BasePage):
    """
    在这里写定位器，通过元素属性定位元素对象
    """
    ###PC端元素###
    userName = (By.CSS_SELECTOR,'#emailId')#定位用户名输入框
    passWord = (By.CSS_SELECTOR,'#password')#定位密码输入框
    loginButton = (By.CSS_SELECTOR,'#login-btn')  # 定位登录按钮
    jtxsdwdwcjxtbab_sxbt = (By.CSS_SELECTOR,'#docTitle')
    jtxsdwdwcjxtbab_badwbm = (By.CSS_SELECTOR,'#recordsDept')
    jtxsdwdwcjxtbab_babh = (By.CSS_SELECTOR,'#recordsNumber')
    jtxsdwdwcjxtbab_lxr = (By.CSS_SELECTOR,'#contact')
    jtxsdwdwcjxtbab_lxdh = (By.CSS_SELECTOR,'#phone')
    jtxsdwdwcjxtbab_yyxtmc = (By.CSS_SELECTOR,'#appName')
    jtxsdwdwcjxtbab_xtjsf = (By.CSS_SELECTOR,'#systemBuild')
    jtxsdwdwcjxtbab_xtym = (By.CSS_SELECTOR,'#domain')
    jtxsdwdwcjxtbab_ip = (By.CSS_SELECTOR,'#ipAddress')
    jtxsdwdwcjxtbab_sxsj = (By.CSS_SELECTOR,'#startUpTime_picker')
    jtxsdwdwcjxtbab_bsfs = (By.CSS_SELECTOR,'#deploymentMode')
    jtxsdwdwcjxtbab_bswzwlqy = (By.CSS_SELECTOR,'#netRegion')
    jtxsdwdwcjxtbab_xtjj = (By.CSS_SELECTOR,'#intro')
    jtxsdwdwcjxtbab_bz =  (By.CSS_SELECTOR,'#remarks')

    def input_office_username(self,text):
        self.send_key(self.userName,text)

    def input_office_password(self, text):
        self.send_key(self.passWord,text)

    def input_office_username_mb(self,text):
        self.send_key(self.userNameMobile,text)

    def input_office_password_mb(self, text):
        self.send_key(self.passWordMobile,text)

    def change_to_oa_link(self):
        self.click(self.OA_LINK)

    def click_office_btn(self):
        self.click(self.loginButton)

    def click_office_btn_mb(self):
        self.click(self.loginButtonMobile)

