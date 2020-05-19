# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
html = """
<div>
  div1
  <p class="stand">div1_p1</p>
  <p class="stand">div1_p2</p>
</div>
<p id=100>p1</p>
<p>p2</p>
"""
soup = BeautifulSoup(html, "html.parser")
# <p class="stand">div1_p1</p>
print(soup.select_one(".stand"))
# [<p class="stand">div1_p1</p>, <p class="stand">div1_p2</p>]
print(soup.select(".stand"))
# div1_p1\ndiv1_p2
for tag in soup.select(".stand"):
    print(tag.text)
