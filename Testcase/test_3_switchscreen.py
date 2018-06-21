'''
Created on 2018年6月19日

@author: admin
'''
import unittest
from selenium import webdriver
from appium import webdriver
from Public import driver
from PO import ChangeScreenPage
class Test(unittest.TestCase):
    def setUp(self):
        self.driver=webdriver.Remote('http://127.0.0.1:4723/wd/hub',driver.MyDriver.desired_caps)
    def tearDown(self):
        self.driver.quit()
    def test_change_1screen_video(self):
        e=self.driver.find_elements_by_xpath('//android.widget.RelativeLayout[@resource-id="com.uniview.app.smb.phone.en.ezview:id/playview_container_bg"]')
        if int(len(e))==4:
            change_screen=ChangeScreenPage.change_page(self.driver)
            change_screen.click_change_one_screen_loc()
            e=self.driver.find_elements_by_xpath('//android.widget.RelativeLayout[@resource-id="com.uniview.app.smb.phone.en.ezview:id/playview_container_bg"]')
            print("当前屏幕为：%d"%(len(e)))
    def test_change_9screen_video(self):
        change_screen=ChangeScreenPage.change_page(self.driver)
        change_screen.click_change_nine_screen_loc()
        e=self.driver.find_elements_by_xpath('//android.widget.RelativeLayout[@resource-id="com.uniview.app.smb.phone.en.ezview:id/playview_container_bg"]')
        if int(len(e))==9:
            print("当前屏幕为：%d"%(len(e)))
    def test_change_16screen_video(self):
        change_screen=ChangeScreenPage.change_page(self.driver)
        change_screen.click_change_sixteen_screen_loc()
        e=self.driver.find_elements_by_xpath('//android.widget.RelativeLayout[@resource-id="com.uniview.app.smb.phone.en.ezview:id/playview_container_bg"]')
        if int(len(e))==16:
            print("当前屏幕为：%d"%(len(e)))
    def test_change_4screen_video(self):
        change_screen=ChangeScreenPage.change_page(self.driver)
        change_screen.click_change_four_screen_loc()
        e=self.driver.find_elements_by_xpath('//android.widget.RelativeLayout[@resource-id="com.uniview.app.smb.phone.en.ezview:id/playview_container_bg"]')
        if int(len(e))==4:
            print("当前屏幕为：%d"%(len(e)))
        
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    suite=unittest.TestSuite()
    suite.addTest(Test('test_change_1screen_video'))
    suite.addTest(Test('test_change_9screen_video'))
    suite.addTest(Test('test_change_16screen_video'))
    suite.addTest(Test('test_change_4screen_video'))
    runner=unittest.TextTestRunner(verbosity=2)
    runner.run(suite)