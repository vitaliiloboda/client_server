import json
import os
import sys
import unittest
from lesson_8.common.variables import ACTION, PRESENCE, TIME, USER, ACCOUNT_NAME, RESPONSE, ERROR, ENCODING
from lesson_8.common.utils import get_message, send_message
sys.path.append(os.path.join(os.getcwd(), '..'))


class TestSocket:
    '''
    Тестовый класс для тестирования отправки и получения, при создании требует словарь,
    который будет прогоняться через тестовую функцию
    '''

    def __init__(self, test_dict):
        self.test_dict = test_dict
        self.encoded_message = None
        self.received_message = None

    def send(self, message_to_send):
        '''
        Тестовая функция отправки, корректно кодирует сообщение,
        также сохраняет то, что должно быть отправлено в сокет.
        message_to_send - то, что отправляет в сокет
        :param message_to_send:
        :return:
        '''

        json_test_message = json.dumps(self.test_dict)
        # кодирует сообщение
        self.encoded_message = json_test_message.encode(ENCODING)
        # сохраняем что должно было отправлено в сокет
        self.received_message = message_to_send

    def recv(self, max_len):
        '''
        Получаем данные из сокета
        :param max_len:
        :return:
        '''
        json_test_message = json.dumps(self.test_dict)
        return json_test_message.encode(ENCODING)


class TestUtils(unittest.TestCase):
    test_dict_send = {
        ACTION: PRESENCE,
        TIME: 1.1,
        USER: {
            ACCOUNT_NAME: 'test_test'
        }
    }
    test_dict_recv_ok = {RESPONSE: 200}
    test_dict_recv_err = {
        RESPONSE: 400,
        ERROR: 'Bad Request'
    }

    def test_send_message(self):
        '''Тестируем корректность работы функции отправки, создадим
        тестовый сокет и проверим корректность отправки словаря
        '''
        # экземпляр тестового сокета, хранит собственно тестовый словарь
        test_socket = TestSocket(self.test_dict_send)
        # вызов тестируемой функции, результаты будут сохранены в тестовом сокете
        send_message(test_socket, self.test_dict_send)
        # проверка корректности кодирования словаря
        # сравниваем результат кодирования и результат от тестируемой функции
        self.assertEqual(test_socket.encoded_message, test_socket.received_message)

    def test_send_message_exception(self):
        '''Тестируем генерацию исключения при не словаре на входе
        # и здесь использован следующий формат assertRaises:
        # <<self.assertRaises(TypeError, test_function, args)>>
        '''
        # экземпляр тестового сокета, хранит собственно тестовый словарь
        test_socket = TestSocket(self.test_dict_send)
        # вызов тестируемой функции, результаты будут сохранены в тестовом сокете
        send_message(test_socket, self.test_dict_send)
        self.assertRaises(TypeError, send_message, test_socket, "wrong_dictionary")

    def test_get_ok_message(self):
        '''Тестируем функцию приема сообщения - корректного словаря'''
        test_sock_ok = TestSocket(self.test_dict_recv_ok)
        test_sock_err = TestSocket(self.test_dict_recv_err)
        # тест корректной расшифровки корректного словаря
        self.assertEqual(get_message(test_sock_ok), self.test_dict_recv_ok)

    def test_get_wrong_message(self):
        '''Тестируем функцию приема сообщения - ошибочного словаря'''
        test_sock_ok = TestSocket(self.test_dict_recv_ok)
        test_sock_err = TestSocket(self.test_dict_recv_err)
        # тест корректной расшифровки ошибочного словаря
        self.assertEqual(get_message(test_sock_err), self.test_dict_recv_err)


if __name__ == '__main__':
    unittest.main()
