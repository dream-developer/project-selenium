# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
html = """
<html><head><title>title</title><body>
<div>
  div1
  <p>div1_p1</p>
  <p>div1_p2</p>
</div>
<p>p1</p>
<p>p2</p>
</body></html>
"""
soup = BeautifulSoup(html, "html.parser")
# <p>div1_p1</p>
print(soup.div.p)
# <p>div1_p1</p>
print(soup.p)
# <p>div1_p2</p>
print(soup.p.next_sibling.next_sibling)
# <p>p1</p>
print(soup.div.next_sibling.next_sibling)
# ['\n  div1\n  ', <p>div1_p1</p>, ' ', <p>div1_p2</p>, '\n']
print(soup.div.contents)
