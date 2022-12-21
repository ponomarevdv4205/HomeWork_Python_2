# Утилиты

import json
import os
import sys
import yaml
from config import MAX_PACKAGE_LENGTH, ENCODING


# Считывание конфигов из второго файлы колнфигов "config.yaml":
def read_config():
    if not os.path.exists('config.yaml'):
        print('config.yaml не найден')
        sys.exit(1)

    with open('config.yaml') as config_file:
        config = yaml.load(config_file, Loader=yaml.FullLoader)

    return config


# Прием и декодирование сообщения:
def get_message(client):
    encoded_response = client.recv(MAX_PACKAGE_LENGTH)
    if isinstance(encoded_response, bytes):
        js_response = encoded_response.decode(ENCODING)
        response = json.loads(js_response)
        if isinstance(response, dict):
            return response
        raise ValueError
    raise ValueError


# Кодирование и отправка сообщения:
def send_message(sock, message):
    js_message = json.dumps(message)
    encoded_message = js_message.encode(ENCODING)
    sock.send(encoded_message)
