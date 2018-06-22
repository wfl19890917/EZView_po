'''
Created on 2018年6月19日

@author: admin
'''
import unittest
from selenium import webdriver
from appium import webdriver
from Public import driver
from PO import AddvideoPage
from selenium.webdriver.common.by import By
import time
from appium.webdriver.common.touch_action import TouchAction
class Test(unittest.TestCase):
    def setUp(self):
        self.driver=webdriver.Remote('http://127.0.0.1:4723/wd/hub',driver.MyDriver.desired_caps)
    def tearDown(self):
        self.driver.quit()
    def test_add_video(self):
        for i in range(0,4):
            add_video=AddvideoPage.living_page(self.driver)
            add_video.click_add_video_loc(i)
            add_video.click_ezview_demo_loc(0)
            add_video.click_camera_loc(i)
            print('添加成功')
    def test_double_big_video(self):
        for i in range(2):
            self.driver.tap([(2,150),])
        time.sleep(2)
        print("放大成功")
    def test_double_small_video(self):
        for i in range(2):
            self.driver.tap([(2,150),])
        time.sleep(2)
        print('缩小成功')
    def test_move_video(self):
        time.sleep(5)
        el=self.driver.find_elements(By.XPATH,'//android.widget.RelativeLayout[@resource-id="com.uniview.app.smb.phone.en.ezview:id/playview_container_bg"]')[0]
        TouchAction(self.driver).press(el).wait(5000).perform()
        el2=self.driver.find_elements(By.XPATH,'//android.widget.RelativeLayout[@resource-id="com.uniview.app.smb.phone.en.ezview:id/playview_container_bg"]')[1]
        TouchAction(self.driver).move_to(el2).release().perform()
        time.sleep(5)
        print('视频移动成功') 
    def test_delete_video(self):
        el=self.driver.find_elements(By.XPATH,'//android.widget.RelativeLayout[@resource-id="com.uniview.app.smb.phone.en.ezview:id/playview_container_bg"]')[1]
        TouchAction(self.driver).press(el).wait(5000).perform()
        el2=self.driver.find_element(By.ID,'com.uniview.app.smb.phone.en.ezview:id/iv_delete')
        TouchAction(self.driver).move_to(el2).release().perform()
        time.sleep(5)
        print('删除视频成功')
    def test_revoke_video(self):
        revoke_video=AddvideoPage.living_page(self.driver)
        revoke_video.click_rovoke_video_loc()           
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    suite=unittest.TestSuite()
    suite.addTest(Test('test_add_video'))
    suite.addTest(Test('test_change_screen_video'))
    suite.addTest(Test('test_move_video'))
    suite.addTest(Test('test_double_big_video'))
    suite.addTest(Test('test_double_small_video'))
    suite.addTest(Test('test_delete_video'))
    suite.addTest(Test('test_revoke_video'))
    runner=unittest.TextTestRunner(verbosity=2)
    runner.run(suite)
    