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
    jtxsdwdwcjxtbab_tj = (By.XPATH,'#noFlowSaveAndClose > button.btn.btn-success')
    #成员单位运维问题申请单
    cydwywwtsqd_bt = (By.CSS_SELECTOR,'#docTitle')
    cydwywwtsqd_sqr = (By.CSS_SELECTOR,'#creatorName')
    cydwywwtsqd_lxdh = (By.CSS_SELECTOR,'#phone')
    #应用系统上线申请单
    yyxtsxsqd_bt = (By.CSS_SELECTOR,'#docTitle')
    yyxtsxsqd_xtmc = (By.CSS_SELECTOR,'#systemName')
    yyxtsxsqd_sqr = (By.CSS_SELECTOR,'#creatorName')
    yyxtsxsqd_sxbb = (By.CSS_SELECTOR,'#onlineVersion')
    yyxtsxsqd_sxnr = (By.CSS_SELECTOR,'#onlineContent')
    yyxtsxsqd_sxyx = (By.CSS_SELECTOR,'#onlineAffect2')
    yyxtsxsqd_bz = (By.CSS_SELECTOR,'#remark')
    #蓝网数据中心维护单
    lwsjzxwhd_sxbt = (By.CSS_SELECTOR,'#docTitle')
    lwsjzxwhd_sqr = (By.CSS_SELECTOR,'#creatorName')
    lwsjzxwhd_whnr = (By.CSS_SELECTOR,'#modifyContent')
    lwsjzxwhd_bz = (By.CSS_SELECTOR,'#remark')
    #集团总部应用系统上线审批
    jtzbyyxtsxsp_bt = (By.CSS_SELECTOR,'#docTitle')
    jtzbyyxtsxsp_zrr = (By.CSS_SELECTOR,'#zrPerson')
    jtzbyyxtsxsp_dh = (By.CSS_SELECTOR,'#phone')
    jtzbyyxtsxsp_xtmc = (By.CSS_SELECTOR,'#systemName')
    jtzbyyxtsxsp_dmyj = (By.CSS_SELECTOR,'#confidentialBasis')
    jtzbyyxtsxsp_zygn = (By.CSS_SELECTOR,'#primaryFunction')
    jtzbyyxtsxsp_yhfw = (By.CSS_SELECTOR,'#userRange')






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

