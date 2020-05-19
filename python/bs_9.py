from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from bs4 import BeautifulSoup
import time
url = "file:///C:/Users/writer/study_work/html/menu.html"
driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.get(url)
# HTMLをパースして"商品名,単価" の文字列を返す
def get_parsed_data(html):
    soup = BeautifulSoup(html, "html.parser")
    item_name = soup.select_one(".item_name").text
    unit_price = soup.select_one(".unit_price").text
    unit_price = unit_price.replace("円","")
    data = item_name + "," + unit_price
    return data
# １．リンクの要素を取得
item_links = driver.find_elements_by_css_selector("ul.item_link > li > a")
for item_link in item_links:
    # ２．Ctrl + クリック
    actions = ActionChains(driver)
    actions.key_down(Keys.CONTROL)
    # アクセス間隔は1秒以上空ける
    time.sleep(1)
    actions.click(item_link)
    actions.key_up(Keys.CONTROL)
    actions.perform()
    # ３．タブの移動
    driver.switch_to.window(driver.window_handles[1])
    # ４．HTMLをパースし出力
    print(get_parsed_data(driver.page_source))
    # タブを閉じる
    driver.close()
    # ５．元のタブへ移動
    driver.switch_to.window(driver.window_handles[0])
driver.quit()