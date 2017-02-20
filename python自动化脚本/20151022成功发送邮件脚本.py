# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re
#当前程序的目的是：打开一个页面，输入用户名密码，点击页面的管理员入口-下拉菜单，点进去以后，进行邮件发送操作。
#另外附带的网页的源码一并打包，方便各位学习。
class Aaa(unittest.TestCase):
    while True:
        def setUp(self):

                self.driver = webdriver.Firefox()
                self.driver.implicitly_wait(1)
                #打开页面
                self.base_url = "http://192.168.1.245:9999/secure/MyJiraHome.jspa"
                self.verificationErrors = []
                self.accept_next_alert = True
        def test_aaa(self):

                driver = self.driver
            #找当前页面的方式
                driver.get(self.base_url + "/secure/Dashboard.jspa")
            # ERROR: Caught exception [ERROR: Unsupported command [selectFrame | gadget-0 | ]]
            #select的方式在这里不适用，使用切换frame的方式，切换到 gadget-0  frame中
                driver.switch_to_frame("gadget-0")
            #切换以后进行登录操作
                driver.find_element_by_id("login-form-username").clear()
                driver.find_element_by_id("login-form-username").send_keys("zhangdelong")
                driver.find_element_by_id("login-form-password").clear()
                driver.find_element_by_id("login-form-password").send_keys("131415")
                driver.find_element_by_id("login").click()
                # ERROR: Caught exception [ERROR: Unsupported command [selectWindow | null | ]]
                #找到下拉菜单的方式，直接用ID
                driver.find_element_by_id("admin_menu").click()
                driver.find_element_by_id("admin_system_menu").click()
                #clear 清除对象的内容，如果可以的话
                driver.find_element_by_id("login-form-authenticatePassword").clear()
                driver.find_element_by_id("login-form-authenticatePassword").send_keys("131415")
                #提交
                driver.find_element_by_id("login-form-submit").click()
                #找到发送邮件的项目
                driver.find_element_by_id("mail_queue").click()
                #根据CSS找到错误队列的地方，再点击"重新发送错误队列"
                driver.find_element_by_css_selector("a > strong").click()
                driver.find_element_by_link_text(u"重新发送错误队列").click()
                #根据CSS找到邮件队列的地方，再点击"发送队列中的邮件"
                driver.find_element_by_css_selector("a > strong").click()
                driver.find_element_by_link_text(u"发送队列中的邮件").click()
        def is_element_present(self, how, what):
            try: self.driver.find_element(by=how, value=what)
            except NoSuchElementException, e: return False
            return True
        def is_alert_present(self):
            try: self.driver.switch_to_alert()
            except NoAlertPresentException, e: return False
            return True
        def close_alert_and_get_its_text(self):
            try:
                alert = self.driver.switch_to_alert()
                alert_text = alert.text
                if self.accept_next_alert:
                    alert.accept()
                else:
                    alert.dismiss()
                return alert_text
            finally: self.accept_next_alert = True
        def tearDown(self):
            self.driver.quit()
            self.assertEqual([], self.verificationErrors)
        time.sleep(5)

