'''
Created on 2018年6月19日

@author: admin
'''
from PO import BasePage
from selenium.webdriver.common.by import By
from appium import webdriver
import time
class collect_page(BasePage.base_page):
    collect_loc=(By.ID,'com.uniview.app.smb.phone.en.ezview:id/alm_collect')
    titile_loc=(By.ID,'com.uniview.app.smb.phone.en.ezview:id/modifyNotify')
    container_loc=(By.XPATH,'//android.widget.RelativeLayout[@resource-id="com.uniview.app.smb.phone.en.ezview:id/playview_container_bg"]')
    input_name_loc=(By.ID,'com.uniview.app.smb.phone.en.ezview:id/modifyCName')
    sure_loc=(By.ID,'com.uniview.app.smb.phone.en.ezview:id/modifyDetermine')
    cancel_loc=(By.ID,'com.uniview.app.smb.phone.en.ezview:id/modifyCancel')
    delete_ok_loc=(By.ID,'com.uniview.app.smb.phone.en.ezview:id/ok_btn')
    delete_cancel_loc=(By.ID,'com.uniview.app.smb.phone.en.ezview:id/cancel_btn')
    delete_title_loc=(By.ID,'com.uniview.app.smb.phone.en.ezview:id/dialog_title')
    def click_collect_loc(self):
        self.driver.find_element(*self.collect_loc).click()
    def click_container_loc(self,index):
        e=self.find_elements(*self.container_loc)[index]
        e.click()
    def input_collect_name_loc(self,name):
        self.find_element(*self.input_name_loc).send_keys(name)
    def click_collect_sure(self):
        self.find_element(*self.sure_loc).click()
    def click_collect_cancel(self):
        self.find_element(*self.cancel_loc).click()
    def click_delete_collect_cancel(self):
        self.find_element(*self.delete_cancel_loc).click()
    def click_delete_collect_ok(self):
        self.find_element(*self.delete_ok_loc).click()
        