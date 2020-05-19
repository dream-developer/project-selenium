# -*- coding: utf-8 -*-
from selenium import webdriver
# Keys と ActionChains のimport
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time
url = "file:///C:/Users/writer/study_work/html/menu.html"
driver = webdriver.Chrome()
driver.get(url)
tag_link = driver.find_element_by_tag_name("a")
# Ctrl + クリック
actions = ActionChains(driver)
actions.key_down(Keys.CONTROL)
actions.click(tag_link)
actions.key_up(Keys.CONTROL)
actions.perform()
# タブの移動
driver.switch_to.window(driver.window_handles[1])
time.sleep(3)
# Ctrl + a
actions2 = ActionChains(driver)
actions2.key_down(Keys.CONTROL)
actions2.send_keys("a")
actions2.key_up(Keys.CONTROL)
actions2.perform()
time.sleep(3)
driver.quit()
