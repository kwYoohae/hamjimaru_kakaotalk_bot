from _typeshed import WriteableBuffer
from selenium import webdriver
from bs4 import BeautifulSoup
from time import sleep
import os
import sys
import _typeshed
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no--sandbox')
chrome_options.add_argument("--single-process")
chrome_options.add_argument("--disable-dev-shm-usage")

chromedriver = '/home/hamji/hamjimaru_kakaotalk_bot/python_test/chromedriver' # chromedriver 경로설정

driver = webdriver.Chrome(chromedriver, chrome_options=chrome_options) 
driver.implicitly_wait(3) # chrromedriver 실행 후 3초간 대기
driver.get('https://www.kw.ac.kr/ko/life/facility11.jsp') # 스크래핑할 url 입력
sleep(3)

html= driver.page_source

soup= BeautifulSoup(html, 'lxml')
target = soup.find('tbl-list')

#날짜 데이터 가져옴
date_str = target.find_all("thead")
for i in range(len(date_str)):
    date_str[i]=date_str.get_text('\n')

#식단 데이터 가져옴
diet_str = target.find_all("td")
for i in range(len(diet_str)):
    diet_str[i]=diet_str.get_text('\n')

if os.path.exists('week_date.txt'):
    os.remove('week_date.txt')
if os.path.exists('week_diet.txt'):
    os.remove('week_diet.txt')

diet_fp=open('week_diet.txt','w',encoding='utf-8')
diet_fp.writelines(diet_str)
diet_fp.close()
date_fp=open('week_date.txt')
date_fp.writelines(date_str)
date_fp.close()

driver.close()

# depth_1_tbody = driver.find_element_by_xpath("//*[@id=\"item_body\"]/div[3]/div/div[1]/article/div[3]/div/section/div/table") # 원하는 table의 xpath
# depth_2_tr = depth_1_tbody.find_elements_by_tag_name("tr") #tr부분을 따옴

# for td in depth_2_tr: # tr과 td부분에 대해서 값을 출력하기 
#     haksik_row = td.text
#     haksik_row_list = haksik_row.split("\n")
#     print(haksik_row_list)