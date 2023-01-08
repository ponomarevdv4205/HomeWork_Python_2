"""
9.2. Написать функцию host_range_ping() для перебора ip-адресов из заданного диапазона.
Меняться должен только последний октет каждого адреса.
По результатам проверки должно выводиться соответствующее сообщение.
"""

# Решение:

import ipaddress
from task_9_1 import host_ping


def host_range_ping(start, step, my_tabulate=False):
    start_ip = ipaddress.ip_address(start)
    end_ip = start_ip + int(step) - 1
    ips = []

    while start_ip <= end_ip:
        ips.append(start_ip)
        start_ip += 1

    return [i for i in host_ping(ips, my_tabulate)]


if __name__ == '__main__':
    start_ip = input('С какого ip-адреса начнем проверять? ')
    step_ip = input('Сколько ip-адресов (последние октеты) будем проверять?: ')
    host_range_ping(start_ip, step_ip, my_tabulate=False)


# проверим с 127.0.0.0