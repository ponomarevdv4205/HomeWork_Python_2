# Конфиг

import logging

# addr — ip-адрес сервера:
DEFAULT_IP_ADDRESS = '127.0.0.1'

# port — tcp-порт на сервере, по умолчанию 7777:
DEFAULT_PORT = 7777

# Максимальная очередь подключений:
MAX_CONNECTIONS = 5

# Максимальная длинна сообщения в байтах:
MAX_PACKAGE_LENGTH = 1024

# Кодировка:
ENCODING = 'utf-8'

# Ключи по умолчанию:
ACTION = 'action'
TIME = 'time'
USER = 'user'
ACCOUNT_NAME = 'account_name'
PRESENCE = 'presence'
RESPONSE = 'response'
ERROR = 'error'
MESSAGE = 'message'
MESSAGE_TEXT = 'mess_text'
SENDER = 'from'
DESTINATION = 'to'
EXIT = 'exit'

# Текущий уровень логирования:
LOGGING_LEVEL = logging.DEBUG

RESPONSE_200 = {RESPONSE: 200}
RESPONSE_400 = {RESPONSE: 400, ERROR: None}
