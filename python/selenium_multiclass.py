# -*- coding: utf-8 -*-
from selenium import webdriver
import time
url = "file:///C:/Users/writer/study_work/html/multiclass.html"
driver = webdriver.Chrome()
driver.get(url)
# multiclass.html にアクセス
elements = driver.find_elements_by_css_selector(".want.need")
for element in elements:
    print(element.text)
time.sleep(3)
driver.quit()
