''' Unit-тесты клиента'''

import sys
import os
import unittest
from lesson_8.common.variables import ACTION, PRESENCE, TIME, USER, ACCOUNT_NAME, RESPONSE, ERROR
from lesson_8.client import create_presence, process_ans
sys.path.append((os.path.join(os.getcwd(), '..')))


class TestClass(unittest.TestCase):
    '''
    Класс с тестами
    '''

    def test_def_presense_not_none(self):
        '''Тестируем что получаем не None'''
        self.assertIsNotNone(create_presence(), True)

    def test_def_presense_return_dict(self):
        '''Тестируем что получаем словарь'''
        test = create_presence()
        self.assertIsInstance(create_presence(), dict)

    def test_def_presense(self):
        '''Тест корректного запроса'''
        test = create_presence()
        test[TIME] = 1.1
        self.assertEqual(test, {ACTION: PRESENCE, TIME: 1.1, USER: {ACCOUNT_NAME: 'Guest'}})

    def test_200_ans(self):
        '''Тест корректного разбора ответа 200'''
        self.assertEqual(process_ans({RESPONSE: 200}), '200 : OK')

    def test_400_ans(self):
        '''Тест корретного разбора 400'''
        self.assertEqual(process_ans({RESPONSE: 400, ERROR: 'Bad Request'}), '400 : Bad Request')

    def test_no_response(self):
        '''Тест исключения без поля RESPONSE'''
        self.assertRaises(ValueError, process_ans, {ERROR: 'Bad Request'})


if __name__ == '__main__':
    unittest.main()
