'''
Created on 2018年6月19日

@author: admin
'''
import unittest
from selenium import webdriver
from appium import webdriver
from Public import driver
from PO import ScreenshotPage
from selenium.webdriver.common.by import By
import time
from Public import toast
class Test(unittest.TestCase):
    def setUp(self):
        self.driver=webdriver.Remote('http://127.0.0.1:4723/wd/hub',driver.MyDriver.desired_caps)
    def tearDown(self):
        self.driver.quit()
    def test_screenshot_no_video(self):
        screenshot=ScreenshotPage.screenshot_page(self.driver)
        screenshot.click_sreccsshot_loc()
        find_toast=toast.is_toast_exist(self.driver, '请选择通道', 10, 0.01)
        if find_toast==False:
            print('未获取到toast：请选择通道%s'%(find_toast))
        else:
            print('获取toast成功%s'%(find_toast))
    def test_screenshot_with_video(self):
        screenshot=ScreenshotPage.screenshot_page(self.driver)
        screenshot.click_sreccsshot_loc()
        self.assertTrue(self.driver.find_element_by_name('图片已保存').is_displayed())
        print('图片保存成功')
    def test_screenshot_with_lookup_vido(self):
        screenshot=ScreenshotPage.screenshot_page(self.driver)
        screenshot.click_sreccsshot_loc()
        self.driver.find_element_by_id('com.uniview.app.smb.phone.en.ezview:id/port_look_up').click()
        self.driver.find_element_by_id('com.uniview.app.smb.phone.en.ezview:id/file_ll_view_back').click()      
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    suite=unittest.TestSuite()
    suite.addTest(Test('test_screenshot_no_video'))
    suite.addTest(Test('test_screenshot_with_video'))
    suite.addTest(Test('test_screenshot_with_lookup_vido'))
    unittest.TextTestRunner(verbosity=2).run(suite)