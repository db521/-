# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

class Fa(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "http://192.168.1.245:9999/secure/MyJiraHome.jspa"

  #      self.verificationErrors = []
 #       self.accept_next_alert = True

    def test_fa(self):
        driver = self.driver
        driver.find_element_by_id("login-form-username").send_keys("zhangdelong")
        driver.find_element_by_id("login-form-password").send_keys("131415")
        driver.find_element_by_id("login").click()
        driver.get(self.base_url + "/secure/Dashboard.jspa")
        driver.find_element_by_id("admin_menu").click()
        driver.find_element_by_id("admin_system_menu").click()
        driver.find_element_by_id("login-form-authenticatePassword").clear()
        driver.find_element_by_id("login-form-authenticatePassword").send_keys("131415")
        driver.find_element_by_id("login-form-submit").click()
        driver.find_element_by_id("mail_queue").click()
        driver.find_element_by_link_text(u"发送队列中的邮件").click()
    
    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException, e: return False
        return True
    

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
