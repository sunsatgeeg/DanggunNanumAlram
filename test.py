from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import time
import os

#browser = webdriver.Chrome(r"C:\Program Files\Google\Chrome\Application\chrome.exe")
browser = webdriver.Chrome()

global startnumber
startnumber = 197174000

browser.get('http://www.daangn.com/articles/%s'%startnumber)

def back(startnumber):
    time.sleep(1)
    global backnumber
    backnumber = startnumber
    browser.get('http://www.daangn.com/articles/%s'%backnumber)
    find(startnumber)
    return

def next(startnumber):
    time.sleep(1)
    global nextnumber
    nextnumber = startnumber
    browser.get('http://www.daangn.com/articles/%s'%nextnumber)
    find(startnumber)
    return

def find(startnumber):
    time.sleep(1)
    try:
        WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="temperature-wrap"]/dt')))
    except:
        print("실패")
    if(browser.find_element_by_xpath('//*[@id="no-article"]')):
        print("게시글이 삭제되었거나 존재하지 않습니당 :( 이전 글을 찾습니다.")
        startnumber -= 1
        back(startnumber)
    #else:
    #    print("게시글이 정해놓은 조건에 맞지 않습니당 :( 다음 글을 찾습니다.")
    #    startnumber += 1
    #    next(startnumber)

find(startnumber)






#try:
#    elem = WebDriverWait(browser, 100).until(EC.presence_of_element_located((By.CLASS_NAME, 'chat-input__textarea')))
#except:
#    print("실패")
#
#time.sleep(1)
#
#browser.find_element_by_tag_name('textarea').send_keys("GeeG")
##텔론_
#try:
#    elem = WebDriverWait(browser, 100).until(EC.presence_of_element_located((By.CLASS_NAME, 'chu__s')))
#except:
#    print("실패")
#
#print("Go")
#
#browser.find_element_by_class_name('tw-align-items-center tw-core-button-label tw-flex tw-flex-grow-0').click()


