# -*- coding: utf-8 -*-
from selenium import webdriver
import time
url = "file:///C:/Users/writer/study_work/html/tea.html"
driver = webdriver.Chrome()
driver.get(url)
# [value='cream'] が無ければ [value='lemon'] の方を取得
if driver.find_elements_by_css_selector("input[name='included'][value='cream']"):
    element = driver.find_element_by_css_selector("input[name='included'][value='cream']")
else:
    element = driver.find_element_by_css_selector("input[name='included'][value='lemon']")
element.click()
time.sleep(3)
driver.quit()
