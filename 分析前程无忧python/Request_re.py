## --*-- coding=utf-8 --*--
import requests
from bs4 import BeautifulSoup as BS
import re
import time
import Datasource


headerstr={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36"
    }

def  url(urlcoucet):
    '''
    :param 动态页数参数:
    :return:返回完整url
    '''
    urlstr="https://search.51job.com/list/010000%252C020000%252C030200,000000,0000,00,9,99,Python,2,"+str(urlcoucet)+".html?" \
           "lang=c&stype=1&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&" \
           "companysize=99&lonlat=0%2C0&radius=-1&ord_field=0&confirmdate=9" \
           "&fromType=&dibiaoid=0&address=&line=&specialarea=00&from=&welfare=1"

    return urlstr

def Re_request(urlstr,header):
    '''传入url 返回html'''
    htmlstr=requests.get(urlstr,headers=header)
    if htmlstr.status_code==200:
        return htmlstr.text

    else :
        print("wu")

def Get_itemurl(htmls):
    ''' 先进入筛选页,然后获得每个招聘项跳转链接'''
    textfile=Datasource.Text_cunchu("C:\\Users\\Administrator\\Desktop")
    mysql_str=Datasource.Mysqldata("智联招聘")
    result=BS(htmls,"lxml")
    resultLists=result.find(attrs={"class":"dw_table","id":"resultList"})
    resultList=resultLists.select(".el")
    for resultitem in resultList:
        urlqs=resultitem.select(".t1 a")
        if urlqs!=[]:
            urlq=urlqs[0].attrs["href"]
            Get_coucet(urlq,mysql_str,textfile)


def Get_coucet(urlcoucet,mysql_str,textfile):
    '''
    1,先判断得到跳转链接是否可用
    2,先获得岗位的信息
    3,再获得职务简介和公司信息，计划职务简介存放在txt里面
    '''
    rebool=re.match('''https://jobs.51job.com/\w+(-\w+)*/\d+.*''',urlcoucet,re.M|re.I)
    if rebool==None:
        print("不能正常分析网页:%s"%urlcoucet)
    else:
        htmlcount=Re_request(urlcoucet,header=headerstr)
        try:
            html_re=BS(htmlcount,"lxml")
        except Exception as ee:
            pass
        ###----------------------------------------职务信息-----------------------
        Zhiwuitmes=html_re.select(".tHeader.tHjob .in .cn")
        if Zhiwuitmes!=[]:
            Zhi_Gangzhao=Zhiwuitmes[0].find("h1").attrs["title"]
            Zhi_Gongzi=Zhiwuitmes[0].find("strong").string
            Zhi_gongsi=Zhiwuitmes[0].find(class_="cname").a.attrs["title"]

            Zhi_zong=Zhiwuitmes[0].select(".msg.ltype")[0].attrs["title"]
            zonglist=re.split("\|",Zhi_zong)
            Zhi_diqu=zonglist[0].strip()
            Zhi_jingyan=zonglist[1].strip()
            if len(zonglist)>=5:
                Zhi_xueli=zonglist[2].strip()
                Zhi_renshu=zonglist[3].strip()
            else:
                Zhi_xueli=""
                Zhi_renshu=""

            Zhi_daiyulist=Zhiwuitmes[0].select(".jtag .t1")[0]
            listdai=Zhi_daiyulist.find_all(class_="sp4")
            if listdai !=[]:
                Zhi_daiyu=listdai[0].string
                if len(listdai)>3:
                    for lis in listdai[1:]:
                        Zhi_daiyu=Zhi_daiyu+"+"+lis.string
            else:
                Zhi_daiyu=""

            ##写入岗位相关数据库
            try:
                Zhiwei=(Zhi_Gangzhao,Zhi_Gongzi,Zhi_diqu,Zhi_jingyan,Zhi_xueli,Zhi_renshu,Zhi_daiyu,Zhi_gongsi)
            except Exception as ee:
                pass
            # return Zhiwei
        ############################################################################

        ###----------------------------------------公司信息-----------------------
        zhizelist=html_re.select(".tCompany_main .bmsg.job_msg.inbox")
        if zhizelist !=[]:
            zhize=zhizelist[0].find_all("p")
            Gongsi_zhize=zhize[0].string
            if Gongsi_zhize!=None:
                for zzzz in zhize[1:]:
                    try:
                        Gongsi_zhize=Gongsi_zhize+zzzz.string+"\n"
                    except Exception as fo:
                        pass
            else:
                Gongsi_zhize="huo qu shi bai"

            textfile.Test_create(Gongsi_zhize,Zhi_gongsi)

        xinxis=html_re.select(".tCompany_sidebar .tBorderTop_box .com_tag")
        if xinxis!=[]:
            xinxi=xinxis[0].find_all(attrs={"class":"at"})
            Gongsi_xingzhi=xinxi[0].attrs["title"]
            Gongsi_renshu=xinxi[1].attrs["title"]
            Gongsi_leixing=xinxi[2].attrs["title"]

        Gongsi_zhize_path=Zhi_gongsi+".txt"
        Gongsi=(Zhi_gongsi,Gongsi_leixing,Gongsi_renshu,Gongsi_xingzhi,Gongsi_zhize_path)

        mysql_str.Insert_gangwei(Zhiwei)
        mysql_str.Insert_gongsi(Gongsi)



        ############################################################################


if __name__=="__main__":
    for i in range(1,325):
        urlstr=url(i)
        htmls=Re_request(urlstr,headerstr)
        Get_itemurl(htmls)

