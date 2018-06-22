'''
Created on 2018年6月22日

@author: admin
'''
import unittest
from PO import MenuPage
from Public import driver
from selenium import webdriver
from appium import webdriver

class Test(unittest.TestCase):


    def setUp(self):
        self.driver=webdriver.Remote('http://127.0.0.1:4723/wd/hub',driver.MyDriver.desired_caps)


    def tearDown(self):
        self.driver.quit()


    def test_notice(self):
        menu=MenuPage.menu_page(self.driver)
        menu.click_menbtn()
        menu.click_notice()


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()