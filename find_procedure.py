# Задание
# мне нужно отыскать файл среди десятков других
# я знаю некоторые части этого файла (на память или из другого источника)
# я ищу только среди .sql файлов
# 1. программа ожидает строку, которую будет искать (input())
# после того, как строка введена, программа ищет её во всех файлах
# выводит список найденных файлов построчно
# выводит количество найденных файлов
# 2. снова ожидает ввод
# поиск происходит только среди найденных на этапе 1
# 3. снова ожидает ввод
# ...
# Выход из программы программировать не нужно.
# Достаточно принудительно остановить, для этого можете нажать Ctrl + C

# Пример на настоящих данных

# python3 find_procedure.py
# Введите строку: INSERT
# ... большой список файлов ...
# Всего: 301
# Введите строку: APPLICATION_SETUP
# ... большой список файлов ...
# Всего: 26
# Введите строку: A400M
# ... большой список файлов ...
# Всего: 17
# Введите строку: 0.0
# Migrations/000_PSE_Application_setup.sql
# Migrations/100_1-32_PSE_Application_setup.sql
# Всего: 2
# Введите строку: 2.0
# Migrations/000_PSE_Application_setup.sql
# Всего: 1

# не забываем организовывать собственный код в функции

import os
# import re

migrations = 'Migrations'
current_dir = os.path.dirname(os.path.abspath(__file__))
target_dir = os.path.join(current_dir, migrations)
file_list = os.listdir(target_dir)

file_extention = 'sql'
file_extention_string = '.' + file_extention

find_string = ''


def find_string_in_file(file_dir, file_name, find_string_in_file):
    with open(os.path.join(file_dir, file_name), encoding='utf-8', mode='r') as fn:
        file_lines = fn.readlines()
        for line in file_lines:
            if find_string_in_file in line:
                return True
        return False


if __name__ == '__main__':
    file_list_dic = dict.fromkeys(file_list, True)
    print('В папке {} обнаружено {} файлов'.format(target_dir, len(file_list_dic)))
    while True:
        find_string = input('Введите строку для поиска: ')
        for file_name in file_list_dic:
            # print(re.match(r'sql\Z', file_name))
            if file_name[len(file_name)-4:len(file_name)] == file_extention_string:
                if find_string_in_file(target_dir, file_name, find_string):
                    print(file_name)
        break

