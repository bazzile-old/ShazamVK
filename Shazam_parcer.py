# -*- coding: utf-8 -*-
import os
from lxml import html

in_file = r"test\myshazam-history.html"


def get_shazams(filename):
    shaz_song_set = set()
    html_file = html.parse(filename)
    root = html_file.getroot()
    for n in range(len(root.xpath('//tr/td[2]/text()'))):
        # название исполнителя - название композиции; сетом убираем дубликаты
        # TODO убрать дефис между названием песни и исполнителем
        shaz_song_set.add((root.xpath('//tr/td[2]/text()')[n] + ' ' + root.xpath('//tr/td[1]/a/text()')[n]))
    return shaz_song_set
