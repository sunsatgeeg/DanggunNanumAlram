from selenium import webdriver
import time
import winsound

#browser = webdriver.Chrome(r"C:\Program Files\Google\Chrome\Application\chrome.exe")
browser = webdriver.Chrome()

global startnumber
startnumber = 200062100
stack = 0
sleeptime = 0
place = '김포시 풍무동'

browser.get('http://www.daangn.com/articles/%s'%startnumber)

def back(startnumber):
    time.sleep(sleeptime)
    global backnumber
    backnumber = startnumber
    browser.get('http://www.daangn.com/articles/%s'%backnumber)
    find(startnumber)
    return

def next(startnumber):
    time.sleep(sleeptime)
    global nextnumber
    nextnumber = startnumber
    browser.get('http://www.daangn.com/articles/%s'%nextnumber)
    if (browser.title != '당신 근처의 당근마켓' and browser.title != '숨긴 게시물 | 당근마켓 중고거래' and browser.find_elements_by_xpath('//*[@id="no-article"]') == []):
        global stack
        stack = 0
    find(startnumber)
    return


def find(startnumber):
    global stack

    if(browser.title == '당신 근처의 당근마켓' or browser.title == '숨긴 게시물 | 당근마켓 중고거래' or browser.find_elements_by_xpath('//*[@id="no-article"]') != []):
        print("게시글이 삭제되었거나 존재하지 않습니당 :( 이전 글을 찾습니다.",divmod(stack,4))
        stack += 1
        if(divmod(stack,2)[1] == 1):
            startnumber += divmod(stack,2)[0]
            next(startnumber)
        else:
            startnumber -= 1
            back(startnumber)
    else:
        if (browser.find_element_by_xpath('//*[@id="region-name"]').text != place):
            print("next")
            startnumber += 1
            next(startnumber)
        else:
            if(browser.find_elements_by_xpath('//*[@id="article-price-nanum"]') != []):
                winsound.PlaySound('sound.mp3', winsound.SND_FILENAME)
                print(browser.current_url)
                startnumber += 1
                next(startnumber)
            else:
                print("next2")
                startnumber += 1
                next(startnumber)

            print("Alram")


find(startnumber)


