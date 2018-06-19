'''
Created on 2018年6月19日

@author: admin
'''
from appium import webdriver
from selenium.webdriver.common.by import By
from PO import BasePage
from selenium import webdriver
import time
from appium.webdriver.common.touch_action import TouchAction
class living_page(BasePage.base_page):
    add_video_loc=(By.XPATH,'//android.widget.ImageView[@resource-id="com.uniview.app.smb.phone.en.ezview:id/playview_addvideo"]')
    ezview_demo_loc=(By.XPATH,'//android.widget.RelativeLayout[@resource-id="com.uniview.app.smb.phone.en.ezview:id/icg_rl_name_playing"]')
    camera_loc=(By.XPATH,'//android.widget.TextView[@resource-id="com.uniview.app.smb.phone.en.ezview:id/icg_tv_node_name"]')
   
    def click_add_video_loc(self,index):
        e=self.driver.find_elements(*self.add_video_loc)[index]
        e.click()
        time.sleep(2)
    def click_ezview_demo_loc(self,index):
        e=self.driver.find_elements(*self.ezview_demo_loc)[index]
        e.click()
        time.sleep(2)
    def click_camera_loc(self,index):
        e=self.driver.find_elements(*self.camera_loc)[index]
        e.click()
        time.sleep(2)
    
   
    
    
    
    
    
        
    
    
    
    
    
    
      
        