import time
import os
from selenium import webdriver
from common.ReadConfig import getbrowserinfo

def CapPic(driver):
    pt = time.strftime('%Y%m%d%H%M',time.localtime(time.time()))
    picname = os.path.dirname(os.path.abspath('.'))+'/picture/'+pt+'.png'
    driver.get_screenshot_as_file(picname)

