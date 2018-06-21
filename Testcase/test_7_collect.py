'''
Created on 2018年6月19日

@author: admin
'''
import unittest
from PO import CollectPage
from Public import driver
from selenium import webdriver
from appium import webdriver
import time

class Test(unittest.TestCase):
    def setUp(self):
        self.driver=webdriver.Remote('http://127.0.0.1:4723/wd/hub',driver.MyDriver.desired_caps)
    def tearDown(self):
        self.driver.quit()
    def test_collect_shuru_cancel(self):
        time.sleep(5)
        collect=CollectPage.collect_page(self.driver)
        collect.click_collect_loc()
        collect.click_collect_cancel()
        print("取消成功")
    def test_collect_shuru_sure(self):
        time.sleep(5)
        collect=CollectPage.collect_page(self.driver)
        collect.click_container_loc(1)
        collect.click_collect_loc()
        collect.input_collect_name_loc('交通视频1')
        time.sleep(2)
        collect.click_collect_sure()
        time.sleep(2)
        print("收藏成功")
    def test_collect_delete_cancel(self):
        time.sleep(5)
        collect=CollectPage.collect_page(self.driver)
        collect.click_collect_loc()
        time.sleep(2)
        collect.click_delete_collect_cancel()
        print("删除成功")
    def test_collect_delete_ok(self):
        time.sleep(5)
        collect=CollectPage.collect_page(self.driver)
        collect.click_collect_loc()
        time.sleep(2)
        collect.click_delete_collect_ok()
        print("删除成功")
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    suite=unittest.TestSuite()
    suite.addTest(Test('test_collect_shuru_cancel'))
    suite.addTest(Test('test_collect_shuru_sure'))
    suite.addTest(Test('test_collect_delete_cancel'))
    suite.addTest(Test('test_collect_delete_ok'))
    unittest.TextTestRunner(verbosity=2).run(suite)