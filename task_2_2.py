# Урок 2. Файловое хранение данных

# 2. Задание на закрепление знаний по модулю json. Есть файл orders в формате JSON с информацией о заказах.
# Написать скрипт, автоматизирующий его заполнение данными. Для этого:
# Создать функцию write_order_to_json(), в которую передается 5 параметров — товар (item), количество (quantity), цена (price), покупатель (buyer), дата (date).
# Функция должна предусматривать запись данных в виде словаря в файл orders.json. При записи данных указать величину отступа в 4 пробельных символа;
# Проверить работу программы через вызов функции write_order_to_json() с передачей в нее значений каждого параметра.

# Решение:

import json


def write_order_to_json(item, quantity, price, buyer, date):
    with open('orders.json') as f:
        my_dict = json.load(f)
        my_dict['orders'].append({'item': item, 'quantity': quantity, 'price': price, 'buyer': buyer, 'date': date})
        print(my_dict)

    with open('orders.json', 'w') as j:
        json.dump(my_dict, j, indent=4)


write_order_to_json('Товар_1', 1, 1000, 'Покупатель_1', '11.12.2022')
write_order_to_json('Товар_2', 2, 2000, 'Покупатель_2', '12.12.2022')
write_order_to_json('Товар_3', 3, 3000, 'Покупатель_3', '13.12.2022')
