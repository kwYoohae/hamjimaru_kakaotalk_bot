#-*- coding: utf-8 -*-
#!/usr/bin/env python3
from selenium import webdriver
from urllib.request import urlopen
from bs4 import BeautifulSoup
from html_table_parser import parser_functions as parser
import pandas as pd
import datetime
from pandas import Series, DataFrame
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--no--sandbox')
chrome_options.add_argument("--single-process")
chrome_options.add_argument('--headless')
chrome_options.add_argument("--disable-dev-shm-usage")

def remove_residue(string):
	removed = ""
	for i in range(len(string)):
		if string[i] == '\n':
			if string[i + 1] == '\n':
				break
		removed += string[i]
	return removed


# chromedriver 경로설정
chromedriver = '/home/hanium/hamjimaru_kakaotalk_bot/python_test/chromedriver'
driver = webdriver.Chrome(chromedriver, options=chrome_options)
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

#print("first command")
#print('월:{0}, 화:{1}, 수:{2}, 목:{3}, 금:{4}'.format(mon,tue,wed,thu,fri))
	diet1 =[mon, tue, wed, thu, fri]
	m1={mon,tue,wed,thu,fri}    
	
for tr in tbody:
	td= tr.find_elements_by_tag_name("td")
	mon = remove_residue(td[1].text)
	tue = remove_residue(td[2].text)
	wed = remove_residue(td[3].text)
	thu = remove_residue(td[4].text)
	fri = remove_residue(td[5].text)


#print("second command")
#print('월:{0}, 화:{1}, 수:{2}, 목:{3}, 금:{4}'.format(mon,tue,wed,thu,fri))
	diet2 =[mon, tue, wed, thu, fri]

data= [diet1,diet2]
toSave = pd.DataFrame(data)
toSave.to_csv("/home/hamji/hamjimaru_kakaotalk_bot/python_test/table_JP.csv", index=False, header=False, encoding="utf-8")

now =datetime.datetime.now()
with open("/log/log.txt",'a') as f:
    f.write("["+now+"] "+"update the diet!")

driver.close()