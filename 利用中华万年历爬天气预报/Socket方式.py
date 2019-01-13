# --*-- coding=utf-8 --*--
import socket
import time
import json

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect(("wthrcdn.etouch.cn",80))
s.send(b"GET /weather_mini?city=%E5%8C%97%E4%BA%AC&callback=flightHandler&callback=flightHandler&_=1543297479964 HTTP/1.1"
       b"\r\nHost: wthrcdn.etouch.cn\r\nConnection: keep-alive\r\nCookie: __guid=172192485.2102437740110235600.1534411427013.685"
       b"\r\nAccept: */*\r\nUser-Agent: Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36"
       b"\r\n\r\n")
strstr=[]
while True:
    dd=s.recv(1024*1024)
    time.sleep(2)
    if not dd:
        break
    else:
        strstr.append(dd)
s.close()
strs=b"".join(strstr)

header,html=strs.split(b"\r\n\r\n",1)
print(str(html,encoding="utf-8",errors="strict"))
# with open("json.txt","wb") as fo:
#     fo.write(html)

