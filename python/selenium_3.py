# -*- coding: utf-8 -*-
from selenium import webdriver
import time
url = "file:///D:/独学/Python/Selenium+BeautifulSoup/project-selenium/html/menu.html"
driver = webdriver.Chrome()
driver.get(url)
# タイトル取得
title = driver.title
print(title)
# ソース取得
html = driver.page_source
print(html)
# 現在のURL
current = driver.current_url
print(current)
time.sleep(3)
driver.quit()
