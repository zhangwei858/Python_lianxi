## --*-- coding=utf-8 --*--
from urllib import request,error,parse
import time

def main(kw,page):
    urlstr=url_get(page=page,kw=kw)
    data_re_write(urlstr=urlstr,page=page)
    time.sleep(5)

def url_get(page,kw):
    "拼接完成url"
    url="http://tieba.baidu.com/f?"
    pasestr={
        "kw":kw,
        "ie":"utf-8",
        "pn":page
    }
    url=url+parse.urlencode(pasestr)
    print(url)
    return url

def data_re_write(urlstr,page):
    header={
        "User-Agent":"Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36"
    }

    restr=request.Request(urlstr,headers=header)
    respon=request.urlopen(restr)
    strhtml=respon.read()
    # print(strhtml.decode("utf-8"))

    pathstr="C:\\Users\\Administrator\\Desktop\\"+str(page)+".html"
    with open(pathstr,"wb") as fofile:
        fofile.write(strhtml)

if __name__ == '__main__':
    main("python",0)