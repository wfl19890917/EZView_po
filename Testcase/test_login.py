'''
Created on 2018年6月21日

@author: admin
'''
import unittest
from selenium import webdriver
from appium import webdriver
from Public import driver_reset,SwipeTo
from PO import LoginPage
import time

class Test(unittest.TestCase):
    def setUp(self):
        self.driver=webdriver.Remote('http://127.0.0.1:4723/wd/hub',driver_reset.MyDriver.desired_caps)
        time.sleep(2)
        SwipeTo.swipLeft(self.driver,500)
        time.sleep(2)
        SwipeTo.swipLeft(self.driver,500)
        self.driver.find_element_by_id('com.uniview.app.smb.phone.en.ezview:id/wnf_five').click()
        time.sleep(2)
        self.driver.find_element_by_id('com.uniview.app.smb.phone.en.ezview:id/close_dialog').click()
        print("滑动启动页成功")
    def tearDown(self):
        self.driver.quit()
    def test_tiyan(self):
        login=LoginPage.Login_page(self.driver)
        login.click_tiyan()
        time.sleep(3)
        #获取当前界面的activity
        act=self.driver.current_activity
        print(act)
        source=self.driver.page_source.find(u"实况")
        if source!=-1:
            print("成功进入实况页")
        else:
            print(source)
    def test_login_all_null(self):
        login=LoginPage.Login_page(self.driver)
        login.input_username('')
        login.input_password('')
        login.click_loginbtn()
        print("请输入用户名密码")
    def test_login_username_null(self):
        login=LoginPage.Login_page(self.driver)
        login.input_username('')
        login.input_password('wfl890917')
        login.click_loginbtn()
        print("请输入用户名密码")
    def test_login_password_null(self):
        login=LoginPage.Login_page(self.driver)
        login.input_username('18201557582')
        login.input_password('')
        login.click_loginbtn()
        print("请输入用户名密码")
    def test_login_username_error(self):
        login=LoginPage.Login_page(self.driver)
        login.input_username('18201557580')
        login.input_password('wfl890917')
        login.click_loginbtn()
        print("请输入用户名密码")
    def test_login_password_error(self):
        login=LoginPage.Login_page(self.driver)
        login.input_username('18201557582')
        login.input_password('wfl89091')
        login.click_loginbtn()
        print("密码输入错误 ")
    def test_login_success(self):
        LoginPage.userlogin(self)
        
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    suite=unittest.TestSuite()
    suite.addTest(Test('test_tiyan'))
    suite.addTest(Test('test_login_all_null'))
    suite.addTest(Test('test_login_username_null'))
    suite.addTest(Test('test_login_password_null'))
    suite.addTest(Test('test_login_username_error'))
    suite.addTest(Test('test_login_password_error'))
    suite.addTest(Test('test_login_success'))
    unittest.TextTestRunner(verbosity=2).run(suite)