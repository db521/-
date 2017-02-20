
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

#找到其下面的ifrome2(id =gadget-0)
browser.switch_to_frame("gadget-0")
#登录用xpath方式
browser.find_element_by_xpath('//*[@id="login-form-username"]').send_keys("zhangdelong")
browser.find_element_by_xpath('//*[@id="login-form-password"]').send_keys("131415")
browser.find_element_by_xpath('//*[@id="login"]').click()
#查找下拉菜单项
#点击Link1链接（弹出下拉列表）
#drop_down = browser.find_element_by_css_selector("div#aui-header-secondary > ul")
#drop_down.find_element_by_id("system-admin-menu").click()
#/secure/project/ViewProjects.jspa
browser.find_element_by_link_text('http://192.168.1.245:9999/secure/project/ViewProjects.jspa')

browser.find_element_by_xpath('//*[@id="system-admin-menu-content"]')
browser.quit()
browser.close()

'''
#找到id 为dropdown1的父元素
browser.find_element_by_xpath('//*[@id="admin_menu"]').is_displayed()
#在父亲元件下找到link 为Action 的子元素
menu = dr.find_element_by_id('dropdown1').find_element_by_link_text('Action')
#鼠标定位到子元素上
webdriver.ActionChains(dr).move_to_element(menu).perform()
time.sleep(2)
'''
