# СТАРТОВЫЙ ФАЙЛ - ЭТО ДЛЯ ЗАПУСКА ТОЛЬКО ДВУХ КЛИЕНТОВ (один на передачу сообщений, а другой на чтение сообщений)

import subprocess

PROCESSES = []

while True:
    ACTION = input('Выберите команду: s - запустить Сервер и Клиентов, x - закрыть все окна, q - выход: ')

    if ACTION == 'q':
        print("Программа завершена!")
        break
    elif ACTION == 's':
        PROCESSES.append(subprocess.Popen('python server.py', creationflags=subprocess.CREATE_NEW_CONSOLE))
        PROCESSES.append(subprocess.Popen('python client_out.py -n user_out', creationflags=subprocess.CREATE_NEW_CONSOLE))
        PROCESSES.append(subprocess.Popen('python client_in.py -n user_in', creationflags=subprocess.CREATE_NEW_CONSOLE))

    elif ACTION == 'x':
        print("Все окна закрыты!")
        while PROCESSES:
            VICTIM = PROCESSES.pop()
            VICTIM.kill()
    else:
        print("Вы выбрали не верную команду! Повторите ввод.")
