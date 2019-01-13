## --*-- coding=utf-8 --*--
from urllib import request,error,parse
import http.cookiejar as jar
header={"User-Agent":"Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36"}
'''
url="http://www.renren.com/969250449/profile?v=info_timeline"
header={
    "User-Agent":"Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36",
    'Cookie':'_r01_=1; anonymid=jq4jqdwlj8yd6x; depovince=BJ; ick_login=4822769b-df03-46de-9270-1e430731d5d8; ch_id=10016; ick=8c62e902-6a96-4250-bd26-a4342e511582; XNESSESSIONID=79b6169125dc; first_login_flag=1; ln_uact=18518572578; ln_hurl=http://head.xiaonei.com/photos/0/0/men_main.gif; jebe_key=b54c15fb-bdb5-41dc-b641-50e59f775f73%7C02ca2cb2f436573047138d347743c5eb%7C1545820706368%7C1%7C1545820716374; wp_fold=0; jebecookies=1b6b473b-65c5-492f-96db-e84ab6955f41|||||; _de=9EBEC0D052EB3CB0BE4D59FB3CFDBA3A; p=1db754355112118da59ac208a910109e2; t=5afe3c9577089f80d050033528aaf20d2; societyguester=5afe3c9577089f80d050033528aaf20d2; id=969250852; xnsid=15c0b1e3; ver=7.0; loginfrom=null'
} ## 再请求头里面带有cookie

reques=request.Request(url,headers=header)
requ=request.urlopen(reques)
with open("C:\\Users\\Administrator\Desktop\\renren.html","wb") as fo:
    fo.write(requ.read())

''' ## 再请求头里面带有cookie

#
url1="https://www.renren.com/969250852/newsfeed/specialfocus"
url2="http://www.renren.com/getFeedOptions"
formdata={
"devid":"46a9a729705a54a0c1071d0005198a58",
"devtype":"se",
"metatype":"1",
"method":"Meta.upload",
"qid":"3069526447",
"rtick":"84210",
"v":"10.0.1581.0",
"is_encrypt":"1",
"is_compress":"0",
"meta_count":"12",
"orgsize":"1614",
"sign":"b1ee4b5e4bc731d80fe32ee08b5f487a"
}
formdata=parse.urlencode(formdata).encode()
cj=jar.CookieJar()
handler=request.HTTPCookieProcessor(cj)
opener=request.build_opener(handler)
reques=request.Request(url2,headers=header)
requ2=opener.open(reques,data=formdata)
print(requ2.getheaders())
#
requ1=request.Request(url1,headers=header)
requ=opener.open(requ1)
#
with open("C:\\Users\\Administrator\Desktop\\renren.html","wb") as fo:
    fo.write(requ.read())

