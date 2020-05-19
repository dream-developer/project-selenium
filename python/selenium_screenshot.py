# -*- coding: utf-8 -*-
from selenium import webdriver
import time
url = "file:///C:/Users/writer/study_work/html/javascript.html"
driver = webdriver.Chrome()
driver.get(url)
driver.save_screenshot("screenshot.png")
time.sleep(3)
driver.quit()
