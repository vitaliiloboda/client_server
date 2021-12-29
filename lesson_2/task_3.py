"""
3. Задание на закрепление знаний по модулю yaml.
Написать скрипт, автоматизирующий сохранение данных в файле YAML-формата.
Для этого:
Подготовить данные для записи в виде словаря, в котором первому ключу соответствует список,
второму — целое число, третьему — вложенный словарь, где значение каждого ключа — это целое число с юникод-символом,
отсутствующим в кодировке ASCII (например, €);
Реализовать сохранение данных в файл формата YAML — например, в файл file.yaml.
При этом обеспечить стилизацию файла с помощью параметра default_flow_style,
а также установить возможность работы с юникодом: allow_unicode = True;
Реализовать считывание данных из созданного файла и проверить, совпадают ли они с исходными.
"""
import yaml

list_for_key = ['one', 'two', 'three']
int_for_key = 5
dict_for_key = {'1€': 1, '2€': 2, '3€': 3, '4€': 4, '5€': 5}

data = {'one': list_for_key, 'two': int_for_key, 'three': dict_for_key}


def data_to_yaml(data):
    with open('file.yaml', 'w', encoding='utf-8') as file:
        yaml.dump(data, file, default_flow_style=False, allow_unicode=True, sort_keys=False, indent=4)

    with open('file.yaml', 'r', encoding='utf-8') as f:
        content = yaml.load(f, Loader=yaml.FullLoader)
        print(content)


data_to_yaml(data)
