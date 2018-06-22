'''
Created on 2018年6月22日

@author: admin
'''
import unittest
from selenium import webdriver
from appium import webdriver
from PO import MenuPage,FavorPage
from Public import driver

class Test(unittest.TestCase):


    def setUp(self):
        self.driver=webdriver.Remote('http://127.0.0.1:4723/wd/hub',driver.MyDriver.desired_caps)

    def tearDown(self):
        self.driver.quit()

    def test_live(self):
        menu=MenuPage.menu_page(self.driver)
        menu.click_menbtn()
        menu.click_favor()
        favor=FavorPage.favor_page(self.driver)
        self.assertEqual('收藏夹',favor.get_favor_title(),msg='验证通过')
        favor.click_more()
        favor.click_live()
    def test_edit(self):
        menu=MenuPage.menu_page(self.driver)
        menu.click_menbtn()
        menu.click_favor()
        favor=FavorPage.favor_page(self.driver)
        self.assertEqual('收藏夹',favor.get_favor_title(),msg='验证通过')
        favor.click_more()
        favor.click_edit()
    def test_rename(self):
        menu=MenuPage.menu_page(self.driver)
        menu.click_menbtn()
        menu.click_favor()
        favor=FavorPage.favor_page(self.driver)
        self.assertEqual('收藏夹',favor.get_favor_title(),msg='验证通过')
        favor.click_more()
        favor.click_rename()
    def test_delete(self):
        menu=MenuPage.menu_page(self.driver)
        menu.click_menbtn()
        menu.click_favor()
        favor=FavorPage.favor_page(self.driver)
        self.assertEqual('收藏夹',favor.get_favor_title(),msg='验证通过')
        favor.click_more()
        favor.click_delete()


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()