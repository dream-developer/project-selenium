# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
html = "<div>タブレット<p class='info'>最新モデル</p><p class='info'>割引対象</p><p class='info'>即日配達</p></div>"
soup = BeautifulSoup(html, "html.parser")
# タブレット最新モデル割引対象即日配
print(soup.div.text)
extract_tag = soup.div.find(class_="info").extract()
# <p class="info">最新モデル</p>
print(extract_tag)
# タブレット割引対象即日配
print(soup.div.text)
for tab in soup.div.find_all(class_="info"):
    tab.extract()
# タブレット
print(soup.div.text)