# -*- coding: utf-8 -*-
from selenium import webdriver
import time
url = "file:///D:/独学/Python/Selenium+BeautifulSoup/project-selenium/html/menu.html"
# Chrome のドライバを取得
driver = webdriver.Chrome()
# urlを開く
driver.get(url)
time.sleep(3)
# 終了する
driver.quit()