# СТАРТОВЫЙ ФАЙЛ - ДЛЯ ЗАПУСКА НЕСКОЛЬКИХ КЛИЕНТСКИХ МОДУЛЕЙ

import subprocess

PROCESSES = []

while True:
    ACTION = input('Выберите команду: s - запустить Сервер и Клиентов, x - закрыть все окна, q - выход: ')

    if ACTION == 'q':
        print("Программа завершена!")
        break

    elif ACTION == 's':
        CLIENTS = int(input('Введите сколько клиентских модулей запустить: '))
        PROCESSES.append(subprocess.Popen('python server.py', creationflags=subprocess.CREATE_NEW_CONSOLE))

        for i in range(CLIENTS):
            PROCESSES.append(subprocess.Popen(f'python client.py -n user_{i + 1}',
                                              creationflags=subprocess.CREATE_NEW_CONSOLE))


    elif ACTION == 'x':
        print("Все окна закрыты!")
        while PROCESSES:
            VICTIM = PROCESSES.pop()
            VICTIM.kill()
    else:
        print("Вы выбрали не верную команду! Повторите ввод.")
