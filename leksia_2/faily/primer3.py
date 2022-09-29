colors = ['red', 'green', 'blue']
data = open('file3.txt', 'a')
#data.writelines(colors) #разделителей не будет,значит без пробелов запишется
data.write('\nLine 12\n')
data.write('Line 13\n')
data.close() #закрытие файла-обяз-но!
#сначала ввели только line2 и line3,
#потом написали 12 и 13 и получили другие строки

# или можно писать коротко, без принудительного закрыти close
exit()
with open('file3.txt', 'w') as data:
    data.write('\nLine 12\n') # \n-это разделитель
    data.write('Line 13\n')