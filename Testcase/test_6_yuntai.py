'''
Created on 2018年6月19日

@author: admin
'''
import unittest
from selenium import webdriver
from appium import webdriver
from Public import driver
from PO import YuntaiPage
from selenium.webdriver.common.by import By
import time
from Public import toast
class Test(unittest.TestCase):
    def setUp(self):
        self.driver=webdriver.Remote('http://127.0.0.1:4723/wd/hub',driver.MyDriver.desired_caps)
    def tearDown(self):
        self.driver.quit()
    def test_yuntai_maintitle(self):
        yuntai=YuntaiPage.yuntai_page(self.driver)
        yuntai.click_yuntai_loc()
        yuntai.get_maintitle_loc()
    def test_yuntai_direct_text(self):
        yuntai=YuntaiPage.yuntai_page(self.driver)
        yuntai.click_yuntai_loc()
        yuntai.click_direct_loc()
        yuntai.get_opera_text()
    def test_yuntai_direct_large(self):
        time.sleep(5)
        yuntai=YuntaiPage.yuntai_page(self.driver)
        yuntai.click_yuntai_loc()
        yuntai.click_direct_loc()
        yuntai.click_opera_large()
    def test_yuntai_direct_small(self):
        yuntai=YuntaiPage.yuntai_page(self.driver)
        yuntai.click_yuntai_loc()
        yuntai.click_direct_loc()
        yuntai.click_opera_small()
    def test_yuntai_focus_text(self):
        time.sleep(5)
        yuntai=YuntaiPage.yuntai_page(self.driver)
        yuntai.click_yuntai_loc()
        yuntai.click_focus_loc()
        yuntai.get_opera_text()
    def test_yuntai_focus_large(self):
        yuntai=YuntaiPage.yuntai_page(self.driver)
        yuntai.click_yuntai_loc()
        yuntai.click_focus_loc()
        yuntai.click_opera_large()
    def test_yuntai_focus_small(self):
        yuntai=YuntaiPage.yuntai_page(self.driver)
        yuntai.click_yuntai_loc()
        yuntai.click_focus_loc()
        yuntai.click_opera_small()
    def test_yuntai_preset_sure(self):
        time.sleep(5)
        yuntai=YuntaiPage.yuntai_page(self.driver)
        yuntai.click_yuntai_loc()
        yuntai.click_preset_loc()
        yuntai.get_preset_text()
        #滑动选择
        self.driver.swipe(160,600,160,1000,2000)
        time.sleep(2)
        self.driver.swipe(250,600,250,1000,2000)
        time.sleep(2)
        self.driver.swipe(500,600,500,1000,2000)
        time.sleep(2)
        yuntai.click_preset_sure()
        print("选择位置成功")
    def test_yuntai_preset_cancel(self):
        time.sleep(5)
        yuntai=YuntaiPage.yuntai_page(self.driver)
        yuntai.click_yuntai_loc()
        yuntai.click_preset_loc()
        yuntai.get_preset_text()
        #滑动选择
        self.driver.swipe(160,600,160,1000,2000)
        time.sleep(2)
        self.driver.swipe(250,600,250,1000,2000)
        time.sleep(2)
        self.driver.swipe(500,600,500,1000,2000)
        time.sleep(2)
        yuntai.click_preset_cancel()
        print("取消选择位置")
    
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    suite=unittest.TestSuite()
    suite.addTest(Test('test_yuntai_maintitle'))
    suite.addTest(Test('test_yuntai_direct_text'))
    suite.addTest(Test('test_yuntai_direct_large'))
    suite.addTest(Test('test_yuntai_direct_small'))
    suite.addTest(Test('test_yuntai_focus_text'))
    suite.addTest(Test('test_yuntai_focus_large'))
    suite.addTest(Test('test_yuntai_focus_small'))
    suite.addTest(Test('test_yuntai_preset'))
    unittest.TextTestRunner(verbosity=2).run(suite)