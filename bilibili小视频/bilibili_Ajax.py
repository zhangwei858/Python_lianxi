## --*-- coding=utf-8 --*--

import requests
from bs4 import BeautifulSoup
import json

urlstr="http://api.vc.bilibili.com/board/v1/ranking/top?"
headerstr={
"Accept":"application/json, text/plain, */*",
"Host":"api.vc.bilibili.com",
"Origin":"http://vc.bilibili.com",
"Referer":"http://vc.bilibili.com/p/eden/rank",
"User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36"
}

def paramsstr(count):
    params={
    "page_size":"10",
    "next_offset":count,
    "tag":"今日热门",
    "platform":"pc"
    }
    return params

def Ajax_re(urlstr,params,headerstr):
    jsonstr={}
    re_str=requests.get(url=urlstr,params=params,headers=headerstr)
    if re_str.status_code==200:
        jsonstr=re_str.json()
    else:
        print("网页链接失败")

    return jsonstr

def Fx_response(jsonstr):
    itemstrs=jsonstr["data"]["items"]
    for itemstr in itemstrs:
        name=itemstr["item"]["description"]
        ftime=itemstr["item"]["upload_time"]
        renshu=itemstr["item"]["watched_num"]
        urlstr=itemstr["item"]["video_playurl"]
        leixing=itemstr["item"]["tags"][0]
        zuozhe=itemstr["user"]["name"]

        print("name:%s,time:%s,renshu:%d,leixing:%s,zhuzhe:%s,url:%s"%(name,ftime,renshu,leixing,zuozhe,urlstr))

if __name__=="__main__":
    params={}
    for i in range(0,2):
        params=paramsstr((i*10+1))
        jsonstr=Ajax_re(urlstr,params,headerstr)
        Fx_response(jsonstr)

