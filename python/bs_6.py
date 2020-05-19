# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
html = """
<div>
  div1
  <p class="stand">div1_p1</p>
  <p class="stand">div1_p2</p>
</div>
<p id="a">p1</p>
<p>p2</p>
"""
soup = BeautifulSoup(html, "html.parser")
# <p id="a">p1</p>
print(soup.find(id = "a"))
# <p class="stand">div1_p1</p>
print(soup.find(class_ = "stand"))
# <p id="a">p1</p>
print(soup.find("p",id = "a"))
# [<p class="stand">div1_p1</p>, <p class="stand">div1_p2</p>]
print(soup.find_all(class_ ="stand"))
# div1_p1\ndiv1_p2
for tag in soup.find_all(class_ = "stand"):
    print(tag.text)
# div1_p1\ndiv1_p2\np1\np2
for tag in soup.find_all("p"):
    print(tag.text)
