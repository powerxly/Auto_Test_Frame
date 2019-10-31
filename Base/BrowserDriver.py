#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author  : Vant
# @Email   : 944921374@qq.com
# @fixBy   : jasonleeyag

import os.path
from selenium import webdriver
from Base.logger import Logger
import yaml
import time

logger = Logger(logger="BrowserDriver").getlog()

class BrowserDriver(object):
    path = os.path.dirname(os.path.dirname(os.path.abspath('.')))#这是获取相对路径的方法
    chrome_driver_path = path + '/driver/chromedriver.exe'
    ie_driver_path = path + '/driver/IEDriverServer.exe'

    def __init__(self,driver):
        self.driver = driver

    def openbrowser(self,driver):
        #读取配置文件"F:\\CODE\\Auto_Test_Framework\\yaml\\browser.yaml"
        #file_path = os.path.dirname(os.path.dirname(os.getcwd()))

        # 获取父级目录
        #parent_path = os.path.dirname(file_path)
        name_path = "F:\\CODE\\Auto_Test_Framework\\yaml\\browser.yaml"
        with open(name_path, 'r',encoding='UTF-8') as f:
            temp = yaml.load(f.read(),Loader=yaml.FullLoader)
        # 获取配置文件属性
        brow = temp['brwserType']['browserName']
        browser = brow
        logger.info("选择的浏览器为: %s 浏览器" % browser)
        ur = temp['testUrl']['URL']
        url = ur
        logger.info("打开的URL为: %s" % url)
        if browser == "Firefox":
            driver = webdriver.Firefox()
            logger.info("启动火狐浏览器")
        elif browser == "Chrome":
            driver = webdriver.Chrome(self.chrome_driver_path)
            logger.info("启动谷歌浏览器")
        elif browser == "IE":
            driver = webdriver.Ie(self.ie_driver_path)
            logger.info("启动IE浏览器")
        driver.get(ur)
        logger.info("打开URL: %s" % url)
        driver.maximize_window()
        logger.info("全屏当前窗口")
        driver.implicitly_wait(5)
        logger.info("设置5秒隐式等待时间")
        return driver

    def openbrowsemobile(self,driver):
        '''
        最新版本chrome该方法不可用！！！
        最新版本chrome该方法不可用！！！
        最新版本chrome该方法不可用！！！
        '''
        #读取配置文件
        file_path = os.path.dirname(os.getcwd())
        parent_path = os.path.dirname(file_path)
        name_path = parent_path + '\yaml\\browser.yaml'
        with open(name_path, 'r') as f:
            temp = yaml.load(f.read(),Loader=yaml.FullLoader)
        # 获取配置文件属性
        brow = temp['brwserType']['browserName']
        browser = brow
        logger.info("选择的浏览器为: %s 浏览器" % browser)
        ur = temp['testUrlMobile']['URL']
        url = ur
        logger.info("打开的URL为: %s" % url)
        if browser == "Firefox":
            driver = webdriver.Firefox()
            logger.info("启动火狐浏览器")
        elif browser == "Chrome":
            mobile_emulation = {"deviceName": "iPhone X"}
            option = webdriver.ChromeOptions()
            option.add_experimental_option('mobileEmulation', mobile_emulation)
            driver = webdriver.Chrome(chrome_options=option)
            logger.info("启动谷歌浏览器")
        elif browser == "IE":
            driver = webdriver.Ie(self.ie_driver_path)
            logger.info("启动IE浏览器")

        driver.get(url)
        logger.info("打开URL: %s" % url)
        driver.maximize_window()
        logger.info("全屏当前窗口")
        driver.implicitly_wait(5)
        logger.info("设置5秒隐式等待时间")
        return driver

    def quit_browser(self):
        logger.info("关闭浏览器")
        self.driver.quit()

    def upload_file(self):
        file_path = os.path.dirname(os.getcwd())
        # 获取父级目录
        parent_path = os.path.dirname(file_path)
        name_path = parent_path + '\yaml\\browser.yaml'
        with open(name_path, 'r', encoding='UTF-8') as f:
            temp = yaml.load(f.read(), Loader=yaml.FullLoader)
        # 获取配置文件属性
        brow = temp['brwserType']['browserName']
        browser = brow
        logger.info("选择的浏览器为: %s 浏览器" % browser)
        ur = temp['testUrl']['URL']
        url = ur
        logger.info("打开的URL为: %s" % url)
        if browser == "Firefox":
            print("开始上传文件")
            os.chdir("F:\CODE\Auto_Test_Framework\\fileupload")
            os.system("firefox_uploadfile.exe")
            print("文件上传完成")
        elif browser == "Chrome":
            print("开始上传文件")
            os.chdir("F:\CODE\Auto_Test_Framework\\fileupload")
            os.system("chrome_uploadfile.exe")
            print("文件上传完成")
        elif browser == "IE":
            print("开始上传文件")
            os.chdir("F:\CODE\Auto_Test_Framework\\fileupload")
            os.system("ie_uploadfile.exe")
            print("文件上传完成")
