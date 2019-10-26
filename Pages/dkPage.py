# -*- coding: utf-8 -*-
# __author__ = jason
# __date: 2019/6/24

from selenium.webdriver.common.by import By
from Base.Selenium2 import BasePage

class dkPage(BasePage):
    """
    在这里写定位器，通过元素属性定位元素对象
    """
    ###PC端元素###
    userName = (By.CSS_SELECTOR,'#emailId')#定位用户名输入框
    passWord = (By.CSS_SELECTOR,'#password')#定位密码输入框
    loginButton = (By.CSS_SELECTOR,'#login-btn')  # 定位登录按钮
    OA_LINK = (By.CSS_SELECTOR,'#oa_link') #定位個人工作臺


    ###移动端元素###

    userList = {"wanghuan": "123456",
                "lush": "123456"
                }


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

