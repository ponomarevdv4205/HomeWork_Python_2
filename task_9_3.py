"""
9.3. Написать функцию host_range_ping_tab(), возможности которой основаны на функции из примера 2.
Но в данном случае результат должен быть итоговым по всем ip-адресам, представленным в табличном формате (использовать модуль tabulate).
Таблица должна состоять из двух колонок и выглядеть примерно так:
Reachable
10.0.0.1
10.0.0.2

Unreachable
10.0.0.3
10.0.0.4
"""

# Решение:

from tabulate import tabulate
from task_9_2 import host_range_ping


def host_range_ping_tab(start, step, my_tabulate=False):
    print(tabulate(host_range_ping(start, step, my_tabulate), headers='keys'))


if __name__ == "__main__":
    start_ip = input('С какого ip-адреса начнем проверять? ')
    step_ip = input('Сколько ip-адресов (последние октеты) будем проверять?: ')
    host_range_ping_tab(start_ip, step_ip, my_tabulate=True)

# проверим с 127.0.0.0