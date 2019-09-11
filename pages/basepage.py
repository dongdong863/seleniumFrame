#coding:utf-8
#公共类，当多个对象存在共性的时候，就可以把这些共性作为公共类，其他对象继承这样的公共类
# 便于脚本的的维护，减少代码量
# 这个公共类作用是当里面包含了对象想识别的方法，基本操作的方法，提炼出来
from selenium import webdriver

#加载元素隐性显示超时设置函数
from selenium.webdriver.support.wait import WebDriverWait


#导入截图函数
import common.Cappic
#加载预期处理函数
from selenium.webdriver.support import expected_conditions as ec
#导入日志处理函数
from  common.loggen import Logger

import time
import os

logger = Logger(logger = 'Basepage').getlog() #调用Logger类里面的getlog()方法


#定义基础页面类文件，该类包含了查找元素及输入数据两个子函数

class BasePage(object):
    #所有类被调用，都会被执行
    def __init__(self,driver,url):
        self.driver = driver
        self.base_url = url


    #定义查找元素超时设置，当页面某个元素在10内没有显示，则抛出异常，并在日志中记录
    def find_element(self,*loc):
        try:
            #loc是表示属性元组本身，*loc表述属性元组的值，
            #因此，此处只能loc
            WebDriverWait(self.driver,10).until(EC.visibility_of_element_located(loc))
            #此处返回元素的属性值，故使用*loc
            return self.driver.find_element(*loc)
        except:
            #当元素找不到的时候调用截图函数
            Cappic(self.driver)
            #元素找不到时在日志中记录信息
            logger.info(u'%页面未找到 %元素' % (self,loc))

    def send_keys(self,loc,vaule):
        try:
            #获取元素的属性值，以便于识别元素
            loc = getattr(self,'%s'% loc)
            #查找元素并输入相关数据
            self.find_element(*loc.send_keys(vaule))
        except AttributeError:
            #当元素找不到的时候调用截图函数
            Cappic(self.driver)
            #元素找不到时在日志里记录信息
            logger.info(u'%页面未找到 %元素' % (self, loc))


    def click(self,loc):
        try:
            loc =getattr(self,'%s'% loc)
            self.find_element(*loc).click
        except AttributeError:
            Cappic(self.driver)
            # 元素找不到时在日志里记录信息
            logger.info(u'%页面未找到 %元素' % (self, loc))


