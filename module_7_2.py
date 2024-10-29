from os import write


def custom_write(file_name, strings): #Замутим функцию
    strings_positions = {} #Здесь подготовим списочек
    with open ('ex.txt', 'w+') as file: # когда открывается файл, в режиме чтения,
                                         # как переменная которую дальше будем называть file
        for i, string in enumerate(strings, start=1): #Для айтемов из интерируемого объекста переберем элементы и их
                                                        #индексы
            position = file.tell()  #кстати где там курсор сейчас?
            file.write(string + '\n') #в файл записываем переменную стринг и потом уходим на новую строку
            strings_positions[(i, position)] = string  #запись строки в словарь с указанием индекса (i) и позиции (position)
    return strings_positions # вернуть заготовленный списочек


info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
    ]
# Вывод на консоль:
result = custom_write('test.txt', info)
for elem in result.items():
  print(elem)