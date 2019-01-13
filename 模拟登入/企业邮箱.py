## --*-- coding=utf-8 --*--
from urllib import request,parse,error
import http.cookiejar as jar
jar_cookie=jar.CookieJar() ## 创建cookie的承载对象
handel=request.HTTPCookieProcessor(jar_cookie) ## 创建一个cookie的handelr
opener=request.build_opener(handel) ## 创建一个opener
url=urlstr="https://qiye.aliyun.com/alimail/ajax/mail/querySessionList.txt?_timestamp_="
header={"User-Agent":"Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36"}
fromdata={
"query":'{"folderIds":["2"]}',
"offset":"0",
"curIncrementId":"0",
# "_csrf_token_":"QXltVG9rZW4tNjI1ODYyMzgtcWFvcVBHQWNSa3dCYXRvMlVmS3FBRUpRc2I3WDRheVVEUlFhTHRPWHlmR3NJd2FLOWg",
# "_root_token_":"dC0xNDgxMDgxLW0zZEVzcw3464",
"_refer_hash_":"h=WyJmbV8yIixbIjIiLCIiLHsiZklkIjoiMiIsInNlbElkIjoiRHp6enp5WHJVTW0tLS0uRGNXNDdFcSIsIm9mZnNldCI6MCwicmciOltbIjIiLHsibWFpbElkIjoiMl8wOkR6enp6eVhyVU1tJC0tLS5EY2V5eUtWIiwiaWQiOiJEenp6enlYclVNbS0tLS5EY1c0N0VxIn1dXX0seyJsYWJlbCI6IumCruS7tiJ9XV0=",
"_tpl_":"DEFAULT"
}
fromdata=parse.urlencode(fromdata).encode()
restr=request.Request(url,headers=header)
respon=opener.open(restr,data=fromdata)
print(respon.read())
print(respon.code)