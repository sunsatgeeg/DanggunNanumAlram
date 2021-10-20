import time
import urllib.request
from bs4 import BeautifulSoup
from pygame import mixer
import threading
#Danggn Nanum Alram

# 찾고싶은 조건
placeList = ['경기도 김포시 풍무동', '경기도 김포시 사우동']
subfind = ['sm7b', '라즈베리파이4']

oldtime = ''
subfindCon = []
for i in subfind:
    subfindCon.append(i.casefold().replace(" ", ""))  # 대문자 > 소문자로 변환

mixer.init()
m1 = mixer.Sound('sound1.mp3')
m2 = mixer.Sound('sound2.mp3')



def alram1():
    m1.set_volume(1)
    m1.play()

def alram2():
    m2.set_volume(1)
    m2.play()

def txtread():
    with open("number.txt", "r", encoding="UTF-8") as f:
        number = f.readlines()[-1]

    with open("number.txt", "w", encoding="UTF-8") as fa:
        fa.write('')

    return number

def url_open(number):
    try:
        url = 'https://www.daangn.com/articles/%s' % number
        html = urllib.request.urlopen(url)
        soup = BeautifulSoup(html, 'html.parser')
    except urllib.error.HTTPError:
        errorPrint = str(number)+' 삭제된 게시물\n'
        print(errorPrint, end='')
        return
        pass

    try:
        title = str(soup.find("title").text.strip())
    except:
        title = "PASS"

    if (title.find('동네생활') != -1 or title.find('내 근처 소식') != -1 or title.find('당근마켓 내 근처 소식') != -1):
        stryArtical = str(number) + ' story_artical\n'
        print(stryArtical, end='')
        return

    if(title.find('숨긴 게시물') != -1 or title.find('당신 근처의 당근마켓') != -1):
        hideArtical = str(number) + ' hide_artical\n'
        print(hideArtical, end='')
        return

    global oldtime
    oldtime = str(soup.select_one('#article-category > time').text.strip())
    sub = str(soup.find('h1', {'property': 'schema:name'}).text.strip())
    region = str(soup.find('meta', {"name": "twitter:data2"}))
    price = str(soup.find('meta', {"name": "twitter:data1"}))
    printinfo = str(number) + " " + str(oldtime) + " " + str(sub) +"\n"
    print(printinfo, end='')

    #무료나눔 알림
    isFree = price.find('content="0원"')
    for i in placeList:
        isRegion = region.find('content="%s"' %i)
        if(isRegion!=-1 and isFree!=-1):
            alram1()
            with open("nanum.txt", "a", encoding="UTF-8") as letfinding:
                letfinding.write(sub + ' - ' + i + '\nhttps://www.daangn.com/articles/%s\n' % number)

    #찾는물건 알림
    subCon = sub.casefold().replace(" ", "")
    for i in subfindCon:
        isFind = subCon.find(i)
        if (isFind!=-1):
            alram2()
            with open("find.txt", "a", encoding="UTF-8") as letfinding:
                letfinding.write('https://www.daangn.com/articles/%s\n' % number)

    with open("number.txt", "a", encoding="UTF-8") as f:
        f.write('\n' + str(number))



"""
url_open(number)

title = str(soup.find(("title")).get_text())
print(title[-7:])
"""

def start():
    number = int(txtread())
    while 1:
        number += 1
        if (oldtime == '1분 이하 전'):
            time.sleep(30)

        t1 = threading.Thread(target=url_open, args=(number, ))
        t1.start()

start()
