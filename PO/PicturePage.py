'''
Created on 2018年6月22日

@author: admin
'''
from PO import BasePage
from selenium.webdriver.common.by import By
class picute_page(BasePage.base_page):
    time=(By.ID,'com.uniview.app.smb.phone.en.ezview:id/edit_bar_time')
    picture_loc=(By.ID,'com.uniview.app.smb.phone.en.ezview:id/edit_bar_pic')
    video_loc=(By.ID,'com.uniview.app.smb.phone.en.ezview:id/edit_bar_video')
    edit_loc=(By.ID,'com.uniview.app.smb.phone.en.ezview:id/file_ll_edit_cbox')
    selected_loc=(By.ID,'com.uniview.app.smb.phone.en.ezview:id/file_multiSelect_imgbtn')
    share_loc=(By.ID,'com.uniview.app.smb.phone.en.ezview:id/file_share_imgbtn')
    export_loc=(By.ID,'com.uniview.app.smb.phone.en.ezview:id/file_export_imgbtn')
    delete_loc=(By.ID,'com.uniview.app.smb.phone.en.ezview:id/file_delete_imgbtn')
    ok_loc=(By.ID,'com.uniview.app.smb.phone.en.ezview:id/ok_btn')
    
    
    def click_picture(self):
        self.find_element(*self.picture_loc).click()
    def click_vidoe(self):
        self.find_element(*self.video_loc).click()
    def click_edit(self):
        self.find_element(*self.edit_loc).click()
    def click_selected(self):
        self.find_element(*self.selected_loc).click()
    def click_delete(self):
        self.find_element(*self.delete_loc).click()
    def click_ok_delete(self):
        self.find_element(*self.ok_loc).click()
