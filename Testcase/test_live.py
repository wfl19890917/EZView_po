'''
Created on 2018年6月20日

@author: admin
'''
import unittest
from PO import LoginPage,MenuPage,PicturePage
from Public import driver
from selenium import webdriver
from appium import webdriver
class Test(unittest.TestCase):
    def setUp(self):
        self.driver=webdriver.Remote('http://127.0.0.1:4723/wd/hub',driver.MyDriver.desired_caps)
    def tearDown(self):
        self.driver.quit()
    def test_live(self):
        menu=MenuPage.menu_page(self.driver)
        menu.click_menbtn()
        menu.click_shikuang()
        if menu.get_shikuang_title()=='实况':
            print("成功跳转实况页:"+menu.get_shikuang_title())
    
    
    
    
   
   
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    suite=unittest.TestSuite()
    unittest.TextTestRunner(verbosity=2).run(suite)