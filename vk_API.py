# -*- coding: utf-8 -*-
import vk
# TODO проверять, есть ли в списке аудиозаписей такая песня
# TODO вычислять среднюю длительность песни в результатах поиска и добавлять её (+ ту, что со словами?)
# 29
session = vk.Session(access_token='73a05d70abc418a24aaa27946029b311c530971a5e6f6d1d515bf8dd9e98ce27217b244508316df16b4')
api = vk.API(session)
# поиск аудио по названию
print(api.audio.search(q='Beatles'))
print(api.audio.get())
