import requests
from bs4 import BeautifulSoup
# import sys
#
# reload(sys)
# sys.setdefaultencoding('utf-8')

header = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'
}
keyword = {'wd':u'app开发'}

url = 'https://www.baidu.com/s?'
response = requests.get(url, params=keyword, headers=header, timeout=5)
print(response.url)
print(response.status_code)

# 成功抓取整个搜索结果第一页
# fp = open('search2.html','w')
# for line in response.content.decode('utf-8'):
#     fp.write(line)
# fp.close()


# 使用beautifulsoup
soup = BeautifulSoup(response.text)
print(soup.title.text)
print(soup.body.text)

# bs的find_all('')会以标签判断,取得完整标签后［''］抓取某属性的值
for x in soup.find_all('a'):
    print(x['href'])















