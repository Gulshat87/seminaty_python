# функция добавления данных в справочник

def adding_data():
    a = input('Введите фамилию, имя и отчества абонента => ')
    b = input('Введите номер телефона абонента => ')
    data = a + '-->' + b
    return data

# функция поиска абонента по справочнику

def search_subscriber(f):
    a = input('Введите фамилию/имя/отчество/телефон => ')
    b = list(filter(lambda x: a in x, f.split('\n')))
    return '\n'.join(b)
        
