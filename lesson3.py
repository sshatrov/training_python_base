# -*- coding: utf8 -*-
import pymorphy2
fp = open("text.txt", encoding="utf8")
contents = fp.read()

# 1) методами строк очистить текст от знаков препинания;
punct_marks = [",", ".", ":", ";", "!", "?", "—", "»","«","(",")"]
for mark in punct_marks:
    contents = contents.replace(mark," ")

# 2) сформировать list со словами (split);
word_list = contents.split()

# 3) привести все слова к нижнему регистру (map);
# 6) выполнить light с условием: в пункте 2 дополнительно к приведению к нижнему регистру выполнить лемматизацию.
word_list_lower = list(map(lambda x: str.lower(x), word_list))
morph = pymorphy2.MorphAnalyzer()
word_list_lemma = []
for word in word_list_lower:
    word_list_lemma.append(morph.parse(word)[0][2])

# 4) получить из list пункта 3 dict, ключами которого являются слова, а значениями их количество появлений в тексте;
word_dict = dict()
for word in word_list_lemma:
    if word in word_dict.keys():
        word_dict[word]+=1
    else:
        word_dict[word]=1

# 5) вывести 5 наиболее часто встречающихся слов (sort), вывести количество разных слов в тексте (set).
word_list_sorted = list(word_dict.items())
word_list_sorted.sort(key=lambda word: word[1])
# word_list_top5

print("Пять наиболее встречаемых слов:",*word_list_sorted[-5:])
