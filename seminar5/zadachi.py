# 1.В файле находится N натуральных чисел, записанных через пробел. 
# Среди чисел не хватает одного, чтобы выполнялось условие
#  A[i] - 1 = A[i-1]. Найдите это число.
#пример: 1 2 4 5 ->3

# lst = list(map(int, input("Введите числа через пробел:\n").split()))

# def Isascending(A):
#     for i in range(1, len(A) - 1):
#         if A[i]-1 != A[i-1]:
            
#             n = A[i-1] + 1
            
#             print(n)
#             break
# Isascending(lst)


# 2.Дан список чисел. Создайте список, в который попадают
#  числа, описываемые возрастающую последовательность. 
#  Порядок элементов менять нельзя.

# Пример:

# [1, 5, 2, 3, 4, 6, 1, 7] => [1, 2, 3] 
# или [1, 7] или [1, 6, 7] и т.д.

lst = [1, 5, 2, 3, 4, 6, 1, 7]
lst2 = [5, 4, 3, 2, 1, 0, -1, -2]
lst3 = [1, 1, 1, 1, 1, 1, 1, 1]

def make_new_list(old_list):
    new_list = []
    for i in range(len(old_list)):
        if i == 0 or old_list[i] > new_list[-1]:
            new_list.append(old_list[i])
    return new_list

print(make_new_list(lst), make_new_list(lst2), make_new_list(lst3))

# 3.Напишите программу, удаляющую из текста
#  все слова, содержащие "абв".

mystr = 'abcdefg'
mylist = mystr.split()
mylist = list(mystr)
del mylist[0:3]

print(mylist)