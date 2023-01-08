"""
9.1. Написать функцию host_ping(), в которой с помощью утилиты ping будет проверяться доступность сетевых узлов.
Аргументом функции является список, в котором каждый сетевой узел должен быть представлен именем хоста или ip-адресом.
В функции необходимо перебирать ip-адреса и проверять их доступность с выводом соответствующего сообщения
 («Узел доступен», «Узел не доступен»). При этом ip-адрес сетевого узла должен создаваться с помощью функции ip_address().
"""

# Решение:

import ipaddress
import platform
import subprocess

# Определяем ОС для передачи соответствующих параметров:
is_win = platform.system().lower()
if is_win == 'windows':
    param = '-n'
else:
    param = '-n'


def host_ping(hosts, my_tabulate=False):
    for host in hosts:
        try:
            ip = ipaddress.ip_address(host)
        except Exception:
            ip = host
        command = ['ping', param, '1', str(ip)]
        response = subprocess.run(command, shell=is_win, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        if my_tabulate==False:
            if response.returncode == 0:
                message = 'Узел доступен'
            else:
                message = 'Узел не доступен'
            yield print(f'{ip} - {message}')
        else:
            if response.returncode == 0:
                key = 'Reachable'
            else:
                key = 'Unreachable'
            yield {key: ip}


if __name__ == '__main__':
    list(host_ping(('yandex.ru', '8.8.8.8', '192.168.0.100', 'gb.ru', '127.0.0.1')))
