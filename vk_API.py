# -*- coding: utf-8 -*-
from collections import Counter
from statistics import mode
import vk


def sec2min(seconds):
    m, s = divmod(seconds, 60)
    return str("%02d:%02d" % (m, s))


request = 'Tommy Emmanuel Big Brother'
song_list = []
duration = []
title = []

session = vk.Session(
    access_token='73a05d70abc418a24aaa27946029b311c530971a5e6f6d1d515bf8dd9e98ce27217b244508316df16b429')
api = vk.API(session)

# максимальное значение выдаваемых аудиозаписей - 300, стандарт - 30
for song in api.audio.search(q=request, autocomplete=1, count=300):
    # первый элемент в ответе - число записей count, поэтому его нужно отсечь
    if type(song) is dict:
        song_list.append(song)
        duration.append(song['duration'])

data = Counter(duration)
for song in song_list:
    # используем most_common, т.к. mode(duration) выдаст конфликт в случае равных претендентов
    if song['duration'] == data.most_common()[0][0]:
        api.audio.add(audio_id=song['aid'], owner_id=song['owner_id'])
        print('Добавлен трек "{0} - {1}" [{2}]. Всего было вариантов: {3}'.format(
            song['artist'], song['title'], sec2min(song['duration']), len(song_list)))
        break
# print('Аудиозаписей:', len(duration))
# # наиболее распространённое значение длительности (мода)
# # print(mode(duration))
