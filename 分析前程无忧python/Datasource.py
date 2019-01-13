## --*-- coding=utf-8 --*--
import pymysql
import os
import time

class Text_cunchu:
    '''  对txt 存储 ，传入文件夹路径和文件名，内容'''

    Os_str="公司职务简介"
    def __init__(self,pathstr):
        self.OS_path=os.path.join(pathstr,self.Os_str)
        self.__OS_Create()
    def __OS_Create(self):
        if os.path.exists(self.OS_path):
            pass
        else:
            os.makedirs(self.OS_path)
    def Test_create(self,coucet,txtname):
        try:
            Text_str=os.path.join(self.OS_path,txtname+".txt")
            with open(Text_str,"w+") as fo:
                fo.write(coucet)
        except Exception as fo:
            pass

class Mysqldata:

    __create_database=" create database if not exists %s "
    __drop_database=" drop database if exists %s"
    __use_database=" use %s"
    __create_table_gangwei='''
    create table if not EXISTS  GangWei
    (
      ID int PRIMARY key auto_increment not NULL ,
      Zgangzhao VARCHAR(150) not null DEFAULT 'Python',
      Zgongzi VARCHAR (100) not null DEFAULT '面谈',
      Zdidian VARCHAR(150) not null DEFAULT '未知',
      Zjingyan VARCHAR(120) not null DEFAULT '无要求',
      Zxueli VARCHAR(80) not null DEFAULT '无要求',
      Zrenshu VARCHAR(80) not null DEFAULT '暂不定',
      Zdaiyu VARCHAR(200) not null DEFAULT '面议',
      Zgongsi VARCHAR(180) not null DEFAULT '未知'
    )engine=InnoDB charset=utf8
    '''
    __insert_table_gangwei='''insert into GangWei(Zgangzhao,Zgongzi,Zdidian,Zjingyan,Zxueli,Zrenshu,Zdaiyu,Zgongsi)VALUES ("%s","%s","%s","%s","%s","%s","%s","%s")'''
    __create_table_gongsi='''
    create table if not  EXISTS Gongsi
      (
      ID int PRIMARY key auto_increment not NULL,
      Gname VARCHAR(150) not null  DEFAULT '未知',
      Ghangye VARCHAR(180) not null DEFAULT '未知',
      Gguim VARCHAR(150) not null DEFAULT '未知',
      Gxingzhi VARCHAR(150) not null DEFAULT '未知',
      Gyaoqiu VARCHAR(200) not null DEFAULT '暂无'
      )engine=INNODB charset=utf8
    '''
    __insert_table_gongsi='''
    insert into Gongsi(Gname,Ghangye,Gguim,Gxingzhi,Gyaoqiu)VALUES("%s","%s","%s","%s","%s")
    '''

    __drop_table_gangwei="drop table if EXISTS GangWei"
    __drop_table_gongzi="drop table if EXISTS GongSi"


    def __init__(self,databsename):
        self.__create_database=self.__create_database%databsename
        self.__drop_database=self.__drop_database%databsename
        self.__use_database=self.__use_database%databsename
        self.__db=pymysql.connect(host="localhost",user="root",password="zw123",port=3306)
        self.__cursor=self.__db.cursor()
        self.__Cdatabase() ##创建项目库
        self.__Udatabase() ##移动指针到指定数据库
        self.__Ctable_gangwei() ##创建岗位库
        self.__Ctable_gongsi() ##创建公司库

    def __Cdatabase(self):
        '''默认不被外面使用,自动实例对象时候调用'''
        self.__cursor.execute(self.__create_database)
        self.__db.commit()
    def _Ddatabase(self):
        ''' 默认不被外面使用'''
        self.__cursor.execute(self.__drop_database)
        self.__db.commit()
    def __Udatabase(self):
        '''默认不被外面使用,自动实例对象时候调用'''
        self.__cursor.execute(self.__use_database)
        self.__db.commit()
    def __Ctable_gangwei(self):
        '''默认不被外面使用,自动实例对象时候调用'''
        self.__cursor.execute(self.__create_table_gangwei)
        self.__db.commit()
    def __Ctable_gongsi(self):
        '''默认不被外面使用,自动实例对象时候调用'''
        self.__cursor.execute(self.__create_table_gongsi)
        self.__db.commit()
    def _Dtable_gangwei(self):
        '''默认不被外面使用'''
        self.__cursor.execute(self.__drop_table_gangwei)
        self.__db.commit()
    def _Dtable_gongsi(self):
        '''默认不被外面使用'''
        self.__cursor.execute(self.__drop_table_gongzi)
        self.__db.commit()
    def Insert_gangwei(self,coucet):
        sql=self.__insert_table_gangwei%coucet
        # print(sql)
        self.__cursor.execute(sql)
        self.__db.commit()
    def Insert_gongsi(self,coucet):
        sql=self.__insert_table_gongsi%coucet
        self.__cursor.execute(sql)
        self.__db.commit()
    def __del__(self):
        self.__db.close()

if __name__=="__main__":
    textfile=Text_cunchu("C:\\Users\\Administrator\\Desktop")
    textfile.Test_create("123","rrr")
    # mysql_str=Mysqldata("智联招聘")
    # mysql_str.Insert_gangwei(("12","34","45","67","89","10","13","14"))