'''
Created on 2018年6月19日

@author: admin
'''
from PO import BasePage
from selenium.webdriver.common.by import By
class yuntai_page(BasePage.base_page):
    yuntai_loc=(By.ID,'com.uniview.app.smb.phone.en.ezview:id/act_yuntai')
    maintitle_loc=(By.ID,'com.uniview.app.smb.phone.en.ezview:id/main_title')
    direct_loc=(By.ID,'com.uniview.app.smb.phone.en.ezview:id/yuntai_direction')
    opera_text_loc=(By.ID,'com.uniview.app.smb.phone.en.ezview:id/text')
    opera_large_loc=(By.ID,'com.uniview.app.smb.phone.en.ezview:id/imageViewAdd')
    opera_small_loc=(By.ID,'com.uniview.app.smb.phone.en.ezview:id/imageViewDelete')
    focus_loc=(By.ID,'com.uniview.app.smb.phone.en.ezview:id/yuntai_focus')
    preset_loc=(By.ID,'com.uniview.app.smb.phone.en.ezview:id/yuntai_presetting')
    preset_text=(By.ID,'com.uniview.app.smb.phone.en.ezview:id/tcd_rl_time_text')
    preset_sure=(By.ID,'com.uniview.app.smb.phone.en.ezview:id/tcd_bt_confirm')
    preset_cancel=(By.ID,'com.uniview.app.smb.phone.en.ezview:id/tcd_bt_confirm')
    def click_yuntai_loc(self):
        self.driver.find_element(*self.yuntai_loc).click()
    def get_maintitle_loc(self):
        el=self.find_element(*self.maintitle_loc)
        print(el.text)
    def click_direct_loc(self):
        self.find_element(*self.direct_loc).click()
    def get_opera_text(self):
        e=self.find_element(*self.opera_text_loc)
        print(e.text)
    def click_opera_large(self):
        self.find_element(*self.opera_large_loc).click()
        print('执行放大操作成功')
    def click_opera_small(self):
        self.find_element(*self.opera_small_loc).click()
        print("执行缩小操作成功")
    def click_focus_loc(self):
        self.find_element(*self.focus_loc).click()
    def click_preset_loc(self):
        self.find_element(*self.preset_loc).click()
    def get_preset_text(self):
        e=self.find_element(*self.preset_text)
        print(e.text)
    def click_preset_sure(self):
        self.find_element(*self.preset_sure).click()
    def click_preset_cancel(self):
        self.find_element(*self.preset_cancel).click()

        