# -*- coding: utf-8 -*-
from selenium import webdriver
import time
driver = webdriver.Chrome()
url_menu = "file:///C:/Users/writer/study_work/html/menu.html"
url_coffee = "file:///C:/Users/writer/study_work/html/coffee.html"
# [1] このタブは1つめなので driver.window_handles[0]
driver.get(url_menu)
time.sleep(1)
# [2] このタブは2つめなので driver.window_handles[1]
driver.execute_script("window.open('" + url_coffee + "')")
# [3] 2つめのタブに移動
driver.switch_to.window(driver.window_handles[1])
time.sleep(1)
print(driver.title)
# [4] 1つめのタブに移動
driver.switch_to.window(driver.window_handles[0])
time.sleep(1)
print(driver.title)
# [5] 2つめのタブに移動と閉じる
driver.switch_to.window(driver.window_handles[1])
driver.close()
time.sleep(3)
driver.quit()
