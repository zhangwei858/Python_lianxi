## --*-- coding=utf-8 --*--
import requests
import json

url="http://wthrcdn.etouch.cn/weather_mini?"
pasrt={
    "city":"北京",
"callback":"flightHandler",
"callback":"flightHandler",
"_":"1543324611059"
}
header={
    "Host":"wthrcdn.etouch.cn",""
"Referer":"http://yun.rili.cn/wnl/index.html",
"User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36"
}

restr=requests.get(url,headers=header,params=pasrt)
if restr.status_code==200:
    jsonstr=restr.text;

else:
    print("not ok ")
print(jsonstr)