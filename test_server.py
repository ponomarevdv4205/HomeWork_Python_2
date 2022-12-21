# Задание 4
# 1. Для всех функций из урока 3 написать тесты с использованием unittest.
# Они должны быть оформлены в отдельных скриптах с префиксом test_ в имени файла (например, test_client.py).

# Решение:

import sys
import os
import unittest

sys.path.append(os.path.join(os.getcwd(), '..'))
from config import STATUS, RESPONSE, ERROR, USER, ACCOUNT_NAME, TIME, ACTION, PRESENCE
from server import client_message


class my_TestServer(unittest.TestCase):
    err_dict = {
        RESPONSE: 400,
        ERROR: 'Не верное подключение'
    }

    ok_dict = {RESPONSE: 200}

    def test_no_action(self):
        self.assertEqual(client_message(
            {TIME: '1.1', USER: {ACCOUNT_NAME: 'Dima'}}), self.err_dict)

    def test_wrong_action(self):
        self.assertEqual(client_message(
            {ACTION: 'not_action', TIME: '1.1', USER: {ACCOUNT_NAME: 'Dima'}}), self.err_dict)

    def test_no_time(self):
        self.assertEqual(client_message(
            {ACTION: PRESENCE, USER: {ACCOUNT_NAME: 'Dima'}}), self.err_dict)

    def test_no_user(self):
        self.assertEqual(client_message(
            {ACTION: PRESENCE, TIME: '1.1'}), self.err_dict)

    def test_unknown_user(self):
        self.assertEqual(client_message(
            {ACTION: PRESENCE, TIME: 1.1, USER: {ACCOUNT_NAME: 'not_Dima'}}), self.err_dict)

    def test_ok_check(self):
        self.assertEqual(client_message(
            {ACTION: PRESENCE, TIME: 1.1, USER: {ACCOUNT_NAME: 'Dima'}}), self.ok_dict)

    def test_ok_status(self):
        self.assertEqual(client_message(
            {ACTION: PRESENCE, TIME: 1.1, USER: {ACCOUNT_NAME: 'Dima'}, STATUS: 'online'}), self.ok_dict)


if __name__ == '__main__':
    unittest.main()
