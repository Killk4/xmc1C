import os
import re
import datetime
import configparser

class Config:
    """
    Класс для работы с файлом конфигурации.
    
    Аргументы:
    configfile: путь к файлу конфигурации

    Методы:
    read_config_file(): читает файл конфигурации
    create_config_file(): создает файл конфигурации"""
    
    def __init__(self):
        self.configfile = 'config.ini'
        self.config = configparser.ConfigParser()
        self.config.read(self.configfile, encoding='utf-8')

    def create_config_file(self):
        '''Создание файла конфигурации'''

        # Филиалы
        self.config['BRANCHES'] = {
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

        # Информация о программе
        self.config['INFO'] = {
            'info' : 'info',
            'version' : '1.0.0',
            'release_date' : '2025-04-14'
        }

        # Настройки программы
        self.config['SETTINGS'] = {
            'settings' : 'settings',
            'font_family' : 'Tahoma',       # Шрифт
            'font_size' : '14',             # Размер шрифта
            'server_updates' : '127.0.0.1', # Сервер обновлений
            'ftp_user' : 'xml_user',        # Пользователь FTP
            'ftp_pass' : 'xml_password',    # Пароль FTP
            'ftp_path' : '/xml/',           # Путь к папке с xml файлами
            'ftp_port' : '21',              # Порт FTP
            'months_path' : './files/'      # Путь к папке с месяцами
        }

        # Запись стандартных настроек конфигурации в ini файл
        with open(self.configfile, 'w', encoding='utf-8') as conf:
            self.config.write(conf)

    def read_config_file(self):
        '''Чтение файла конфигурации'''

        try:
            if(self.config['INFO']):        # Проверка наличия файла конфигурации
                pass
        except:
            self.create_config_file()       # Создание файла конфигурации
        return self.config                  # Возвращение конфигурации

class Branches:
    """
    Класс для работы с филиалами.
    
    Аргументы:
    config_soft: конфигурация программы

    Методы:
    getBranchesName(): получение названий филиалов
    """
    def __init__(self, config_soft):
        self.config_soft = config_soft

    def getBranchesName(self)-> list:
        '''Получение названий филиалов'''

        branche_name = []

        braches = self.config_soft['BRANCHES']
        for branch in braches:
            branche_name.append(braches[branch])

        return branche_name

class XML:
    """
    Класс для работы с xml файлами.
    
    Аргументы:
    config_soft: конфигурация программы

    Методы:
    autofind_xml(): автоматическое сопоставление имя файлов с названиями филиалов
    """
    def __init__(self, config_soft):
        self.config_soft = config_soft

    def autofind_xml(self, branches: list, path: list, year: int = 2025, month: str = '1.Январь')-> list:
        '''Автовыбор (сопоставление) имён файлов с названиями филиалов'''
        
        files = os.listdir(f'{path}/{year}/{month}/')           # Получаем список файлов в папке

        xml_files = []                                          # Список xml файлов

        # Сопоставуляем файлы с названиями ветвей
        for file in files:
            find_file = file.lower()
            for branch in branches:
                if re.search(r'\d.* ' + branch.lower() + '.xml', find_file):
                    xml_files.append(f'{branch}:{file}')        # Добавляем в список xml файлов филиал и его файл (Филиал:Файл)

        return xml_files

class Folder:
    def __init__ (self):
        self.current_year = datetime.datetime.now().year
    
    def create_folder(self, term: int = 0)->None:
        '''Создание папки года (по умолчанию текущего) и создание в этой папке ещё папки с месяцами'''
        os.mkdir(f'./files/{self.current_year, term}/')
        os.mkdir(f'./files/{self.current_year, term}/1.Январь/')
        os.mkdir(f'./files/{self.current_year, term}/2.Февраль/')
        os.mkdir(f'./files/{self.current_year, term}/3.Март/')
        os.mkdir(f'./files/{self.current_year, term}/4.Апрель/')
        os.mkdir(f'./files/{self.current_year, term}/5.Май/')
        os.mkdir(f'./files/{self.current_year, term}/6.Июнь/')
        os.mkdir(f'./files/{self.current_year, term}/7.Июль/')
        os.mkdir(f'./files/{self.current_year, term}/8.Август/')
        os.mkdir(f'./files/{self.current_year, term}/9.Сентябрь/')
        os.mkdir(f'./files/{self.current_year, term}/10Октябрь/')
        os.mkdir(f'./files/{self.current_year, term}/11Ноябрь/')
        os.mkdir(f'./files/{self.current_year, term}/12Декабрь/')