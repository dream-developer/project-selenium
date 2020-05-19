# -*- coding: utf-8 -*-
from selenium import webdriver
# selenium.webdriver.support.ui の Select をimport
from selenium.webdriver.support.ui import Select
# selenium.webdriver.common.alert の Alert をimport
from selenium.webdriver.common.alert import Alert
import time
url = "file:///C:/Users/writer/study_work/html/coffee.html"
driver = webdriver.Chrome()
driver.get(url)
# プルダウン要素からSelectインスタンスを取得
element = driver.find_element_by_name("num")
select_num = Select(element)
# select_by_value 等のメソッドで操作
select_num.select_by_value("2")
element = driver.find_element_by_xpath("/html/body/form/input[1]")
element.click()
chk_sugar = driver.find_element_by_css_selector("input[name='included'][value='sugar']")
chk_milk = driver.find_element_by_css_selector("input[name='included'][value='milk']")
chk_cream = driver.find_element_by_css_selector("input[name='included'][value='cream']")
chk_sugar.click()
chk_cream.click()
print(chk_milk.is_selected())
print(chk_cream.is_selected())
element = driver.find_element_by_name("remarks")
element.send_keys("やや熱めでお願いします")
time.sleep(1)
elements = driver.find_element_by_css_selector("input[type='submit']")
# elements = driver.find_element_by_css_selector("input[type='reset']")
elements.click()
# ドライバからAlertインスタンスを取得し、acceptメソッドでOK押下
Alert(driver).accept()
time.sleep(3)
driver.quit()
