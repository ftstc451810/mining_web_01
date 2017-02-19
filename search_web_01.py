from urllib.request import urlopen
from bs4 import BeautifulSoup
from urllib.error import HTTPError


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

html = getHtml("http://www.pythonscraping.com/pages/warandpeace.html")
bsObj = BeautifulSoup(html.read())
nameList = bsObj.findAll("span",{'class':'green'})
for name in nameList:
    # get_text() 会把所有标签都清除，只剩中间的text值
    print(name.get_text())

nameList02 = bsObj.findAll({'h1','h2','h3','h4','h5','h6'})
nameList03 = bsObj.findAll('span',{'class':{'green','red'}})
nameList04 = bsObj.findAll(text='prince')
print(len(nameList04))


