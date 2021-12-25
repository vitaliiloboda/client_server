from chardet import detect

with open('test.txt', 'w', encoding='utf-8') as file:
    file.write('сетевое программирование\nсокет\nдекоратор')

with open('test.txt', 'rb') as file:
    content = file.read()
encoding = detect(content)['encoding']

with open('test.txt', encoding=encoding) as file:
    for line in file:
        print(line, end='')
    print()
