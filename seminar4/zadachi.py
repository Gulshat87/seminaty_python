# Задачи для решения на семинаре:
# 1. Задайте строку из набора чисел.
#  Напишите программу, которая покажет 
#  большее и меньшее число. В качестве 
#  символа-разделителя используйте пробел.
# Ввод: 2 3 5 -> 2 5

# a = str(input())
# a = list(map(int, a.split()))
# print (f'Большое число: {max(a)}, Меньшее число: {min(a)}')

# 3. Найдите корни квадратного уравнения 
# Ax² + Bx + C = 0 двумя способами:
    
#     1) с помощью математических формул н
#     ахождения корней квадратного уравнения

# def discriminant(a,b,c):
#     return(b**2 - 4*a*c)

# def solution(a,b,c):
#     if d<0:
#         print('Корней нет')
#     elif d==0:
#         print(f'x = (-b/2*a)')
#     else:
#         print(f'x1=((-b+sqrt(d)/2), x2=x1=((-b-sqrt(d)/2)')

# a = int(input())
# b = int(input())
# c = int(input())

# d= discriminant(a,b,c)
# solution(a,b,c)
#     2) с помощью дополнительных библиотек
#     Python(sympy)
# import sympy
# from sympy.solve import solve
# from sympy import Symbol


# a = int(input())
# b = int(input())
# c = int(input())

# # d= discriminant(a,b,c)
# # solution(a,b,c)

# x = sympy.Symbol('x')
# print(sympy.solve(a*x**2+b*x+c,x))


# 3. Задайте два числа. Напишите программу,

#  которая найдёт НОК (наименьшее общее кратное)
#   этих двух чисел.
# Ввод  3 , 10 -> 30

a = int(input())
b = int(input())
i = 1
while True:
    if i % a == 0 and i % b == 0:
        print(i)
        break
    i += 1