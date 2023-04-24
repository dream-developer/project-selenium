# -*- coding: utf-8 -*-
from selenium import webdriver
import time
from selenium.webdriver.common.by import By

url = "file:///D:/独学/Python/Selenium+BeautifulSoup/project-selenium/html/menu.html"
driver = webdriver.Chrome()
driver.get(url)
# h1タグのテキスト
tags_h1 = driver.find_elements(By.CSS_SELECTOR, "h1")
for h1 in tags_h1:
    print(h1.text)
# aタグのテキストとhref属性の値
tags_a = driver.find_elements(By.CSS_SELECTOR, "a")
for a in tags_a:
    print(a.text + " " + a.get_attribute("href"))
# ulタグの数 → 1
print(len(driver.find_elements(By.CSS_SELECTOR, "ul")))
# liタグの数 → 2
print(len(driver.find_elements(By.CSS_SELECTOR, "li")))
# ulタグのテキストを取得
print(driver.find_elements(By.CSS_SELECTOR, "ul")[0].text)
# aタグ２つめのテキスト → Tea 
print(driver.find_elements(By.CSS_SELECTOR, "a")[1].text)
# aタグ２つめをクリック 
time.sleep(1)
driver.find_elements(By.CSS_SELECTOR, "a")[1].click()
time.sleep(3)
driver.quit()
