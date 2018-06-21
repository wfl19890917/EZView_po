'''
Created on 2018年6月19日

@author: admin
'''
from PO import BasePage
from selenium.webdriver.common.by import By
class screenshot_page(BasePage.base_page):
    sreccsshot_loc=(By.ID,'com.uniview.app.smb.phone.en.ezview:id/act_sreccsshots')
    lookpu_video_loc=(By.ID,'com.uniview.app.smb.phone.en.ezview:id/port_look_up')
    back_loc=(By.ID,'com.uniview.app.smb.phone.en.ezview:id/file_ll_view_back')
    def click_sreccsshot_loc(self):
        self.find_element(*self.sreccsshot_loc).click()
    def click_lookup_video(self):
        self.find_element(*self.lookpu_video_loc).click()
    def click_back_loc(self):
        self.find_element(*self.back_loc).click()

        