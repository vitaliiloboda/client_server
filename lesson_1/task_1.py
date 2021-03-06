"""
1. Каждое из слов «разработка», «сокет», «декоратор» представить в строковом формате и
проверить тип и содержание соответствующих переменных.
Затем с помощью онлайн-конвертера преобразовать строковые представление
в формат Unicode и также проверить тип и содержимое переменных.
"""


def check(words: list) -> None:
    """
    the function prints the values and types of each item
    in the list (the list is an argument to the function).
    :param words:
    :return: None
    """

    for word in words:
        print(f'слово: {word}')
        print(f'тип: {type(word)}')
    print('-' * 80)


if __name__ == '__main__':
    word_1 = 'разработка'
    word_2 = 'сокет'
    word_3 = 'декоратор'

    word_1_unic = '\u0440\u0430\u0437\u0440\u0430\u0431\u043e\u0442\u043a\u0430'
    word_2_unic = '\u0441\u043e\u043a\u0435\u0442'
    word_3_unic = '\u0434\u0435\u043a\u043e\u0440\u0430\u0442\u043e\u0440'

    words_list = [word_1, word_2, word_3]
    words_list_unic = [word_1_unic, word_2_unic, word_3_unic]

    check(words_list)
    check(words_list_unic)
