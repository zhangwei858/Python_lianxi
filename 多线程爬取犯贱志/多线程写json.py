##  --*-- coding=utf-8 --*--
import threading
import requests
import time
from queue import Queue
from bs4 import BeautifulSoup as BS
import json
import os

def main(urlqueue,filequeue,writequeue):
    header={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36"}
    L=threading.Lock()

    reque1=Request_th(header,urlqueue,filequeue,"reque1")
    reque2=Request_th(header,urlqueue,filequeue,"reque2")
    reque3=Request_th(header,urlqueue,filequeue,"reque3")

    resop1=Resoper_th(filequeue,"resop1",writequeue)
    resop2=Resoper_th(filequeue,"resop2",writequeue)
    resop3=Resoper_th(filequeue,"resop3",writequeue)

    write1=Write_th("C:\\Users\\Administrator\\Desktop\\读写\\ff.txt",writequeue,L,"write1")
    write2=Write_th("C:\\Users\\Administrator\\Desktop\\读写\\ff.txt",writequeue,L,"write2")
    write3=Write_th("C:\\Users\\Administrator\\Desktop\\读写\\ff.txt",writequeue,L,"write3")

    # region ##start()
    reque1.start()
    reque2.start()
    reque3.start()
    # time.sleep(2)############
    resop1.start()
    resop2.start()
    resop3.start()
    # time.sleep(2)#############
    write1.start()
    write2.start()
    write3.start()
    # endregion
    reque1.join()
    reque2.join()
    reque3.join()
    resop1.join()
    resop2.join()
    resop3.join()
    write1.join()
    write2.join()
    write3.join()


class Request_th(threading.Thread):
    def __init__(self,header,urlqueue,filequeue,name):
        super().__init__()
        self.urlqueue=urlqueue
        self.filequeue=filequeue
        self.name=name
        self.header=header
    def run(self):
        print("%s---线程启动"%self.name)
        while self.urlqueue.qsize()>0:
            try:
                url=self.urlqueue.get(False)
                req_str=requests.get(url,headers=self.header)
                if req_str.status_code==200:
                    filetext=req_str.text
                    self.filequeue.put(filetext)
                    # print("+++"+str(self.filequeue.qsize()))
                    # print(filetext)
            except Exception as ee:
                print("{}--线程异常结束".format(self.name))
                break
        print("{}--线程结束".format(self.name))

class Resoper_th(threading.Thread):
    def __init__(self,filequeue,name,writeque):
        super().__init__()
        self.name=name
        self.fileque=filequeue
        self.write=writeque

    def run(self):
        print("%s线程启动"%self.name)
        while True:
            try:
                # print("--"+str(self.fileque.qsize()))
                filetext=self.fileque.get(True,timeout=10)
                # print("12")
                Textstr=BS(filetext,"lxml")
                lists=Textstr.select(".cont-list .cont-item")
                for list in lists:
                    title=list.select(".cont-list-editor")[0].string
                    concet=list.select(".cont-list-title")[0].string
                    writejson={"tile":title,"concet":concet}
                    jsonstr=json.dumps(writejson,ensure_ascii=False,indent=2)
                    self.write.put(jsonstr) ## 添加

            except Exception as ee:
                print("%s线程结束"%self.name)
                break
        # print(self.fileque.qsize())

class Write_th(threading.Thread):
    def __init__(self,pathstr,writeque,lock,name):
        super().__init__()
        self.pathstr=pathstr
        self.writeque=writeque
        self.lock=lock
        self.name=name
    def run(self):
        print("%s----线程启动"%self.name)
        while True:
            try:
                self.lock.acquire()
                filestr=self.writeque.get(True,10)
                with open(self.pathstr,"a+",encoding="utf-8") as fofile:
                    fofile.write(filestr)
            except Exception as ee:
                print("{0}---线程结束".format(self.name))
                break
            finally:
                self.lock.release()

if __name__ == '__main__':
    timestart=time.time()
    url_start="http://www.fanjian.net/jiantu-{0}"
    qstr_url=Queue(500)
    qstr_file=Queue(5000)
    qstr_jsonfo=Queue(5000)
    for i in range(1,499):
        urlend=url_start.format(i)
        qstr_url.put(urlend)

    main(qstr_url,qstr_file,qstr_jsonfo)

    timeend=time.time()
    print("总消耗时间：{}".format(timeend-timestart))