'''
Created on 2018年6月19日

@author: admin
'''
from PO import BasePage
from selenium.webdriver.common.by import By
class screenshot_page(BasePage.base_page):
    screccsshot_loc=(By.ID,'com.uniview.app.smb.phone.en.ezview:id/act_sreccsshots')
    lookpu_video_loc=(By.ID,'com.uniview.app.smb.phone.en.ezview:id/port_look_up')
    def click_sreccsshot_loc(self):
        self.driver.find_element(*self.sreccsshot_loc).click()
    def click_lookup_video(self,*loc):
        self.find_element(*self.lookpu_video_loc).click()

        