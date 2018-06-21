'''
Created on 2018年6月19日

@author: admin
'''
from PO import BasePage
from selenium.webdriver.common.by import By
import time
class change_page(object):
    change_one_screen_loc=(By.ID,'com.uniview.app.smb.phone.en.ezview:id/cbOneScreen')
    change_nine_screen_loc=(By.ID,'com.uniview.app.smb.phone.en.ezview:id/alm_ninescreen')
    change_sixteen_screen_loc=(By.ID,'com.uniview.app.smb.phone.en.ezview:id/alm_sixteenscreen')
    change_four_screen_loc=(By.ID,'com.uniview.app.smb.phone.en.ezview:id/alm_fourscreen')
    revoke_video_loc=(By.ID,'com.uniview.app.smb.phone.en.ezview:id/alm_delete')
    def click_change_one_screen_loc(self):
        self.driver.find_element(*self.change_one_screen_loc).click()
        time.sleep(2)
    def click_change_four_screen_loc(self):
        self.driver.find_element(*self.change_four_screen_loc).click()
        time.sleep(2)
    def click_change_nine_screen_loc(self):
        self.driver.find_element(*self.change_nine_screen_loc).click()
        time.sleep(2)
    def click_change_sixteen_screen_loc(self):
        self.driver.find_element(*self.change_sixteen_screen_loc).click()
        time.sleep(2)
    def click_rovoke_video_loc(self):
        for i in range(2):
            self.driver.find_element(*self.revoke_video_loc).click()
            time.sleep(2)
        