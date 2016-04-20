# -*- coding: utf-8 -*-
import time
from collections import Counter
import vk
from shazam_parcer import get_shazams


def sec2min(seconds):
    m, s = divmod(seconds, 60)
    return str("%02d:%02d" % (m, s))

# TODO-basile исключить из шазамов песни, уже имеющиеся в списке моих аудио
def my_vk_song_list():
    my_audios = []
    for my_song in api.audio.get():
        my_audios.append(my_song['artist'] + ' ' + my_song['title'])
    return my_audios


request = 'Tommy Emmanuel - from the hip'
in_file = r"test\myshazam-history.html"

session = vk.Session(
    access_token='73a05d70abc418a24aaa27946029b311c530971a5e6f6d1d515bf8dd9e98ce27217b244508316df16b429')
api = vk.API(session)


for shazam in get_shazams(in_file):
    song_list = []
    duration = []
    # максимальное значение выдаваемых аудиозаписей - 300, стандарт - 30
    for song in api.audio.search(q=shazam, autocomplete=1, count=300):
        # первый элемент в ответе - число записей count, поэтому его нужно отсечь
        if type(song) is dict:
            song_list.append(song)
            duration.append(song['duration'])

    data = Counter(duration)
    for song in song_list:
        # используем most_common, т.к. mode(duration) выдаст конфликт в случае равных претендентов
        # добавляем проверку по длине названия (+7 символов на наличие года в формате /1967/ в названии)
        if song['duration'] == data.most_common()[0][0] and (
                    (len(str((song['artist']))) + len(str((song['title'])))) <= (len(shazam)) + 7):
            # api.audio.add(audio_id=song['aid'], owner_id=song['owner_id'])
            print('Добавлен трек "{0} - {1}" [{2}]. Всего было вариантов: {3}'.format(
                song['artist'], song['title'], sec2min(song['duration']), len(song_list)))
            break
    time.sleep(1)
