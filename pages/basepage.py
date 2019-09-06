#coding:utf-8
#公共类，当多个对象存在共性的时候，就可以把这些共性作为公共类，其他对象继承这样的公共类
# 便于脚本的的维护，减少代码量
# 这个公共类作用是当里面包含了对象想识别的方法，基本操作的方法，提炼出来
from selenium import webdriver

#加载元素显示超时设置函数
from selenium.webdriver.support.wait import WebDriverWait


#导入截图函数
import common.CapPic
#加载预期处理函数
from selenium.webdriver.support import expected_conditions as ec

import common.logGen






