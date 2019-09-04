#coding:utf-8
import configparser
import os


def getbrowserinfo(name):

    cf = configparser.ConfigParser()
    cfpath = os.path.dirname(os.path.abspath('.'))+'/config/config.ini'
    print(cfpath)

    cf.read(cfpath)
    browserinfo = cf.get('browser',name)
    return browserinfo

print(getbrowserinfo('BrowserName'))

















