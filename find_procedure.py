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

file_extention = 'sql'
file_extention_string = '.' + file_extention

# Если нужно сократить вывод файлов неким количеством.
# 0 (ноль), если нужно выводить все файлы.
file_output_threshold_value = 5

find_string = ''


def find_string_in_file(find_file_dir, find_file_name, string_in_file):
    with open(os.path.join(find_file_dir, find_file_name), encoding='utf-8', mode='r') as fn:
        file_lines = fn.readlines()
        for line in file_lines:
            if string_in_file in line:
                return True
        return False


def count_of_occurrences(count_dict):
    count_value = 0
    for element in count_dict:
        if count_dict[element] is True:
            count_value += 1
    return count_value


def print_valid_file_names(file_dict):
    for element in file_dict:
        if file_dict[element] is True:
            print(element)


def file_names_dict_init(find_file_extention, init_dict):
    for find_file_name in init_dict:
        if find_file_name[len(find_file_name) - len(find_file_extention):len(find_file_name)] == find_file_extention:
            init_dict[find_file_name] = True


if __name__ == '__main__':

    file_list = os.listdir(target_dir)
    file_list_dic = dict.fromkeys(file_list, False)
    print('В папке {} обнаружено {} файлов'.format(target_dir, len(file_list_dic)))

    file_names_dict_init(file_extention_string, file_list_dic)

    while True:
        find_string = input('Введите строку для поиска: ')

        for file_name in file_list_dic:
            if file_list_dic[file_name] is True:
                if not find_string_in_file(target_dir, file_name, find_string):
                    file_list_dic[file_name] = False

        found_files_count = count_of_occurrences(file_list_dic)
        if found_files_count == 0:
            print('Такого вхождения не найдено. Начните поиск заново.')
            file_names_dict_init(file_extention_string, file_list_dic)
            continue
        elif found_files_count < file_output_threshold_value or file_output_threshold_value == 0:
            print_valid_file_names(file_list_dic)
        else:
            print('Слишком большой список файлов... Нужно уточнить поиск.')
        print('Всего найдено файлов: {}'.format(found_files_count))

