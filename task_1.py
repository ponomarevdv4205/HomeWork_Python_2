# Урок 1. Концепции хранения информации

# Задание 1

# 1. Каждое из слов «разработка», «сокет», «декоратор» представить в строковом формате и проверить тип и содержание соответствующих переменных.
#  Затем с помощью онлайн-конвертера преобразовать строковые представление в формат Unicode и также проверить тип и содержимое переменных.

# Решение:

print('Решение задания № 1:')
word_1 = 'разработка'
word_2 = 'сокет'
word_3 = 'декоратор'

print(type(word_1))
print(type(word_2))
print(type(word_3))
print(word_1, word_2, word_3)

word_1_unicode = u'\u0440\u0430\u0437\u0440\u0430\u0431\u043e\u0442\u043a\u0430'
word_2_unicode = u'\u0441\u043e\u043a\u0435\u0442'
word_3_unicode = u'\u0434\u0435\u043a\u043e\u0440\u0430\u0442\u043e\u0440'

print(type(word_1_unicode), type(word_2_unicode), type(word_3_unicode))
print(word_1_unicode, word_2_unicode, word_3_unicode)
print(100 * '*')


# 2. Каждое из слов «class», «function», «method» записать в байтовом типе без преобразования в последовательность кодов (не используя методы encode и decode)
# и определить тип, содержимое и длину соответствующих переменных.

# Решение:

print('Решение задания № 2:')
word_1 = b'class'
word_2 = b'function'
word_3 = b'method'

print(type(word_1), type(word_2), type(word_3))
print(word_1, word_2, word_3)
print(len(word_1), len(word_2), len(word_3))
print(100 * '*')


# 3. Определить, какие из слов «attribute», «класс», «функция», «type» невозможно записать в байтовом типе.

# Решение:

print('Решение задания № 3:')
for item in ['attribute', 'класс', 'функция', 'type']:
    try:
        print(item, type(item), item.encode('ascii'), ' - Можно записать в байтовом типе!')
    except:
        print(item, type(item), ' - Нельзя записать в байтовом типе!')

print(100 * '*')


# 4. Преобразовать слова «разработка», «администрирование», «protocol», «standard» из строкового представления в байтовое и выполнить обратное преобразование (используя методы encode и decode).

# Решение:

print('Решение задания № 4:')
for item in ['разработка', 'администрирование', 'protocol', 'standard']:
    item_encode = item.encode('utf-8', 'replace')
    item_decode = item_encode.decode('utf-8')
    print(item, item_encode, item_decode)

print(100 * '*')


# 5. Выполнить пинг веб-ресурсов yandex.ru, youtube.com и преобразовать результаты из байтовового в строковый тип на кириллице.

# Решение:

print('Решение задания № 5:')

import subprocess

for item in ['yandex.ru', 'youtube.com']:
    args = ['ping', item]
    subproc_ping = subprocess.Popen(args, stdout=subprocess.PIPE)
    for line in subproc_ping.stdout:
        print(line.decode('cp866').encode('utf-8').decode('utf-8'))

print(100 * '*')


# 6. Создать текстовый файл test_file.txt, заполнить его тремя строками: «сетевое программирование», «сокет», «декоратор».
# Проверить кодировку файла по умолчанию. Принудительно открыть файл в формате Unicode и вывести его содержимое.

# Решение:

print('Решение задания № 6:')

import locale

code = locale.getpreferredencoding()
print('Кодировка в системе: ', code)

my_file = open('test_file.txt', 'w')
my_file.writelines(['сетевое программирование\n', 'сокет\n', 'декоратор\n'])
print('Кодировка файла "test_file.txt": ', my_file.encoding)
my_file.close()

print("Сейчас будет выведена ошибка, т.к. открываемый файл в другой кодировке: UnicodeDecodeError: 'utf-8' codec can't decode byte 0xf1 in position 0: invalid continuation byte")
with open("test_file.txt", encoding='utf-8') as file:
    for line in file:
        print(line, end='')
