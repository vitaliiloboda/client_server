word_1 = 'разработка'
word_2 = 'администрирование'
word_3 = 'protocol'
word_4 = 'standard'

words_list = [word_1, word_2, word_3, word_4]

for word in words_list:
    word_e = word.encode('utf-8')
    print(word_e)
    print(type(word_e))
    word_d = word_e.decode('utf-8')
    print(word_d)
    print(type(word_d))
    print('------------------------------------')
