#coding=utf-8
import os
#test app
import time
from appium import webdriver

#test
PATH=lambda p:os.path.abspath(os.path.join(os.path.dirname(__file__),p))
desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '4.4.2'
desired_caps['deviceName'] = 'Android Emulator'
desired_caps['app']=PATH('D:\\app-c-daodao-20170117-1737-v1.2.0.apk')
driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
# desired_caps['appActivity'] = '.Calculator'
# desired_caps['appPackage'] = 'com.android.calculator2'

time.sleep(20)
driver.find_element_by_id('com.dongdao.daodao:id/home_iv_guide_requirement').click()
driver.find_element_by_class_name('android.widget.ImageView').click()
driver.find_element_by_class_name('android.widget.ImageView').click()

driver.find_element_by_id('com.dongdao.daodao:id/home_page_tv_morecase').click()
driver.find_element_by_id('com.dongdao.daodao:id/title_bar_iv_right').click()
#发布需求,先登录
driver.find_element_by_id('com.dongdao.daodao:id/login_et_account').send_keys('18500313747')
driver.find_element_by_id('com.dongdao.daodao:id/login_et_password').send_keys('111111')
driver.find_element_by_id('com.dongdao.daodao:id/login_bt_save').click()
time.sleep(10)
driver.find_element_by_id('com.dongdao.daodao:id/add_order_form_et_theme_content').send_keys(u'test')
#选择业务分类
driver.find_element_by_id('com.dongdao.daodao:id/add_order_form_tv_requirement_classify_content').click()
#选择第一个业务分类
driver.find_element_by_id('com.dongdao.daodao:id/requirement_classify_iv_status').click()
#点确定返回到发布需求页
driver.find_element_by_id('com.dongdao.daodao:id/title_bar_tv_right').click()
time.sleep(1)
#预算
driver.find_element_by_id('com.dongdao.daodao:id/add_order_form_et_budget_content').send_keys('1000')
#交付时间
driver.find_element_by_id('com.dongdao.daodao:id/add_order_form_tv_delivery_time_content').click()

#需求描述
driver.find_element_by_id('com.dongdao.daodao:id/add_order_form_et_requirement_content').send_keys('内容内容')
#点发布需求按钮
driver.find_element_by_id('com.dongdao.daodao:id/add_order_form_bt_save').click()
time.sleep(5)


