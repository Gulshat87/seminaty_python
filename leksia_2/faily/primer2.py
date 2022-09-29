colors = ['red', 'green123', 'blue123']
data = open('file2.txt', 'w') #перезаписывает, старое стирает а новое пишет
data.writelines(colors) #разделителей не будет,значит без пробелов запишется
data.close() #закрытие файла-обяз-но!