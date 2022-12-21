# Задание 4
# 1. Для всех функций из урока 3 написать тесты с использованием unittest.
# Они должны быть оформлены в отдельных скриптах с префиксом test_ в имени файла (например, test_client.py).

# Решение:

import sys
import os
import unittest
import json

sys.path.append(os.path.join(os.getcwd(), '..'))
from config import RESPONSE, ERROR, USER, ACCOUNT_NAME, TIME, ACTION, PRESENCE, ENCODING
from utils import read_config, get_message, send_message


class my_TestSocket:

    def __init__(self, test_dict):
        self.test_dict = test_dict
        self.encoded_message = None
        self.receved_message = None

    def send(self, message_to_send):
        json_test_message = json.dumps(self.test_dict)
        self.encoded_message = json_test_message.encode(ENCODING)
        self.receved_message = message_to_send

    def recv(self, max_len):
        json_test_message = json.dumps(self.test_dict)
        return json_test_message.encode(ENCODING)


class Tests(unittest.TestCase):

    def test_config_default_ip(self):
        self.assertEqual(read_config()['DEFAULT_IP_ADDRESS'], '127.0.0.1')

    def test_config_default_port(self):
        self.assertEqual(read_config()['DEFAULT_PORT'], 7777)

    def test_config_max_connection(self):
        self.assertEqual(read_config()['MAX_CONNECTIONS'], 5)

    def test_config_max_package_length(self):
        self.assertEqual(read_config()['MAX_PACKAGE_LENGTH'], 1024)

    def test_config_encoding(self):
        self.assertEqual(read_config()['ENCODING'], 'utf-8')

    def test_config_status(self):
        self.assertEqual(read_config()['STATUS'], 'online')

    test_dict_send = {
        ACTION: PRESENCE,
        TIME: 111111.222222,
        USER: {
            ACCOUNT_NAME: 'ABCD'
        }
    }
    test_dict_recv_ok = {RESPONSE: 200}
    test_dict_recv_err = {
        RESPONSE: 400,
        ERROR: 'Bad Request'
    }

    def test_send_message(self):
        test_socket = my_TestSocket(self.test_dict_send)
        send_message(test_socket, self.test_dict_send)
        self.assertEqual(test_socket.encoded_message, test_socket.receved_message)
        with self.assertRaises(Exception):
            send_message(test_socket, test_socket)

    def test_get_message(self):
        test_sock_ok = my_TestSocket(self.test_dict_recv_ok)
        test_sock_err = my_TestSocket(self.test_dict_recv_err)
        self.assertEqual(get_message(test_sock_ok), self.test_dict_recv_ok)
        self.assertEqual(get_message(test_sock_err), self.test_dict_recv_err)


if __name__ == '__main__':
    unittest.main()
