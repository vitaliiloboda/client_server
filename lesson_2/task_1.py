"""
Задание на закрепление знаний по модулю CSV. Написать скрипт, осуществляющий выборку определенных данных
из файлов info_1.txt, info_2.txt, info_3.txt и формирующий новый «отчетный» файл в формате CSV.
Для этого:
Создать функцию get_data(), в которой в цикле осуществляется перебор файлов с данными, их открытие и считывание данных.
В этой функции из считанных данных необходимо с помощью регулярных выражений извлечь значения параметров
«Изготовитель системы», «Название ОС», «Код продукта», «Тип системы».
Значения каждого параметра поместить в соответствующий список.
Должно получиться четыре списка — например, os_prod_list, os_name_list, os_code_list, os_type_list.
В этой же функции создать главный список для хранения данных отчета — например,
main_data — и поместить в него названия столбцов отчета в виде списка:
«Изготовитель системы», «Название ОС», «Код продукта», «Тип системы».
Значения для этих столбцов также оформить в виде списка и поместить в файл main_data (также для каждого файла);
Создать функцию write_to_csv(), в которую передавать ссылку на CSV-файл.
В этой функции реализовать получение данных через вызов функции get_data(),
а также сохранение подготовленных данных в соответствующий CSV-файл;
Проверить работу программы через вызов функции write_to_csv().
"""
import csv
from chardet import detect
import re


def get_data(files: list, params: list, lists: list) -> list:
    main_data = [params]

    for f in files:
        with open(f, 'rb') as file:
            content = file.read()
            encoding = detect(content)['encoding']

        with open(f, encoding=encoding) as file:
            content = file.read()

            for i in range(len(params)):
                search_result = re.search(fr'{params[i]}(.+)', content)
                result = re.split(r':\s+', search_result.group())[1]
                lists[i].append(result)

    for i in range(len(lists[0])):
        new_list = []
        for j in lists:
            new_list.append(j[i])
        main_data.append(new_list)

    return main_data


def write_to_csv(file: str, files: list, params: list, lists: list) -> None:
    data = get_data(files, params, lists)

    with open(file, 'w', encoding='utf-8') as file:
        file_writer = csv.writer(file)
        file_writer.writerows(data)


os_prod_list = []
os_name_list = []
os_code_list = []
os_type_list = []

file_list = ['info_1.txt', 'info_2.txt', 'info_3.txt']
search_param = ['Изготовитель системы', 'Название ОС', 'Код продукта', 'Тип системы']
result_lists = [os_prod_list, os_name_list, os_code_list, os_type_list]

write_to_csv('data_file.csv', file_list, search_param, result_lists)

with open('data_file.csv', encoding='utf-8') as f:
    f_reader = csv.reader(f)
    for row in f_reader:
        print(row)
