# -*- coding: utf-8 -*-
from selenium import webdriver
import time
url = "file:///C:/Users/writer/study_work/html/menu.html"
driver = webdriver.Chrome()
driver.get(url)
# テキストリンクがCoffeeの要素を取得しクリック
element = driver.find_element_by_link_text("Coffee")
element.click()
time.sleep(1)
# ページ更新
driver.refresh()
time.sleep(1)
# 前に戻る
driver.back()
time.sleep(1)
# 次に進む
driver.forward()
print(driver.current_url)
time.sleep(3)
driver.quit()
