# Задание 3
# 1. Реализовать простое клиент-серверное взаимодействие по протоколу JIM (JSON instant messaging):
# клиент отправляет запрос серверу;
# сервер отвечает соответствующим кодом результата.
#
# Клиент и сервер должны быть реализованы в виде отдельных скриптов, содержащих соответствующие функции.
# Функции клиента:
# 1) сформировать presence-сообщение;
# 2) отправить сообщение серверу;
# 3) получить ответ сервера;
# 4) разобрать сообщение сервера;
# параметры командной строки скрипта client.py
# <addr> [<port>]: addr — ip-адрес сервера; port — tcp-порт на сервере, по умолчанию 7777.

# Решение:

import sys
import json
import socket
import time
from config import STATUS, ACTION, PRESENCE, TIME, USER, ACCOUNT_NAME, RESPONSE, ERROR, DEFAULT_IP_ADDRESS, DEFAULT_PORT
from utils import get_message, send_message


# сформировать presence-сообщение:
def create_presence(account_name='Dima'):
    out = {
        ACTION: PRESENCE,
        TIME: time.time(),
        USER: {
            ACCOUNT_NAME: account_name
        },
        STATUS: STATUS
    }
    return out


def main():
    # параметры командной строки скрипта client.py:
    try:
        addr = sys.argv[1]
        port = int(sys.argv[2])
        if port < 1024 or port > 65535:
            raise ValueError
    except IndexError:
        addr = DEFAULT_IP_ADDRESS
        port = DEFAULT_PORT
    except ValueError:
        print('Порт может быть только в диапазоне от 1024 до 65535')
        sys.exit(1)

    # отправить сообщение и получить ответ сервера:
    my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    my_socket.connect((addr, port))
    message_to_server = create_presence()
    send_message(my_socket, message_to_server)
    try:
        answer = process_ans(get_message(my_socket))
        print(answer)
    except (ValueError, json.JSONDecodeError):
        print('Ошибка декодирования сообщение сервера')


# разобрать сообщение сервера:
def process_ans(message):
    if RESPONSE in message:
        if message[RESPONSE] == 200:
            return '200: ответ сервера получен'
        return f'400: {message[ERROR]}'
    raise ValueError


if __name__ == '__main__':
    main()
