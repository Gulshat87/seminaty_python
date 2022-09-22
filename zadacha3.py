#Напишите программу, которая на вход принимает 
#5 чисел и находит максимальное из них.

# c1 = int(input())
# max = c1
# for i in range(4):
#     c1 = int(input())
#     if c1 > max:
#         max = c1
# print(max)

#или через список

# a = list(map(int,input().split()))
# maximum = max(a)
# print(maximum)

#коротко
print(max(list(map(int,input().split()))))




