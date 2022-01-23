""" Декораторы """
import inspect
import logging
import sys
import traceback
import lesson_6.logs.client_log_config
import lesson_6.logs.server_log_config

if sys.argv[0].find('client') == -1:
    LOGGER = logging.getLogger('server')
else:
    LOGGER = logging.getLogger('client')


def log(func):
    def log_saver(*args, **kwargs):
        result = func(*args, **kwargs)
        LOGGER.debug(f'Была вызвана функция {func.__name__} с параметрами {args}, {kwargs}. '
                     f'Вызов из модуля {func.__module__}. '
                     f'Вызов из функции {traceback.format_stack()[0].strip().split()[-1]}. '
                     f'Вызов из функции {inspect.stack()[1][3]}')
        return result
    return log_saver
