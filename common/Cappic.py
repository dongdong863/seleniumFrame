import time
import os


def Cappic(driver):
    pt = time.strftime('%Y%m%d%H%M',time.localtime(time.time()))
    picname = os.path.dirname(os.path.abspath('.'))+'/picture/'+pt+'.png'
    driver.get_screenshot_as_file(picname)

