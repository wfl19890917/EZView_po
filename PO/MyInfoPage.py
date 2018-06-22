'''
Created on 2018年6月21日

@author: admin
'''
from PO import BasePage
from appium import webdriver
from selenium.webdriver.common.by import By
import time
class myinfo_page(BasePage.base_page):
    username_loc=(By.ID,'com.uniview.app.smb.phone.en.ezview:id/acaiUserName')
    edit_username_loc=(By.ID,'com.uniview.app.smb.phone.en.ezview:id/relative2')
    save_loc=(By.ID,'com.uniview.app.smb.phone.en.ezview:id/acu_Determine')
    logoutbtn_loc=(By.ID,'com.uniview.app.smb.phone.en.ezview:id/acaiSwitchAccount')
    open_historyaccount=(By.ID,'com.uniview.app.smb.phone.en.ezview:id/choice_account_cb')
    delete_account=(By.ID,'com.uniview.app.smb.phone.en.ezview:id/delete_account_iv')
    delete_sure=(By.NAME,'确认')
    
    def edit_username(self,name):
        self.find_element(*self.username_loc).click()
        self.find_element(*self.edit_username_loc).send_keys(name)
        self.find_element(*self.save_loc).click()
        time.sleep(2)
        print("保存成功")
    def get_edit_username(self):
        return self.find_element(*self.username_loc).text
    def click_logoutbtn(self):
        self.find_element(*self.logoutbtn_loc).click()
    def click_open_history(self):
        self.find_element(*self.open_historyaccount).click()
    def click_delete_account(self):
        self.find_element(*self.delete_account).click()
    def click_delete_sure(self):
        self.find_element(*self.delete_sure).click()
        print("删除用户名成功")
def userLogout(self):
    userlogout=myinfo_page(self.driver)
    userlogout.click_logoutbtn()
    userlogout.click_open_history()
    userlogout.click_delete_account()
    userlogout.click_delete_sure()
    
   
        
    
    
    
    
    
        