'''
Created on 2018年6月21日

@author: admin
'''
from PO import BasePage
from appium import webdriver
from selenium.webdriver.common.by import By
class myinfo_page(BasePage.base_page):
    username_loc=(By.ID,'com.uniview.app.smb.phone.en.ezview:id/acai_username')
    logoutbtn_loc=(By.ID,'com.uniview.app.smb.phone.en.ezview:id/acaiSwitchAccount')
    def click_username(self):
        self.find_element(*self.username_loc).click()
    
    
    
    
        