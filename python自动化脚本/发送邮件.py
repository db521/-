#coding=UTF-8
from selenium import webdriver
import unittest, time, re

class sendmail(unittest.TestCase):
    def setUp(self):
        self.verificationErrors = []
        browser = webdriver.Chrome(executable_path=r"C:\Program Files (x86)\Google\Chrome\Application\chromedriver_x64.exe")
        self.selenium = webdriver.Chrome("localhost", 4444, "browser", "http://192.168.1.245:9999/secure/MyJiraHome.jspa")
  #      self.selenium = webdriver.Chrome("localhost", 4444, "*chrome", "http://192.168.1.245:9999/secure/MyJiraHome.jspa")
  #      self.selenium.start()

    def test_sendmail(self):
        sel = self.selenium
        sel.open("/secure/Dashboard.jspa")
        sel.select_frame("gadget-0")
        sel.type("id=login-form-username", "zhangdelong")
        sel.type("id=login-form-password", "131415")
        sel.click("id=admin_menu")
        sel.click("css=img[alt=\"zhangdelong\"]")
        sel.click("id=admin_system_menu")
        sel.wait_for_page_to_load("30000")
        sel.type("id=login-form-authenticatePassword", "131415")
        sel.click("id=login-form-submit")
        sel.wait_for_page_to_load("30000")
        sel.click("id=mail_queue")
        sel.wait_for_page_to_load("30000")
        sel.click(u"link=发送队列中的邮件")
        sel.wait_for_page_to_load("30000")
        sel.click(u"link=错误队列 (123)")
        sel.wait_for_page_to_load("30000")
        sel.click(u"link=重新发送错误队列")
        sel.wait_for_page_to_load("30000")
        sel.click("css=a > strong")
        sel.wait_for_page_to_load("30000")
        sel.click(u"link=发送队列中的邮件")
        sel.wait_for_page_to_load("30000")

    def tearDown(self):
        self.selenium.stop()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
