## --*-- coding=utf-8 --*--

import threading
import requests
from bs4 import BeautifulSoup

class Request_url(threading.Thread):
    '''智联大页面获得每个职务的具体连接，放在队列中'''
    def __init__(self,que_html,header,que_urlxihua,name):
        super().__init__()
        self.que_html=que_html
        self.que_xihua=que_urlxihua
        self.header=header
        self.name=name
    def run(self):
        print("{}启动".format(self.name))

class Request_urlxihua(threading.Thread):
    ''' 分析第一层页面的内容，得到每个岗位的具体链接的url放在队列中'''
    def __init__(self,que_html,header,que_urlxihua,name):
        super().__init__()
        self.htmlstr=que_html
        self.header=header
        self.urlxihua=que_urlxihua
        self.name=name
    def run(self):
        print("{}启动".format(self.name))



class Rspon_gw(threading.Thread):
    ''' 爬去并分析每个具体岗位的内容，在放队列中，职务内容和岗位要求分别放在不同队列'''
    def __init__(self,que_urlxihua,que_file,que_coucet,name):
        super().__init__()
        self.urlxihua=que_urlxihua
        self.file=que_file
        self.coucet=que_coucet
        self.name=name
    def run(self):
        print("{}启动".format(self.name))