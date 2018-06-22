'''
Created on 2018年6月22日

@author: admin
'''
import unittest
from selenium import webdriver
from appium import webdriver
from PO import MenuPage,ConfigurePage
from Public import driver,gesture

class Test(unittest.TestCase):


    def setUp(self):
        self.driver=webdriver.Remote('http://127.0.0.1:4723/wd/hub',driver.MyDriver.desired_caps)
    def tearDown(self):
        self.driver.quit()
    def test_lock(self):
        menu=MenuPage.menu_page(self.driver)
        menu.click_menbtn()
        menu.click_configure()
        config=ConfigurePage.confir_page(self.driver)
        self.assertTrue('配置', config.get_configure_title())
        config.click_passprotected()
        config.click_gesture()
        gesture.setLock()
    def test_unlock(self):
        gesture.unLock()
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()