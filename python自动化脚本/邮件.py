
# -*- coding: utf-8 -*-
from selenium import selenium
import unittest, time, re

class 发送邮件2(unittest.TestCase):
    def setUp(self):
        self.verificationErrors = []
        self.selenium = selenium("localhost", 4444, "*chrome", "http://192.168.1.245:9999/secure/MyJiraHome.jspa")
        self.selenium.start()
    
    def test_发送邮件2(self):
        sel = self.selenium
        sel.open("/secure/MyJiraHome.jspa")
        sel.click("id=errorTryAgain")
        sel.wait_for_page_to_load("30000")
        sel.click("id=admin_menu")
        sel.click("id=admin_system_menu")
        sel.wait_for_page_to_load("30000")
        sel.type("id=login-form-authenticatePassword", "131415")
        sel.click("id=login-form-submit")
        sel.wait_for_page_to_load("30000")
        sel.click("id=mail_queue")
        sel.wait_for_page_to_load("30000")
        sel.click(u"link=发送队列中的邮件")
        sel.wait_for_page_to_load("30000")
    
    def tearDown(self):
        self.selenium.stop()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
