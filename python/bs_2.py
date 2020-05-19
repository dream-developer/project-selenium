# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
html = """
<html><head><title>title</title></head>
<body><div><p>test</p></div><p>test</p>
</body></html>
"""
soup = BeautifulSoup(html, "html.parser")
print(soup.prettify())