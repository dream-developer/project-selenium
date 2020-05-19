# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
html = "&gt;&lt;&copy;&nbsp;&yen;"
soup = BeautifulSoup(html, "html.parser")
# &gt;&lt;© ¥
print(soup.prettify(formatter="minimal"))
# &gt;&lt;&copy;&nbsp;&yen;
print(soup.prettify(formatter="html"))
# ><© ¥
print(soup.prettify(formatter=None))