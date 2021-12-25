word_1 = 'attribute'
word_2 = 'класс'
word_3 = 'функция'
word_4 = 'type'

words_list = [word_1, word_2, word_3, word_4]

for word in words_list:
    word_b = f"b'{word}'"
    try:
        eval(f'print({word_b})')
        # eval(word_b)
    except SyntaxError:
        print(f'{word}: Невозможно записать в байтовом типе')
