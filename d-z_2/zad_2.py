# '2. Напишите программу, которая принимает
#  на вход число N и выдает набор произведений 
#  чисел от 1 до N.

# *Пример:*

# - пусть N = 4, тогда [ 1, 2, 6, 24 ]
#  (1, 1*2, 1*2*3, 1*2*3*4)

# #первый вариант
# n = int(input())
# m = 1
# mass = []

# for i in range(1, n+1):
#     m *= i
#     mass.append(m)
# print(mass) 



# второй вариант-через факториал:

import math
n = int(input())
mass = [math.factorial(i) for i in range(1,n+1)]
print(mass)
