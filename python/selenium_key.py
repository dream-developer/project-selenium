# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
url = "file:///C:/Users/writer/study_work/html/key.html"
driver = webdriver.Chrome()
driver.get(url)
text1 = driver.find_element_by_name("text1")
text2 = driver.find_element_by_name("text2")
# text1 SHIFTキー押しながら test
text1.send_keys(Keys.SHIFT, "test")
# text1 Ctrlキー押しながら ac
text1.send_keys(Keys.CONTROL, "ac")
# text2 Ctrlキー押しながら v
text2.send_keys(Keys.CONTROL, "v")
time.sleep(3)
driver.quit()
