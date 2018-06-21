'''
Created on 2018年6月19日

@author: admin
'''
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from appium import webdriver
class base_page(object):
    def __init__(self, driver):
        self.driver=driver
    def find_element(self,*loc):
        try:
            WebDriverWait(self.driver,10).until(EC.visibility_of_element_located(loc))
            f=self.driver.find_element(*loc)
            return f
        except Exception as e:
            print('%s页面未找到元素%s'%(self.driver,loc))
    def find_elements(self,*loc):
        try:
            WebDriverWait(self.driver,10).until(EC.visibility_of_all_elements_located(loc))
            f=self.driver.find_elements(*loc)
            return f
        except Exception as e:
            raise e
    #重写元素定位的方法
    def find_elemente(self,loc):
        try:
            return self.driver.find_element_by_id(loc)
        except Exception as e:
            print("未找到%s"%(self,loc))
        
            
    
        