'''
Created on 2018年6月21日

@author: admin
'''
import unittest
from PO import LoginPage,MenuPage,MyInfoPage
from Public import driver
from selenium import webdriver
from appium import webdriver

class Test(unittest.TestCase):
    def setUp(self):
        self.driver=webdriver.Remote('http://127.0.0.1:4723/wd/hub',driver.MyDriver.desired_caps)
    def tearDown(self):
        self.driver.quit()
    def test_currentaccout(self):
        menu=MenuPage.menu_page(self.driver)
        menu.click_menbtn()
        if menu.get_currentname()=='您还没有登录哦~':
            menu.click_rentou()
            LoginPage.userlogin(self)
            menu.click_menbtn()
            print("用户名："+menu.get_cuname())
        else:
            print("已登录")
    def test_edit_name(self):
        myinfo=MyInfoPage.myinfo_page(self.driver)
        myinfo.edit_username('welcomeg123365')
        print("我的:"+myinfo.get_edit_username())
    def test_logout(self):
        menu=MenuPage.menu_page(self.driver)
        menu.click_menbtn()
        menu.click_rentou()
        MyInfoPage.userLogout(self)
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()