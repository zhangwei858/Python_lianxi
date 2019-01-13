## --*-- coding=utf-8 --*--
from queue import Queue
import time
from CunChuandFenXi.Fenxi import Request_url,Request_urlxihua,Rspon_gw
from CunChuandFenXi.CunChu import WriteMongo,WriteFile


def main(que_url,que_html,que_urlxihua,que_coucet,que_file):
    '''启动各种线程'''
    header={ "User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36"}

    Start_re(que_url,header,que_html)
    Start_re_xihua(que_html,header,que_urlxihua)
    Start_fx(que_urlxihua,que_file,que_coucet)
    Start_monge(que_coucet)
    Start_file(que_file)

def Start_re(que_url,header,que_html):
    ''' 爬取第一层页面，返回html放在队列中，同时使用3个线程工作'''
    ReSy=["ReSy1","ReSy2","ReSy3"]
    for i in ReSy:
        RS=Request_url(que_html,header,que_urlxihua,i)
        RS.start()
        RS.join()

def Start_re_xihua(que_html,header,que_urlxihua):
    ''' 分析第一层页面的内容，得到每个岗位的具体链接的url放在队列中，同时使用3个线程工作'''
    ReXh=["ReXh1","ReXh2","ReXh3"]
    for i in ReXh:
        Re=Request_urlxihua(que_html,header,que_urlxihua,i)
        Re.start()
        Re.join()

def Start_fx(que_urlxihua,que_file,que_coucet):
    ''' 爬去并分析每个具体岗位的内容，在放队列中，职务内容和岗位要求分别放在不同队列,同时使用3个线程工作'''
    Rgw=["RGW1","RGW2","RGW3"]
    for i in Rgw:
        Rsn=Rspon_gw(que_urlxihua,que_file,que_coucet,i)
        Rsn.start()
        Rsn.join()

def Start_monge(que_coucet):
    '''岗位描述，写入mongodb，同时使用3个线程工作'''
    mongos=["mongo1","mongo2","mongo3"]
    for i in mongos:
        wm=WriteMongo(que_coucet,i)
        wm.start()
        wm.join()

def Start_file(que_file):
    '''岗位描述和要求，同时使用3个线程工作'''
    files=["file1","file2","file3"]
    for i in files:
        fe=WriteFile(que_coucet,i)
        fe.start()
        fe.join()

if __name__ == '__main__':
    que_url=Queue(500)   ## 加载所有url
    que_html=Queue(500)## 获得每个具体页面内容
    que_urlxihua=Queue(5000)## 获得每一个职务连接url
    que_coucet=Queue(5000)
    que_file=Queue(5000)

    # urlstr="https://sou.zhaopin.com/?p={}&jl=530&kw=Python&kt=3"
    # for i in range(1,10):
    #     url=urlstr.format(i)
    #     que_url.put(url)

    main(que_url,que_html,que_urlxihua,que_coucet,que_file)
