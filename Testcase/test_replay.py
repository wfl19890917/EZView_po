'''
Created on 2018年6月19日

@author: admin
'''
import unittest
from PO import MenuPage
from selenium import webdriver
from appium import webdriver
from Public import driver
class Test(unittest.TestCase):


    def setUp(self):
        self.driver=webdriver.Remote('http://127.0.0.1:4723/wd/hub',driver.MyDriver.desired_caps)


    def tearDown(self):
        self.driver.quit()


    def test_replay(self):
        menu=MenuPage.menu_page(self.driver)
        menu.click_menbtn()
        menu.click_replay()
        if menu.get_replay_title()=='回放 ':
            print("成功跳转回放页 :"+menu.get_replay_title())


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()