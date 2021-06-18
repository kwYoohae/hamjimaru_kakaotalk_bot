from selenium import webdriver
from bs4 import BeautifulSoup
chromedriver = 'C:\\Users\yhc95\Desktop\code\연습\python\chromedriver.exe'

driver = webdriver.Chrome(chromedriver)
driver.implicitly_wait(3)
driver.get('https://www.kw.ac.kr/ko/life/facility11.jsp')

depth_1_tbody = driver.find_element_by_xpath("//*[@id=\"item_body\"]/div[3]/div/div[1]/article/div[3]/div/section/div/table")
depth_2_tr = depth_1_tbody.find_elements_by_tag_name("tr")

for td in depth_2_tr:
    haksik_row = td.text
    haksik_row_list = haksik_row.split("\n")
    print(haksik_row_list)