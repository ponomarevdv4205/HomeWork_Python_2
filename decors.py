# Декораторы

import sys
import logging
import inspect

# определяем клиент или сервер:
if sys.argv[0].find('client') == -1:
    LOGGER = logging.getLogger('server_log')
else:
    LOGGER = logging.getLogger('client_log')


# декоратор @log, фиксирующий обращение к декорируемой функции. Он сохраняет ее имя и аргументы.
# В декораторе @log реализована фиксация функции, из которой была вызвана декорированная.
def log(func_z):
    def log_saver(*args, **kwargs):
        rez = func_z(*args, **kwargs)
        LOGGER.debug(f'Была вызвана функция {func_z.__name__} c параметрами {args}, {kwargs}. '
                     f'Вызов из модуля {func_z.__module__}. '
                     f'Вызов из функции {inspect.stack()[1][3]}')
        return rez

    return log_saver
