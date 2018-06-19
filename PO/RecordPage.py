'''
Created on 2018年6月19日

@author: admin
'''
from PO import BasePage
from selenium.webdriver.common.by import By
class record_page(BasePage.base_page):
    record_loc=(By.ID,'com.uniview.app.smb.phone.en.ezview:id/al_Record')
    def click_record_loc(self):
        self.driver.find_element(*self.record_loc).click()
        