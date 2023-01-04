# Утилиты

import json
import os
import sys
import yaml
from config import MAX_PACKAGE_LENGTH, ENCODING
from decors import log
from errors import IncorrectDataRecivedError, NonDictInputError


# Считывание конфигов из второго файлы колнфигов "config_old.yaml":
@log
def read_config():
    if not os.path.exists('config_old.yaml'):
        print('config_old.yaml не найден')
        sys.exit(1)

    with open('config_old.yaml') as config_file:
        config = yaml.load(config_file, Loader=yaml.FullLoader)

    return config


# Прием и декодирование сообщения:
@log
def get_message(client):
    encoded_response = client.recv(MAX_PACKAGE_LENGTH)
    if isinstance(encoded_response, bytes):
        json_response = encoded_response.decode(ENCODING)
        response = json.loads(json_response)
        if isinstance(response, dict):
            return response
        else:
            raise IncorrectDataRecivedError
    else:
        raise IncorrectDataRecivedError


# Кодирование и отправка сообщения:
@log
def send_message(sock, message):
    if not isinstance(message, dict):
        raise NonDictInputError
    js_message = json.dumps(message)
    encoded_message = js_message.encode(ENCODING)
    sock.send(encoded_message)
