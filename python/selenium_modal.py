# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.alert import Alert
import time
url = "file:///C:/Users/writer/study_work/html/modal.html"
driver = webdriver.Chrome()
driver.get(url)
# [1] モーダルを出すボタン
driver.find_element_by_id("btn").click()
# [2] モーダルの入力欄
driver.find_element_by_id("inputfield").send_keys("てすと")
# [3] モーダルの入力後OKボタン
driver.find_element_by_xpath("/html/body/div[1]/div[3]/div/button").click()
time.sleep(3)
driver.quit()
