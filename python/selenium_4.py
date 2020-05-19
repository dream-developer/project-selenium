# -*- coding: utf-8 -*-
from selenium import webdriver
import time
url = "file:///C:/Users/writer/study_work/html/menu.html"
driver = webdriver.Chrome()
driver.get(url)
# h1タグのテキスト
tags_h1 = driver.find_elements_by_tag_name("h1")
for h1 in tags_h1:
    print(h1.text)
# aタグのテキストとhref属性の値
tags_a = driver.find_elements_by_tag_name("a")
for a in tags_a:
    print(a.text + " " + a.get_attribute("href"))
# ulタグの数 → 1
print(len(driver.find_elements_by_tag_name("ul")))
# liタグの数 → 2
print(len(driver.find_elements_by_tag_name("li")))
# ulタグのテキストを取得
print(driver.find_elements_by_tag_name("ul")[0].text)
# aタグ２つめのテキスト → Tea 
print(driver.find_elements_by_tag_name("a")[1].text)
# aタグ２つめをクリック 
time.sleep(1)
driver.find_elements_by_tag_name("a")[1].click()
tag_a = driver.find_element_by_tag_name("a")
time.sleep(3)
driver.quit()
