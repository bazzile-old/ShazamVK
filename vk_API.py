# -*- coding: utf-8 -*-
from collections import Counter
from statistics import mode
import vk
# TODO проверять, есть ли в списке аудиозаписей такая песня
# 29
session = vk.Session(access_token='73a05d70abc418a24aaa27946029b311c530971a5e6f6d1d515bf8dd9e98ce27217b244508316df16b429')
api = vk.API(session)
# поиск аудио по названию
# print(api.audio.search(q='Beatles', count=2))

song_list = []
duration = []
# максимальное значение выдаваемых аудиозаписей - 300
for song in api.audio.search(q='Beatles - Come Together', autocomplete=1, sort=2, count=300):
    # первый элемент в ответе - число записей count, поэтому его нужно отсечь
    if type(song) is dict:
        song_list.append(song)
for song in song_list:
    duration.append(song['duration'])
print('Аудиозаписей:', len(duration))
data = Counter(duration)
print(data.most_common())
# наиболее распространённое значение длительности (мода)
print(mode(duration))
