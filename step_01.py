import urllib.request
import urllib.parse

# 01
# response = urllib.request.urlopen("http://www.baidu.com").read()
# print(response)

# 02
# dic = {'username':'18850317583','password':'8104515093zcs'}
# data = urllib.parse.urlencode(dic).encode('UTF-8')
# url = 'https://passport.csdn.net/account/login?from=http://my.csdn.net/my/mycsdn'
# response = urllib.request.urlopen(url, data)
# print(response.read().decode('UTF-8'))

# 04
enable_proxy = True
proxy_handler = urllib.request.ProxyHandler({'http':'http://some-proxy.com:8080'})
null_proxy_handler = urllib.request.ProxyHandler({})
if enable_proxy:
    opener = urllib.request.build_opener(proxy_handler)
else:
    opener = urllib.request.build_opener(null_proxy_handler)
urllib.request.install_opener(opener)

# # 03、05
url = "https://passport.csdn.net/account/login?from=http://my.csdn.net/my/mycsdn"
values = {'username':'18850317583','password':'8104515093zcs'}
headers = {'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    # 'Accept-Encoding':'gzip, deflate, sdch, br',
    'Accept-Language':'zh-TW,zh;q=0.8,en-US;q=0.6,en;q=0.4,zh-CN;q=0.2',
    'Connection':'keep-alive',
    'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36',
    'Referer': 'http://www.zhihu.com/articles'}
data = urllib.parse.urlencode(values).encode('utf-8')
request = urllib.request.Request(url,data,headers)
try:
    response = urllib.request.urlopen(request)
except urllib.request.HTTPError as e:
    print(e.code)
except urllib.request.URLError as e:
    print(e.reason)
else:
    print('OK')
# response = urllib.request.urlopen(request, timeout=10) 如中间含data就不用声明，直接接着打10即可
print(response.read().decode('utf-8'))











