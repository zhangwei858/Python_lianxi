## --*-- coding=utf-8 --*--
import json
import time
import os
import pymongo
import threading

class WriteMongo(threading.Thread):
    '''岗位描述，写入mongodb'''
    def __init__(self,que_coucet,name):
        super().__init__()
        self.coucet=que_coucet
        self.name=name
    def run(self):
        print("{}启动".format(self.name))

class WriteFile(threading.Thread):
    '''岗位描述和要求'''
    def __init__(self,que_coucet,name):
        super().__init__()
        self.coucet=que_coucet
        self.name=name
    def run(self):
        print("{}启动".format(self.name))