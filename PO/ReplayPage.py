'''
Created on 2018年6月19日

@author: admin
'''
from selenium.webdriver.common.by import By
from PO import BasePage
class MyClass(BasePage.base_page):
    playback_loc=(By.ID,'com.uniview.app.smb.phone.en.ezview:id/act_playback')
    def click_playback_loc(self):
        self.driver.find_element(*self.playback_loc).click()
        