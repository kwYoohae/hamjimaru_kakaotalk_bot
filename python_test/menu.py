import os
from selenium import webdriver
from bs4 import BeautifulSoup

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no--sandbox')
chrome_options.add_argument("--single-process")
chrome_options.add_argument("--disable-dev-shm-usage")

chromedriver = '/home/hamji/hamjimaru_kakaotalk_bot/python_test/chromedriver' # chromedriver 경로설정

driver = webdriver.Chrome(chromedriver, chrome_options=chrome_options) 
driver.implicitly_wait(3) # chrromedriver 실행 후 3초간 대기
driver.get('https://www.kw.ac.kr/ko/life/facility11.jsp') # 스크래핑할 url 입력

depth_1_tbody = driver.find_element_by_xpath("//*[@id=\"item_body\"]/div[3]/div/div[1]/article/div[3]/div/section/div/table") # 원하는 table의 xpath
depth_2_tr = depth_1_tbody.find_elements_by_tag_name("tr") #tr부분을 따옴

for td in depth_2_tr: # tr과 td부분에 대해서 값을 출력하기 
    haksik_row = td.text
    haksik_row_list = haksik_row.split("\n")
    print(haksik_row_list)