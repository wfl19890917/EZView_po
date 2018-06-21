'''
Created on 2018年6月19日

@author: admin
'''
from PO import BasePage
from selenium.webdriver.common.by import By
class record_page(BasePage.base_page):
    record_loc=(By.ID,'com.uniview.app.smb.phone.en.ezview:id/al_Record')
    lookup_loc=(By.ID,'com.uniview.app.smb.phone.en.ezview:id/port_look_up')
    back_loc=(By.ID,'com.uniview.app.smb.phone.en.ezview:id/file_ll_view_back')
    def click_record_loc(self):
        self.find_element(*self.record_loc).click()
    def click_lookup_loc(self):
        self.find_element(*self.lookup_loc).click()
    def click_back_loc(self):
        self.find_element(*self.back_loc).click()
        