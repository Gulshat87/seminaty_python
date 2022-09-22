#которая будет на вход приниать
#число N и выводить числа от -N до N

# n = int(input())
# i = -n
# while i <= n:
#     print(i)
#     i +=1

# или
# n = int(input())
# for i in range(-n,n+1,1):
#     print(i)

#или
n = int(input())
mass = []
for i in range(-n,n+1,1):
    mass.append(i)
print(mass)