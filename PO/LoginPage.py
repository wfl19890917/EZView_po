'''
Created on 2018年6月20日

@author: admin
'''
from PO import BasePage
from selenium.webdriver.common.by import By
from appium import webdriver
class Login_page(BasePage.base_page):
    username_loc=(By.ID,'com.uniview.app.smb.phone.en.ezview:id/acaUserName')
    password_loc=(By.ID,'com.uniview.app.smb.phone.en.ezview:id/acaPassWord')
    loginbtn_loc=(By.ID,'com.uniview.app.smb.phone.en.ezview:id/acaLogin')
    tiyan_loc=(By.ID,'com.uniview.app.smb.phone.en.ezview:id/alAvoidLogin')
    def input_username(self,username):
        self.find_element(*self.username_loc).send_keys(username)
    def input_password(self,password):
        self.find_element(*self.password_loc).send_keys(password)
    def click_loginbtn(self):
        self.find_element(*self.loginbtn_loc).click()
    def click_tiyan(self):
        self.find_element(*self.tiyan_loc).click()
def userlogin(self):
    userlogin=Login_page(self.driver)
    userlogin.input_username('18201557582')
    userlogin.input_password('wfl890917')
    userlogin.click_loginbtn()
    print("登录成功")
    
    
    
        