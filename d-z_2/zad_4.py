#  Задайте список из 2N+1 элементов, 
# заполненных числами из промежутка [-N, N].
#  Найдите произведение элементов на указанных
#  позициях. 
#  Позиции вводятся с клавиатуры.

n = int(input())
mass = [i for i in range(-n,n+1)]
print(mass) #сгенериров массив
mult = 1
pos = list(map(int,input().split()))
for i in pos:
    mult *= mass[i]
print(mult)
