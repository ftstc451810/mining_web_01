import urllib.request
import urllib.parse
import http.cookiejar
url="https://www.baidu.com/"
# cookie, proxy：代理避免一直用同个IP
cj = http.cookiejar.CookieJar()
cp = urllib.request.HTTPCookieProcessor(cj)
proxy_handler = urllib.request.ProxyHandler({'http':'http://some-proxy.com:8080'})
opener = urllib.request.build_opener(cp, proxy_handler)
urllib.request.install_opener(opener)

# header防反爬，假装为浏览器:useragent
header = {
    'Accept':'text/javascript, application/javascript, application/ecmascript, application/x-ecmascript, */*; q=0.01',
    'Accept-Language':'zh-TW,zh;q=0.8,en-US;q=0.6,en;q=0.4,zh-CN;q=0.2',
    'Connection':'keep-alive',
    # 'Cookie':'BAIDUID=5636D0F4D036A82652D033ED6DCB760E:FG=1; BIDUPSID=5636D0F4D036A82652D033ED6DCB760E; PSTM=1487295556; H_PS_645EC=30baHVr8oCcLbrejr%2FzdBAULv7xMAg4jt18VRYDtY7e5JNq99NNub9QA66I; BD_CK_SAM=1; PSINO=7; BD_HOME=0; H_PS_PSSID=1443_21080_22035_20929; __bsi=16127913276913910055_00_0_I_R_3_0303_C02F_N_I_I_0; BD_UPN=123253',
    'Host':'www.baidu.com',
    'Referer':'https://www.baidu.com/',
    'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'
}

keyword="app开发"
bind_kw= urllib.parse.urlencode(keyword).encode('UTF-8')
request = urllib.request.urlopen(url, bind_kw, header)
response = request.read().decode('UTF-8')
print(response)

# 失败一直无法成功搜寻，改用request库