# -*- coding: utf-8 -*-
import os
import requests
from lxml import html, etree

html = html.parse(r"E:\!Go\myshazam-history.html")
root = html.getroot()
print(root.xpath('//tr/td[2]/text()'))
# html_string = etree.tostring(html)
# tree = html.fromstring(html_string)


"""
artist
/html/body/table/tbody/tr[2]/td[2]
/html/body/table/tbody/tr[3]/td[2]
/html/body/table/tbody/tr[4]/td[2]
html body table tbody tr td a
"""

"""
title
/html/body/table/tbody/tr[2]/td[1]/a
/html/body/table/tbody/tr[3]/td[1]/a
/html/body/table/tbody/tr[4]/td[1]/a
"""
