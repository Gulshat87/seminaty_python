path = 'file3.txt' #путь к файлу, файл должен лежать там, где лежит папка-в общей
# и выводит в консоле
data = open(path, 'r')
for line in data:
    print(line)
data.close()