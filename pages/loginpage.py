#coding:utf-8

from selenium import webdriver
from pages.basepage import BasePage
from selenium.webdriver.common.by import By
from common.loggen import Logger


logger = Logger('loginPage').getlog()

class LoginPage(BasePage):

