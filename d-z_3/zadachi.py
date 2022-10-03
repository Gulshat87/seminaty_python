# . Задайте список из нескольких чисел. 
# Напишите программу, которая найдёт сумму 
# элементов списка, стоящих на нечётной позиции.

# *Пример:*

# - [2, 3, 5, 9, 3] -> на нечётных
#  позициях элементы 3 и 9, ответ: 12

from itertools import count
from random import random


# def sum(mass):
#     count=0
#     for i in range(i, len(mass),2):
#         count +=mass[i]
#     print(count)
# a = [random.randint(1,10) for i in range(5)]
# print(a)
# sum(a)

# 2. Напишите программу,
#  которая найдёт произведение пар чисел 
#  списка. Парой считаем первый и последний 
#  элемент, второй и предпоследний и т.д.

# *Пример:*

# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

# def sum(mass):
#     resmass = []
#     if len(mass)%2 == 0:
#         for i in range(len(mass)//2):
#             resmass.append(mass[i]*mass[len(mass)-1-i])
#         else:
#             for i in range(len(mass)//2+1):
#               resmass.append(mass[i]*mass[len(mass)-1-i])  
#     print(resmass)
# a = [random.randint(1,10) for i in range(5)]
# print(a)
# sum(a)


# 3. Задайте список из вещественных чисел. 
# Напишите программу, которая найдёт разницу 
# между максимальным и минимальным значением 
# дробной части элементов.

# *Пример:*

# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19

# def f1(n):
#     res = str(n)
#     fif = res.find('.')
#     res = float('0.'+ res[fif+1::])
#     return res
# def diffloat(mass):
#     res = []

#     for i in mass:
#         res.append(f1(i))
#     print(max(res)-min(res))

# a = [1.45,22.35,45.2]
# diffloat(a)

# 4. Напишите программу, которая будет 
# преобразовывать десятичное число в двоичное.

# *Пример:*

# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

n = int(input())
print(str(bin(n))[2::])


