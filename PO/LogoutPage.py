'''
Created on 2018年6月20日

@author: admin
'''
from PO import BasePage
from selenium.webdriver.common.by import By
class logout_page(BasePage.base_page):
    logoutbtn_loc=(By.ID,'com.uniview.app.smb.phone.en.ezview:id/acaiSwitchAccount')
    open_historyaccount=(By.ID,'com.uniview.app.smb.phone.en.ezview:id/choice_account_cb')
    delete_account=(By.ID,'com.uniview.app.smb.phone.en.ezview:id/delete_account_iv')
    delete_sure=(By.NAME,'确认')
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
    userlogout=logout_page(self.driver)
    userlogout.click_logoutbtn()
    userlogout.click_open_history()
    userlogout.click_delete_account()
    userlogout.click_delete_sure()

        