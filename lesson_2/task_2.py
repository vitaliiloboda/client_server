"""2. Задание на закрепление знаний по модулю json. Есть файл orders в формате JSON с информацией о заказах.
Написать скрипт, автоматизирующий его заполнение данными.
Для этого:
Создать функцию write_order_to_json(), в которую передается 5 параметров — товар (item), количество (quantity),
цена (price), покупатель (buyer), дата (date). В это словаре параметров обязательно должны присутствовать
юникод-символы, отсутствующие в кодировке ASCII.
Функция должна предусматривать запись данных в виде словаря в файл orders.json.
При записи данных указать величину отступа в 4 пробельных символа;
Необходимо также установить возможность отображения символов юникода: ensure_ascii=False;
Проверить работу программы через вызов функции write_order_to_json() с передачей в нее значений каждого параметра.
"""

# {"orders": []}


import json
from pprint import pprint


def write_order_to_json(item: str, quantity: int, price: int, buyer: str, date: str) -> None:
    data_dict = {
        'item': item,
        'quantity': quantity,
        'price': price,
        'buyer': buyer,
        'date': date
    }

    with open('orders.json', 'r+', encoding='utf-8') as file:
        file.seek(0, 2)
        file.seek(file.tell() - 2, 0)
        file.write(', ')
        if file.tell() < 16:
            file.seek(file.tell() - 2, 0)
        else:
            file.seek(file.tell() - 0, 0)
        json.dump(data_dict, file, indent=4, ensure_ascii=False)
        file.write(']}')


write_order_to_json('стол', 2, 50, 'John Smith', '25/11/2021')
write_order_to_json('стул', 5, 25, 'Ivan Tree', '01/12/2021')

with open('orders.json', encoding='utf-8') as f:
    content = json.load(f)
    pprint(content)
