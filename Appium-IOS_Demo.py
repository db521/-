#-*- coding: UTF-8 -*-
import os
import time
import unittest
from appium import webdriver
from lib2to3.pgen2.driver import Driver
from lib2to3.tests.support import driver
 
PATH=lambda p:os.path.abspath(
os.path.join(os.path.dirname(__file__),p)                            
)
global driver
 
class LoginAndroidTests(unittest.TestCase):
    def setUp(self):
        print time.time()
        desired_caps={}
        desired_caps['deviceName'] = 'iPhone 5s'
        #desired_caps['deviceName'] = 'iPhone 6'
        desired_caps['platformName']='ios'
        desired_caps['browserName']=''
        desired_caps['platformVersion']='8.2'
       # desired_caps['platformVersion']='8.1.2'
        desired_caps['bundleId']='com.nbcb.mobilebank.0914'
        desired_caps['udid']='781534f9ede8f6f2c8469522659fddac7e213b82'
        #desired_caps['udid']='d542d749953b228ba23aa6495227da8debcdd858'

        #desired_caps['unicodeKeyboard']='true'
        print "Create sesssion"	
        #self.driver=webdriver.Remote('http://192.168.110.130:4723/wd/hub',desired_caps)
		self.driver=webdriver.Remote('http://localhost:4723/wd/hub',desired_caps)
       
    def tearDown(self):
        #self.driver.quit()
        time.sleep(1)
   
    def test_login(self):
        time.sleep(1)
        #选择环境
        
        print "Select Envirenment"
        button=self.driver.find_element_by_name("62")
        button.click()
        time.sleep(2)
        
        #点击“登录”按钮
        print "Click Login"
        button=self.driver.find_element_by_name("登录")
        button.click()
        time.sleep(1)

        #输入账户
        print "Input Account"
        el=self.driver.find_element_by_id("登录名/账号/身份证")
        el.click()
        el.send_keys("6223161800618561")
        
        el=self.driver.find_element_by_id("请输入查询密码")
        el.click()

        print "Input Password"
        button=self.driver.find_element_by_name("1")
        i=0
        while(i<6):
            button.click()
            i+=1

        
        button=self.driver.find_element_by_name("登录")
        button.click()
        
    
        time.sleep(5)
        print time.time()
        #self.driver.quit()
       
        
        #此处加上检测登录是否成功的代码
if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(LoginAndroidTests)
    unittest.TextTestRunner(verbosity=2).run(suite)
