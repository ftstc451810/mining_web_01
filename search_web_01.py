from urllib.request import urlopen
from bs4 import BeautifulSoup
from urllib.error import HTTPError
import re
import random
import datetime

def getHtml(url):
    try:
        html = urlopen(url)
    #     网页在伺服器上不存在
    except HTTPError as e:
        print(e)
        # return None
    #   伺服器不存在
    else:
        if html == None:
            print("there's no this server or the site")
            return None
    return html

def getTitle(url):

    try:
        html = getHtml(url)
        bsObj = BeautifulSoup(html.read())
        title = bsObj.body.h1
    except AttributeError as e:
        print(e)
    else:
        if title == None:
            print('there\'s no the tag of body.h1')
            return None
        return title

# 02 了解 findAll()
# html = getHtml("http://www.pythonscraping.com/pages/warandpeace.html")
# bsObj = BeautifulSoup(html)
# nameList = bsObj.findAll("span",{'class':'green'})
# for name in nameList:
#     # get_text() 会把所有标签都清除，只剩中间的text值
#     print(name.get_text())
#
# nameList02 = bsObj.findAll({'h1','h2','h3','h4','h5','h6'})
# nameList03 = bsObj.findAll('span',{'class':{'green','red'}})
# nameList04 = bsObj.findAll(text='prince')
# print(len(nameList04))

# 03子标签、后代标签、兄弟标签 tr:一横列、th:标题栏（tr内的一格）、td:项目栏（tr内的一格）
# html = getHtml('http://www.pythonscraping.com/pages/page3.html')
# bsObj = BeautifulSoup(html)
# vs BeautifulSoup(html.read())

# try:
#     for child in bsObj.find('table',{'id':'giftList'}).tr.children:
#         print(child.get_text())
#     #     get_text()去掉所有标签，仅留文字
# except AttributeError as e:
#     print(e)

# for sibling in bsObj.find('table',{'id':'giftList'}).tr.next_siblings:
#     print(sibling)

# for tr in bsObj.find('table',{'id':'giftList'}).tr:
#     print(tr)
# #     就只抓第一个tr标签而已
# 04wiki

# random.seed(datetime.datetime.now())
# def getLinks(wikiVoc):
#     try:
#         html = getHtml('http://en.wikipedia.org'+wikiVoc)
#         # https可直接改为http
#         bsObj = BeautifulSoup(html,'html.parser')
#         # print('gotten bsObj from'+wikiVoc+': '+datetime.datetime.now()) 文字里放变量要使用%
#         print('gotten bsObj from %s: %s'%(wikiVoc,datetime.datetime.now()))
#         return bsObj.findAll('a', href=re.compile("^(/wiki/)((?!:).)*$"))
#         # 正则表达的括号要放对
#     except:
#         print('something wrong happened')
#
# links = getLinks("/wiki/Mersenne_Twister")
# while len(links) > 0:
#     newVoc = links[random.randint(0, len(links)-1)].attrs['href']
#     print(newVoc)
#     links = getLinks(newVoc)

# 05 搜集站内所有链接，且不重复

pages = set()
def getArtPages(URL):
    html = getHtml('http://www.bnext.com.tw'+URL)
    bsObj = BeautifulSoup(html,'html.parser')
    for link in bsObj.findAll('a',href=re.compile('(/article/)(.)*$')):
        if 'href' in link.attrs:
            if link.attrs['href'] not in pages:
                fullURL = link.attrs['href']
                newURL = re.findall('https://www.bnext.com.tw/article(.)*',fullURL)
                print(newURL[0])
                pages.add(newURL[0])
                getArtPages('/article'+newURL[0])

getArtPages('')
# UnboundLocalError: local variable 'html' referenced before assignment

























