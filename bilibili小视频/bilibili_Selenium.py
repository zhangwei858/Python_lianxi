## --*-- coding-utf-8 --*--
from selenium import webdriver
import time
from bs4 import BeautifulSoup as BS
import re

urldtr="http://vc.bilibili.com/p/eden/rank#/?tab=%E5%85%A8%E9%83%A8"
browser=webdriver.Chrome("C:\\Users\\Administrator\\AppData\\Local\\Programs\\Python\\Python36\\Scripts\\chromedriver.exe")
browser.get(urldtr)
time.sleep(3)
for i in range(5):
    browser.execute_script('window.scrollTo(0, document.body.scrollHeight)')
    time.sleep(2)
    print("页面下拉加载第%d 次"%(i+1))

htmlstr=browser.page_source

def Fx_re(htmlstr):
    try:
        htmls=BS(htmlstr,"lxml")
        listitems=htmls.select(".rank-item")
        for listitem in listitems:
            Uname=listitem.select(".video-detail .item-title")[0].string
            timrstr=listitem.select(".video-detail .item-time")[0].string
            Utime=re.findall("\d{4}-\d{2}-\d{2}\s\d{2}:\d{2}:\d{2}",timrstr)[0]

            Uzuozhe=listitem.find(attrs={"class":"host-name"}).string
            Urenshu=listitem.find_all(class_="watch")[0].string
            print("name:%s,,time:%s,,zuozhe:%s,,renshu:%s"%(Uname,Utime,Uzuozhe,Urenshu))
    except Exception as ER:
        print("shu据分析出错:"+ER.args[0])
if __name__=="__main__":
    Fx_re(htmlstr)
    browser.close()