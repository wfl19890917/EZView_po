'''
Created on 2018年6月21日

@author: admin
'''
from PO import BasePage
from appium import webdriver
from selenium.webdriver.common.by import By
class menu_page(BasePage.base_page):
    menbtn_loc=(By.ID,'com.uniview.app.smb.phone.en.ezview:id/mainBtnMenu')
    curname_loc=(By.ID,'com.uniview.app.smb.phone.en.ezview:id/account_user_name')
    shikuang_loc=(By.XPATH,'//android.widget.TextView[@text="实　　况"]')
    shikuang_title_loc=(By.ID,'com.uniview.app.smb.phone.en.ezview:id/main_title')
    replay_loc=(By.XPATH,"//android.widget.TextView[@text='回　　放']")
    replay_title_loc=(By.ID,'com.uniview.app.smb.phone.en.ezview:id/textView1')
    device_loc=(By.XPATH,"//android.widget.TextView[@text='设备管理']")
    picture_loc=(By.XPATH,"//android.widget.TextView[@text='图像管理']")
    favorte_loc=(By.XPATH,"//android.widget.TextView[@text='收  藏  夹']")
    notice_loc=(By.XPATH,"//android.widget.TextView[@text='告警通知']")
    configure_loc=(By.XPATH,"//android.widget.TextView[@text='配　　置']")
    help_loc=(By.XPATH,"//android.widget.TextView[@text='帮　　助']")
    rentou_loc=(By.ID,'com.uniview.app.smb.phone.en.ezview:id/menu_rentou')
    def click_rentou(self):
        self.find_element(*self.rentou_loc).click()
    def click_menbtn(self):
        self.find_element(*self.menbtn_loc).click()
    def get_currentname(self):
        return self.find_element(*self.curname_loc).text
    def click_shikuang(self):
        self.find_element(*self.shikuang_loc).click()
    def get_shikuang_title(self):
        return self.find_element(*self.shikuang_title_loc).text
    def click_replay(self):
        self.find_element(*self.replay_loc).click()
    def get_replay_title(self):
        return self.find_element(*self.replay_title_loc).text
    def click_device(self):
        self.find_element(*self.device_loc).click()
    def click_picture(self):
        self.find_element(*self.picture_loc).click()
    def click_favor(self):
        self.find_element(*self.favorte_loc).click()
    def click_notice(self):
        self.find_element(*self.notice_loc).click()
    def click_configure(self):
        self.find_element(*self.configure_loc).click()
    def click_help(self):
        self.find_element(*self.help_loc).click()

        
    
    
    
        
        
    
        