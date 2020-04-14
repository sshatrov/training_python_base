# -*- coding: utf8 -*-

# 2.1 - Вывести на экран циклом пять строк из нулей, причем каждая строка должна быть пронумерована.
print ("Task 2.1\n")
m = 5
i = 0
while i<m:
    print (i,0)
    i+=1

# 2.2 - Пользователь в цикле вводит 10 цифр. Найти количество введеных пользователем цифр 5.
print ("\n\nTask 2.2\n")
i = 0
ii = 0
input_str = ''
while i<10:
    input_str = input("Enter any number: ")
    if input_str=="5":
      ii+=1
    i+=1
print(f"'5' found {ii} times")

#2.3 - Найти сумму ряда чисел от 1 до 100. Полученный результат вывести на экран.
print ("\n\nTask 2.3\n")
sum = 0

for i in range(1,101):
    sum+=i
print(sum)

#2.4 - Найти произведение ряда чисел от 1 до 10. Полученный результат вывести на экран.
print ("\n\nTask 2.4\n")
sum = 1
for i in range(2,11):
    sum*=i
print(sum)

# 2.5 - Вывести цифры числа на каждой строчке.
print ("\n\nTask 2.5\n")
integer_number = 2129

#print(integer_number%10,integer_number//10)

while integer_number>0:
    print(integer_number%10)
    integer_number = integer_number//10

# 2.6 - Найти сумму цифр числа.
print ("\n\nTask 2.6\n")
integer_number = 2129
sum = 0
while integer_number>0:
    sum+=integer_number%10
    integer_number = integer_number//10
print (sum)

# 2.7 - Найти произведение цифр числа.
print ("\n\nTask 2.7\n")
integer_number = 2129

sum = 1
while integer_number>0:
    sum*=integer_number%10
    integer_number = integer_number//10
print (sum)

# 2.8 - Дать ответ на вопрос: есть ли среди цифр числа 5?
print ("\n\nTask 2.8\n")
integer_number = 215
while integer_number>0:
    if integer_number%10 == 5:
        print('Yes')
        break
    integer_number = integer_number//10
else: print('No')

# 2.9 - Найти максимальную цифру в числе
print ("\n\nTask 2.9\n")
integer_number = 2156
max_number = 0
while integer_number>0:
    if integer_number%10 > max_number:
        max_number = integer_number%10
    integer_number = integer_number//10
print(max_number)

#2.10 - Найти количество цифр 5 в числе
print ("\n\nTask 2.10\n")
integer_number= 51255
i = 0
while integer_number>0:
    if integer_number%10 ==5:
        i+=1
    integer_number = integer_number//10
print(f"'5' found {i} times")
