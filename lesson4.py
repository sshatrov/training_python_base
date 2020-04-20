#!/usr/bin/python3
# -*- coding: utf8 -*-
# 1. Напишите функцию (F): на вход список имен и целое число N;
# на выходе список длины N случайных имен из первого списка (могут повторяться, можно взять значения:
# количество имен 20, N = 100, рекомендуется использовать функцию random);
import random
def random_names(names_list, int_number):
    names_list_i = []
    i = 0
    while i <int_number:
        names_list_i.append(names_list[random.randrange(0,len(names_list))])
        i+=1
    return names_list_i
names_list = ["Абакум", "Абрам", "Абросим", "Аввакум", "Август", "Авдей",
              "Авдий", "Авель", "Авенир", "Аверий", "Аверкий", "Аверьян",
              "Авксентий", "Аврам", "Аврелиан", "Автоном", "Агап", "Агапий", "Агапит",
              "Агафангел", "Борис"]
int_number = 100

# 2. Напишите функцию вывода самого частого имени из списка на выходе функции F;
def frequent_names(names_list_input):
    names_dict = dict()
    for name in names_list_input:
        if name in names_dict.keys():
            names_dict[name]+=1
        else:
            names_dict[name]=1
    sort1 = list(names_dict)
    names_dict_sorted = list (names_dict.items())
    names_dict_sorted.sort(key=lambda name: name[1])
    return(names_dict_sorted[-1][0])

# 3. Напишите функцию вывода самой редкой буквы, с которого начинаются имена в списке на выходе функции F.
def unique_letter(names_list_input):
    names_list_trimmed = list(map (lambda name: name[0],names_list_input))
    letters_dict = dict()
    for letter in names_list_trimmed:
        if letter in letters_dict:
            letters_dict[letter]+=1
        else:
            letters_dict[letter]=1
    letters_dict_sorted = list (letters_dict.items())
    letters_dict_sorted.sort(key = lambda letter: letter[1])
    return (letters_dict_sorted[0][0])

# 4.  В файле с логами найти дату самого позднего лога (по метке времени): https://drive.google.com/open?id=1pKGu-u2Vvtx4xK8i2ZhOzE5rBXyO4qd8

fp = open("log")
fc = fp.readlines()
lines_list = list(map(lambda line: line.split(' - '),fc))
lines_list.sort(key=lambda line:line[0])
print(" - ".join(lines_list[-1]))
