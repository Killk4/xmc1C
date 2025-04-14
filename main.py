import os
import re
import configparser

# Инициализация файла конфигурации
config = configparser.ConfigParser()

# Пытаемся прочитать файл конфигурации
config.read('config.ini')

# Если удалось, то работаем с ним
try:
    if(config['CONFIG']):
        pass
# Иначе создаём
except:
    config['BRANCHES'] = {
        'barnches' : 'barnches',
        'JK' : 'ЖК',
        'IL' : 'ил',
        'KB' : 'КБ',
        'KV' : 'Кирова',
        'KP' : 'Крупской',
        'NR' : 'Нарат',
        'PK' : 'ПК',
        'SL' : 'Салют',
        'SK' : 'СКФНКЦ',
        'SM' : 'Смена',
        'UN' : 'Юность'
    }

    config['INFO'] = {
        'info' : 'info',
        'version' : '1.0.0',
        'release_date' : '2025-04-14'
    }

    config['SETTINGS'] = {
        'settings' : 'settings',
        'font_family' : 'Tahoma',
        'font_size' : '14',
        'server_updates' : '127.0.0.1',
        'ftp_user' : 'xml_user',
        'ftp_pass' : 'xml_password',
        'months_path' : './months/'
    }

    # Запись стандартных настроек конфигурации в ini файл
    with open('client_config.ini', 'w') as configfile:
        config.write(configfile)



def autofind_xml(branches: list)-> list:
    '''Автовыбор (сопоставление) имён файлов с названиями филиалов'''
    # Получаем список файлов
    files = os.listdir()

    xml_files = ['name:file']

    # Сопоставуляем файлы с названиями ветвей
    for file in files:
        find_file = file.lower()
        for branch in branches:
            if re.search(r'\d.* ' + branch.lower() + '.xml', find_file):
                xml_files.append(f'{branch}:{file}')

    return xml_files

def getBranchesName()-> list:
    '''Получение названия филиала'''

    branche_name = []

    braches = config['BRANCHES']
    for branch in braches:
        branche_name.append(braches[branch])

    return branche_name

result = autofind_xml(getBranchesName())
print(result)