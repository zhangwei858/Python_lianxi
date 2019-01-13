##  --*--coding=utf-8 --*--
import requests
import time
import math
import re
from pyquery import PyQuery as PQ
from bs4 import BeautifulSoup as BS

header={
"User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36"
}

def urlstr(url,yeshu):
    '''动态整理url'''
    urlone="https://bj.lianjia.com/zufang/%s/pg%d/"%(url,yeshu)
    # print(urlone)
    return urlone

def request_html(url,header):
    '''传入网址，获得请求返回的内容'''
    return_html=""
    re_str=requests.get(url,headers=header)
    if re_str.status_code==200:
        return_html=re_str.text
    else:
        print("网页访问不成功，%s"%url)

    return  return_html

def Xiangxixinxi(Concent_insert,url_str):
    '''
    url代表详细一条信息的内容网页，concent是list包括标题和关键词
    :param Concent_insert:
    :param url_str:
    :return:无  应该直接调用 数据库插入（先写入内存，再写数据库）
    '''
    X_mianji=0
    X_huxing=""
    X_louceng=""
    X_chaoyang=""
    X_xiaoqu=""
    X_weizhi=""
    X_ditie=""
    X_shijian=0
    X_jiage=0
    html_str=request_html(url_str,header)
    items_yuan=BS(html_str,"lxml")
    X_jiage=int(items_yuan.find(class_="price").find(attrs={"class":"total"}).string)##价格获取

    items=items_yuan.select(".zf-room p")
    if items:
        try: ##获取面积
            mianji=items[0].get_text()
            mianjire=re.search("(.*?)(\d+\.\d+).*?",mianji,re.M|re.I)
            X_mianji=float(mianjire.group(2))
            # print(X_mianji)
        except Exception as ee:
            print("mianji:"+ee.args[0])

        try:##户型
            huxiang=items[1].get_text()
            hxre=re.search("(.*?)：(.*)",huxiang)
            X_huxing=hxre.group(2)
            # print(X_huxing)
        except Exception as ee:
            print("huxing"+ee.args[0])

        try:##楼层高度
            louceng=items[2].get_text()
            lcre=re.search("(.*?)：(.*)",louceng)
            X_louceng=lcre.group(2)
            # print(X_louceng)
        except Exception:
            print("louceng")

        try:##方向
            chaoyang=items[3].get_text()
            cyre=re.search("(.*?)：(.*)",chaoyang)
            X_chaoyang=cyre.group(2)
        except Exception:
            print("chaoxiang")

        try:##地铁
            ditie=items[4].get_text()
            dtre=re.search("(.*?)：(.*)",ditie)
            X_ditie=dtre.group(2)
        except Exception:
            print("ditie")

        try:##小区
            xiaoqu=items[5].get_text()
            xqre=re.search("(.*?)：(.*)",xiaoqu)
            X_xiaoqu=xqre.group(2)
        except Exception:
            print("xiaoqu")

        try:##地理位置
            weizhi=items[6].get_text()
            wzre=re.search("(.*?)：(.*)",weizhi)
            X_weizhi=wzre.group(2)
        except Exception:
            print("weizhi")

        try:##发布时间
            shijian=items[7].get_text()
            sjre=re.search("(.*?)：(.*)",shijian)
            X_shijian=sjre.group(2)
        except Exception:
            print("shijian")

    Concent_insert+=[X_jiage,X_mianji,X_huxing,X_louceng,X_chaoyang,X_xiaoqu,X_weizhi,X_ditie,X_shijian]
    print(Concent_insert)

def PqFx(htmlstr):
    '''
    主要分析打开的页数页面，获得该页的信息内容和URL连接，然后传入详细分析方法中
    :param htmlstr:
    :return: 信息的条数，主要是给第一次用来计算uan循环次数
    '''
    shuju=30 #给初始值，如果获取失败，该查询只会循环一ye
    py_str=PQ(htmlstr)
    # shuju=int(py_str(".list-head.clear>h2 span").text())
    ####-----------------------------------------------##
    try:
        items=py_str("#house-lst li").items()
        for item in items:
            Concet_insert=[]
            toumu=item(".info-panel>h2 a") ## 连接的网址和表述
            item_url=toumu.attr["href"]
            item_title=toumu.attr("title")

            guanjianci=item(".view-label.left>span").text()
            item_gjc=re.sub(" ","+",guanjianci)

            Concet_insert=[item_title,item_gjc]
            # print(item_url)
            Xiangxixinxi(Concet_insert,item_url)

    except Exception as rr:
        print("网页内容获取失败--PqFx:"+rr.args[0])

    return shuju

def Xunhuanrespon(shuju,input_str):
    ''' 从访问的首页获得，查询结果一共有多少条内容，
    然后算出需要循环de页数，从而循环分析每一页'''
    ye_shu=int(math.ceil(shuju/30.0))
    for i in range(2,ye_shu+1):
        url_str_x=urlstr(input_str,i)
        htmlstr_x=request_html(url_str_x,header)
        if htmlstr_x!="":
            PqFx(htmlstr_x)
        else:
            pass

if __name__=="__main__":
    input_str=input("输入查询的区域：")
    url_str=urlstr(input_str,1)
    htmlstr=request_html(url_str,header)
    if htmlstr!="":
        shuju=PqFx(htmlstr)
        Xunhuanrespon(shuju,input_str)
    else:
        pass