#-*- coding: utf-8 -*-
from selenium import webdriver
from urllib.request import urlopen
from bs4 import BeautifulSoup
from html_table_parser import parser_functions as parser
import pandas as pd
from pandas import Series, DataFrame
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--no--sandbox')
chrome_options.add_argument("--single-process")
chrome_options.add_argument('--headless')
chrome_options.add_argument("--disable-dev-shm-usage")

# chromedriver 경로설정
chromedriver = '/home/hamji/hamjimaru_kakaotalk_bot/python_test/chromedriver'
driver = webdriver.Chrome(chromedriver, chrome_options=chrome_options)
driver.implicitly_wait(1)
driver.get('https://www.kw.ac.kr/ko/life/facility11.jsp')  # 스크래핑할 url 입력
driver.implicitly_wait(1)

table = driver.find_element_by_xpath("//*[@id=\"item_body\"]/div[3]/div/div[1]/article/div[3]/div/section/div/table")
thead = table.find_elements_by_tag_name("thead")
tbody = table.find_elements_by_tag_name("tbody")

for tr in thead:
    th= tr.find_elements_by_tag_name("th")
    mon=th[1].text
    tue=th[2].text
    wed=th[3].text
    thu=th[4].text
    fri=th[5].text
       
    print('월:{0}, 화:{1}, 수:{2}, 목:{3}, 금:{4}'.format(mon,tue,wed,thu,fri))
    diet1 =[mon, tue, wed, thu, fri]
    m1={mon,tue,wed,thu,fri}    
    
for tr in tbody:
    td= tr.find_elements_by_tag_name("td")
    mon=td[1].text
    tue=td[2].text
    wed=td[3].text
    thu=td[4].text
    fri=td[5].text
       
    print('월:{0}, 화:{1}, 수:{2}, 목:{3}, 금:{4}'.format(mon,tue,wed,thu,fri))
    diet2 =[mon, tue, wed, thu, fri]
        
data= [[diet1],[diet2]]
toSave = pd.DataFrame(data)
toSave
toSave.to_csv("/home/hamji/hamjimaru_kakaotalk_bot/python_test/table.csv", index=False, header=False, encoding="utf-8")

driver.close()
