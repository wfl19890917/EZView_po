'''
Created on 2018年6月22日

@author: admin
'''
from PO import BasePage
from selenium.webdriver.common.by import By
class favor_page(BasePage.base_page):
    titile_loc=(By.ID,'com.uniview.app.smb.phone.en.ezview:id/afShouCangJia')
    add_collect_loc=(By.ID,'com.uniview.app.smb.phone.en.ezview:id/afBtnAdd')
    device_loc=(By.XPATH,'//android.widget.TextView[@resource-id="com.uniview.app.smb.phone.en.ezview:id/iflDeviceName"]')
    text_loc=(By.ID,'com.uniview.app.smb.phone.en.ezview:id/favoritestext')
    more_loc=(By.ID,'com.uniview.app.smb.phone.en.ezview:id/RelativeLayout1')
    live_loc=(By.ID,'com.uniview.app.smb.phone.en.ezview:id/ddi_tv_live')
    edit_loc=(By.ID,'com.uniview.app.smb.phone.en.ezview:id/tv_edit')
    rename_loc=(By.ID,'com.uniview.app.smb.phone.en.ezview:id/tv_speed_test')
    delete_loc=(By.ID,'com.uniview.app.smb.phone.en.ezview:id/tv_delete')
    def get_favor_title(self):
        return self.find_element(*self.titile_loc).text
    def get_text(self):
        return self.find_element(*self.text_loc).text
    def click_more(self):
        self.find_element(*self.more_loc).click()
    def click_live(self):
        self.find_element(*self.live_loc).click()
    def click_edit(self):
        self.find_element(*self.edit_loc).click()
    def click_rename(self):
        self.find_element(*self.rename_loc).click()
    def click_delete(self):
        self.find_element(*self.delete_loc).click()
    
    
        