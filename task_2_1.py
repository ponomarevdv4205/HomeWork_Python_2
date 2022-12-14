# Урок 2. Файловое хранение данных

# 1. Задание на закрепление знаний по модулю CSV.
# Написать скрипт, осуществляющий выборку определенных данных из файлов info_1.txt, info_2.txt, info_3.txt и формирующий новый «отчетный» файл в формате CSV.
# Для этого:

# Создать функцию get_data(), в которой в цикле осуществляется перебор файлов с данными, их открытие и считывание данных.
# В этой функции из считанных данных необходимо с помощью регулярных выражений извлечь значения параметров «Изготовитель системы», «Название ОС», «Код продукта», «Тип системы».
# Значения каждого параметра поместить в соответствующий список. Должно получиться четыре списка — например, os_prod_list, os_name_list, os_code_list, os_type_list.
# В этой же функции создать главный список для хранения данных отчета — например, main_data — и поместить в него названия столбцов отчета в виде списка:
# «Изготовитель системы», «Название ОС», «Код продукта», «Тип системы».
# Значения для этих столбцов также оформить в виде списка и поместить в файл main_data (также для каждого файла);

# Создать функцию write_to_csv(), в которую передавать ссылку на CSV-файл. В этой функции реализовать получение данных через вызов функции get_data(),
# а также сохранение подготовленных данных в соответствующий CSV-файл;

# Проверить работу программы через вызов функции write_to_csv().

# Решение:

import csv
import re


def get_data(item):
    os_prod_list = []
    os_name_list = []
    os_code_list = []
    os_type_list = []
    main_data = [['Изготовитель системы', 'Название ОС', 'Код продукта', 'Тип системы']]
    for file in item:
        open_file = open(file)
        for row in open_file:
            row = row.rstrip()
            if re.match('Изготовитель системы', row):
                os_prod_list.append(re.search(r'(Изготовитель системы).\s*(.*)', row).group(2))
            elif re.match('Название ОС', row):
                os_name_list.append(re.search(r'(Название ОС).\s*(.*)', row).group(2))
            elif re.match('Код продукта', row):
                os_code_list.append(re.search(r'(Код продукта).\s*(.*)', row).group(2))
            elif re.match('Тип системы', row):
                os_type_list.append(re.search(r'(Тип системы).\s*(.*)', row).group(2))

    for idx in range(len(item)):
        main_data.append([os_prod_list[idx], os_name_list[idx], os_code_list[idx], os_type_list[idx]])
    return main_data


def write_to_csv(file, data):
    with open(file, 'w', newline='') as f:
        f_writer = csv.writer(f)
        for number in data:
            f_writer.writerow(number)


info = get_data(['info_1.txt', 'info_2.txt', 'info_3.txt'])
write_to_csv('my_file.csv', info)

with open('my_file.csv') as f:
    print(f.read())
