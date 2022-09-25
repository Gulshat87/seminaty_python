x = int(input())
y = int(input())
z = int(input())


if (not(x and y and z)) == (not(x) or not(y) or not(z)):
    print('ok')
else:
    print('no')