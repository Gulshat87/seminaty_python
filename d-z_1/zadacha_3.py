x = int(input())
y = int(input())

x != 0
y != 0
 
if (x > 0) and (y > 0):
    print('точка находится в 1 четверти')
elif (x < 0) and (y > 0):
    print('точка находится во 2 четверти')
elif (x < 0) and (y < 0):
    print('точка находится во 3 четверти')
elif (x > 0) and (y < 0):
    print('точка находится во 4 четверти')