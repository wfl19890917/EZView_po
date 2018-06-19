'''
Created on 2018年6月19日

@author: admin
'''

class MyDriver(object):
    desired_caps={}
    desired_caps['automationName']='Uiautomator2'
    desired_caps['platformName']='Android'
    desired_caps['platformVersion']='6.0.1'
    desired_caps['deviceName']='aeacb854'
    desired_caps['appPackage']='com.uniview.app.smb.phone.en.ezview'
    desired_caps['appActivity']='com.elsw.ezviewer.controller.activity.WelcomeAct'
    desired_caps['unicodeKeyboard']='True'
    desired_caps['resetKeyboard']='True'
    desired_caps['noReset']='true'
        