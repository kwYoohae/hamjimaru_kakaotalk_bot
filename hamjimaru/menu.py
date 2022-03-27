#-*- coding: utf-8 -*-
#!/usr/bin/env python3
from bs4 import BeautifulSoup
import pandas as pd
import datetime
import requests
import time
import schedule

headers = {
	"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.82 Safari/537.36"
}

def job():
	r = requests.get('https://www.kw.ac.kr/ko/life/facility11.jsp', headers=headers)
	soup = BeautifulSoup(r.text, 'html.parser')
	table = soup.find('table', {'class': 'tbl-list'})
	thead = table.find('thead')
	tbody = table.find('tbody')

	diet1 = map(lambda node: node.text.replace("\n",""), thead.findAll("th")[1:])
	diet2 = map(lambda node: node.text, tbody.findAll("td")[1:])
	data= [diet1,diet2]
	
	toSave = pd.DataFrame(data)
	toSave.to_csv("./table.csv", index=False, header=False, encoding="utf-8")

	now =datetime.datetime.now()
	now =str(now)
	with open("./log.txt",'a') as f:
		f.write("["+now+"] "+"update the diet!\n")
		f.close()

schedule.every(3).hours.do(job)

while True:
	schedule.run_pending()
	time.sleep(1)
