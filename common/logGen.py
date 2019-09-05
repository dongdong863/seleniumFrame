#coding:utf-8
#1、导入python的默认包含的日志模块
import logging
#2、日志写完存放在哪里
import os
#3、日志要记录对应的名称，还是需要time处理
import time
# 先创建一个log对象
# 再创建一个句柄对象，光有log对象没有用，文件输不出来，没有存储的地方

logger = logging.getLogger('LogTestFun')
#设置调试级别：DEbug，info
logger.setLevel(logging.INFO)

#写数据文件，存放地址，写到哪个位置
fileh = logging.FileHandler('路径+名字')
fileh.setLevel(logging.INFO)

#把相对的日志写到里面去
logger.addHandler(fileh)

logger.info('info message')


