'''
Created on 2018年6月19日

@author: admin
'''
from PO import BasePage
from selenium.webdriver.common.by import By
class collect_page(object):
    collect_loc=(By.ID,'com.uniview.app.smb.phone.en.ezview:id/alm_collect')
    def collect_loc(self):
        self.driver.find_element(*self.collect_loc).click()
        