
a = int(input())

print('Введите номер дня недели')

if a == 1:
    print('понедельник - рабочий день')
elif a == 2:
    print('вторник - рабочий день')
elif a == 3:
    print('среда - рабочий день')
elif a == 4:
    print('четверг - рабочий день')
elif a == 5:
    print('пятница - рабочий день')
elif a == 6:
    print('суббота - выходной день')
elif a == 7:
    print('воскресенье - выходной день')
else:
    print('такого дня недели не существует')