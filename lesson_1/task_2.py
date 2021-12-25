word_1 = 'class'
word_2 = 'function'
word_3 = 'method'

words_list = [word_1, word_2, word_3]

for word in words_list:
    word_b = f"b'{word}'"
    eval(f'print({word_b})')
    eval(f'print(len({word_b}))')
    eval(f'print(type({word_b}))')
    print('--------------------------')
