
#coding=UTF-8
import sys
default_encoding = 'utf-8'
if sys.getdefaultencoding() != default_encoding:
    reload(sys)
    sys.setdefaultencoding(default_encoding)
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
import time


browser = webdriver.Chrome(executable_path=r"C:\Program Files (x86)\Google\Chrome\Application\chromedriver_x64.exe")

browser.get("http://192.168.1.245:9999/secure/MyJiraHome.jspa")
time.sleep(3)
browser.find_element_by_xpath('//*[@id="login-form-username"]').send_keys("XXX")

'''
try:
#kwddd 是一个无法找到的元素id
    browser.find_element_by_name("os_username").send_keys("zhangdelong")

except:
    browser.get_screenshot_as_file("c:\kw.png")
#如果没有找到上面的元素就截取当前页面。
header
assert "百度一下，你就知道" in browser.title

clicka = browser.find_element_by_name("os_username").send_keys("zhangdelong")

print browser.find_element_by_xpath
clickb = browser.find_element_by_id("login-form-password").send_keys("131415")
print clickb
time.sleep(3)
click1 = browser.find_element_by_id("admin_system_menu").click()
click2 = browser.find_element_by_id("login-form-authenticatePassword").send_keys("131415")
time.sleep(3)
click3 = browser.find_element_by_id("login-form-submit").click()

time.sleep(3)
click4 = browser.find_element_by_id("mail_queue").click()
time.sleep(3)
click5 = browser.find_element_by_name(u"发送队列中的邮件").click()
time.sleep(3)

browser.close()

'''