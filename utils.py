# Утилиты

import json
from config import MAX_PACKAGE_LENGTH, ENCODING


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
