# Задание 4
# 1. Для всех функций из урока 3 написать тесты с использованием unittest.
# Они должны быть оформлены в отдельных скриптах с префиксом test_ в имени файла (например, test_client.py).

# Решение:
import sys
import os
import unittest

sys.path.append(os.path.join(os.getcwd(), '..'))
from config import RESPONSE, ERROR, USER, ACCOUNT_NAME, TIME, ACTION, PRESENCE
from client import create_presence, process_response_ans


class my_TestClass(unittest.TestCase):

    # Тест № 1 на все параметры/атрибуты подключения клиента:
    def test_def_presense(self):
        test = create_presence()
        test[TIME] = 1.1
        self.assertEqual(test, {ACTION: PRESENCE, TIME: 1.1, USER: {ACCOUNT_NAME: 'Dima'}})

    # Тест № 2 на удачное подключение:
    def test_200(self):
        self.assertEqual(process_response_ans({RESPONSE: 200}), '200: ответ сервера получен')

    # Тест № 3 на не удачное подключение:
    def test_400(self):
        self.assertEqual(process_response_ans({RESPONSE: 400, ERROR: 'Bad Request'}), '400: Bad Request')

    # Тест № 4 исключение без поля RESPONSE:
    def test_no_response(self):
        self.assertRaises(ValueError, process_response_ans, {ERROR: 'Bad Request'})


if __name__ == '__main__':
    unittest.main()
