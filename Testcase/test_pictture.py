'''
Created on 2018年6月22日

@author: admin
'''
import unittest
from selenium import webdriver
from appium import webdriver
from PO import MenuPage,PicturePage
from Public import driver

class Test(unittest.TestCase):
    def setUp(self):
        self.driver=webdriver.Remote('http://127.0.0.1:4723/wd/hub',driver.MyDriver.desired_caps)
    def tearDown(self):
        self.driver.quit()
    def test_picture(self):
        menu=MenuPage.menu_page(self.driver)
        menu.click_menbtn()
        menu.click_picture()
        pic=PicturePage.picute_page(self.driver)
        pic.click_picture()
        pic.click_vidoe()
        pic.click_edit()
        pic.click_selected()
        pic.click_delete()
        pic.click_ok_delete()
        print("删除成功")


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()