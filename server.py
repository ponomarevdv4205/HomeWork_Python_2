# Функции сервера:
# 1) принимает сообщение клиента;
# 2) формирует ответ клиенту;
# 3) отправляет ответ клиенту;
# имеет параметры командной строки: -p <port> — TCP-порт для работы (по умолчанию использует 7777); -a <addr> — IP-адрес для прослушивания (по умолчанию слушает все доступные адреса).

# Решение:

import socket
import sys
import json
from config import ACTION, ACCOUNT_NAME, RESPONSE, MAX_CONNECTIONS, PRESENCE, TIME, USER, ERROR, DEFAULT_PORT
from utils import get_message, send_message


def client_message(message):
    # формирует ответ клиенту:
    if ACTION in message and message[ACTION] == PRESENCE and TIME in message \
            and USER in message and message[USER][ACCOUNT_NAME] == 'Dima':
        return {RESPONSE: 200}
    return {
        RESPONSE: 400,
        ERROR: 'Не верное подключение по ACCOUNT_NAME'
    }


def main():
    # параметры командной строки скрипта server.py:
    # -p < port > — TCP - порт для работы:
    try:
        if '-p' in sys.argv:
            port = int(sys.argv[sys.argv.index('-p') + 1])
        else:
            port = DEFAULT_PORT
        if port < 1024 or port > 65535:
            raise ValueError
    except IndexError:
        print('После параметра -\'p\' необходимо указать номер порта')
        sys.exit(1)
    except ValueError:
        print('Порт может быть только в диапазоне от 1024 до 65535')
        sys.exit(1)

    # -a < addr > — IP - адрес для прослушивания:
    try:
        if '-a' in sys.argv:
            ip_address = sys.argv[sys.argv.index('-a') + 1]
        else:
            ip_address = ''

    except IndexError:
        print(
            'После параметра \'a\'- необходимо указать адрес, который будет слушать сервер.')
        sys.exit(1)

    # принимает сообщение клиента и отправляет ответ клиенту:

    my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    my_socket.bind((ip_address, port))
    my_socket.listen(MAX_CONNECTIONS)

    while True:
        client, client_address = my_socket.accept()
        try:
            message_from_client = get_message(client)
            print(message_from_client)
            response = client_message(message_from_client)
            send_message(client, response)
            client.close()
        except (ValueError, json.JSONDecodeError):
            print('Некорретное сообщение от клиента')
            client.close()


if __name__ == '__main__':
    main()
