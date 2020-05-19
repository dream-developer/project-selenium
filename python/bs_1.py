# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
html = """
<html><head><title>title</title></head>
<body><p>test 1</p><p>test 2</p><p>test 3</p>
</body></html>
"""
soup = BeautifulSoup(html, "html.parser")
for p in soup.find_all("p"):
    print(p.text)