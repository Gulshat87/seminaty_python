# 1.Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.

# *Пример:*

# - 6782 -> 23
# - 0,56 -> 11



num = (input('Ведите число : '))
x = num.split(".") # разделили введеное на 2 части
a = int(x[0]) #целая часть
b = int(x[1]) #дробная часть
sum = 0
while (a !=0):#суммируем числа целой части
    sum = sum + (a % 10) 
    a = a // 10
while (b !=0): #суммируем числа дробной части
    sum = sum + (b % 10)
    b = b // 10
print(sum)

