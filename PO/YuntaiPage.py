'''
Created on 2018年6月19日

@author: admin
'''
from PO import BasePage
from selenium.webdriver.common.by import By
class MyClass(BasePage.base_page):
    yuntai_loc=(By.ID,'com.uniview.app.smb.phone.en.ezview:id/act_yuntai')
    def click_yuntai_loc(self):
        self.driver.find_element(*self.yuntai_loc).click()

        