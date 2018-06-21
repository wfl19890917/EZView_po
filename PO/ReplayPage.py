'''
Created on 2018年6月19日

@author: admin
'''
from selenium.webdriver.common.by import By
from PO import BasePage
class replay_page(BasePage.base_page):
    playback_loc=(By.ID,'com.uniview.app.smb.phone.en.ezview:id/act_playback')
    title_loc=(By.ID,'com.uniview.app.smb.phone.en.ezview:id/textView1')
    def click_playback_loc(self):
        self.find_element(*self.playback_loc).click()
    def get_title_loc(self):
        return self.find_element(*self.title_loc).text
        
        