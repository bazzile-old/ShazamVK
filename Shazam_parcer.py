# -*- coding: utf-8 -*-
import os
from lxml import html


song_set = set()
html = html.parse(r"test\myshazam-history.html")
root = html.getroot()
for n in range(len(root.xpath('//tr/td[2]/text()'))):
    # название исполнителя - название композиции; сетом убираем дубликаты
    # TODO убрать дефис между названием песни и исполнителем
    song_set.add((root.xpath('//tr/td[2]/text()')[n] + ' - ' + root.xpath('//tr/td[1]/a/text()')[n]))
print(len(song_set))