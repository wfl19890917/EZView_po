'''
Created on 2018年6月22日

@author: admin
'''
from appium import webdriver
from selenium.webdriver.common.by import By
from PO import BasePage
class confir_page(BasePage.base_page):
    title_loc=(By.ID,'com.uniview.app.smb.phone.en.ezview:id/loca_config_title')
    passprotected_loc=(By.ID,'com.uniview.app.smb.phone.en.ezview:id/alcPassSwitch')
    gesture_loc=(By.XPATH,"//android.widget.TextView[@text='手势密码']")
    draw_loc=(By.ID,'com.uniview.app.smb.phone.en.ezview:id/gesturepwd_create_text')
    
    def get_configure_title(self):
        return self.find_element(*self.title_loc).text
    def click_passprotected(self):
        self.find_element(*self.passprotected_loc).click()
    def click_gesture(self):
        self.find_element(*self.gesture_loc).click()
        
    
        