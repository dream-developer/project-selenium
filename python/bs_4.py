# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
html = "<html><head><title>title</title></head><body>body</body></html>"
soup = BeautifulSoup(html, "html.parser")
# <title>title</title>
print(soup.html.head.title)
# <title>title</title>
print(soup.title)
# title
print(soup.title.text)