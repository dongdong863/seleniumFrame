from common.ReadConfig import getbrowserinfo
from selenium import webdriver
from common.CapPic import CapPic
import os
def browserstart():
    browsername = getbrowserinfo('browser')
    Url = getbrowserinfo('Url')
    if browsername == 'Chrome':
        driver = webdriver.Chrome()
        driver.get(Url)
    elif browsername == 'Ie':
        driver = webdriver.Ie()
        driver.get(Url)
    CapPic(driver)


