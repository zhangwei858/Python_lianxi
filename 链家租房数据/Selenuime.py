## --*-- coding=utf-8 --*--
from selenium import webdriver
from bs4 import BeautifulSoup as BS
import time

urlstr="https://bj.lianjia.com/"
brower=webdriver.Chrome("C:\\Users\\Administrator\\AppData\\Local\\Programs\\Python\\Python36\\Scripts\\chromedriver.exe")
brower.get(urlstr)
time.sleep(5)
Selectstr=brower.find_element_by_css_selector(".tab.check")
print(Selectstr.text)