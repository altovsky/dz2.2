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

migrations = 'Migrations'
current_dir = os.path.dirname(os.path.abspath(__file__))
target_dir = os.path.join(current_dir, migrations)

file_extension = 'sql'

# Если нужно сократить вывод файлов неким количеством.
# 0 (ноль), если нужно выводить все файлы.
file_output_threshold_value = 7

find_string = ''


def read_files(find_file_dir, find_extension):
    files_list = os.listdir(find_file_dir)
    find_extension_string = f'.{find_extension}'
    files_list_real = []
    for files in files_list:
        if files.endswith(find_extension_string):
            files_list_real.append(files)
    return files_list_real


def find_string_in_file(find_file_dir, find_file_name, string_in_file):
    with open(os.path.join(find_file_dir, find_file_name), encoding='utf-8', mode='r') as fn:
        for line in fn:
            if string_in_file in line:
                return True
        return False


if __name__ == '__main__':

    file_list = read_files(target_dir, file_extension)
    print('В папке {} обнаружено {} файлов'.format(target_dir, len(file_list)))

    while True:
        find_string = input('Введите строку для поиска: ')
        file_list_temp = []
        for file_name in file_list:
            if find_string_in_file(target_dir, file_name, find_string):
                file_list_temp.append(file_name)
        file_list = file_list_temp
        if len(file_list) == 0:
            print('Такого вхождения не найдено. Начните поиск заново.')
            file_list = read_files(target_dir, file_extension)
            continue
        elif len(file_list) < file_output_threshold_value or file_output_threshold_value == 0:
            for file in file_list:
                print(file)
        else:
            print('Слишком большой список файлов... Нужно уточнить поиск.')
        print(f'Всего найдено файлов: {len(file_list)}')
