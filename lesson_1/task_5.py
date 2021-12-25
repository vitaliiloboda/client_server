import chardet
import subprocess
import platform

sites_list = ['yandex.ru', 'youtube.com']


def ping(sites, data):
    for site in sites:
        param = '-n' if platform.system().lower() == 'windows' else '-c'
        args = ['ping', param, str(data), site]
        result = subprocess.Popen(args, stdout=subprocess.PIPE)
        for line in result.stdout:
            result = chardet.detect(line)
            line = line.decode(result['encoding'])
            print(line)
        print('-------------------------------------------------------------')


ping(sites_list, 2)
