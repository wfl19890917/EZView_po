'''
Created on 2018年6月19日

@author: admin
'''
import unittest
from selenium import webdriver
from appium import webdriver
from Public import driver
from PO import RecordPage
from selenium.webdriver.common.by import By
import time
from Public import toast
class Test(unittest.TestCase):
    def setUp(self):
        self.driver=webdriver.Remote('http://127.0.0.1:4723/wd/hub',driver.MyDriver.desired_caps)
    def tearDown(self):
        self.driver.quit()
    def test_record_start(self):
        record_video=RecordPage.record_page(self.driver)
        record_video.click_record_loc()
        record_video.click_record_loc()
        find_toast=toast.is_toast_exist(self.driver, '开始录像', 10, 0.01)
        print('开始录像')
    def test_record_less_3s_video(self):
        record_video=RecordPage.record_page(self.driver)
        record_video.click_record_loc()
        record_video.click_record_loc()
        find_toast=toast.is_toast_exist(self.driver, '录制时间小于3s，请重新录制', 10, 0.01)
        print('录制时间小于3s，请重新录制')
    def test_recored_more_3s_video(self):
        record_video=RecordPage.record_page(self.driver)
        record_video.click_record_loc()
        time.sleep(5)
        record_video.click_record_loc()
        self.assertTrue(self.driver.find_element_by_name('录像已保存').is_displayed())
        print('录像保存成功')
    def test_record_lookpu_video(self):
        record_video=RecordPage.record_page(self.driver)
        record_video.click_record_loc()
        time.sleep(5)
        record_video.click_record_loc()
        self.driver.find_element_by_id('com.uniview.app.smb.phone.en.ezview:id/port_look_up').click()
        self.driver.find_element_by_id('com.uniview.app.smb.phone.en.ezview:id/file_ll_view_back').click()  
        print('查看录像成功')    
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()