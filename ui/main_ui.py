from PyQt5 import QtCore, QtGui, QtWidgets
from datetime import datetime
import re
import AccHelper
import replaceUZiZP
import time

from PyQt5.QtCore import QThread
from replaceUZiZP import ReplaceThread


config_soft = AccHelper.Config().read_config_file() # Чтение фала конфигурации
xml = AccHelper.XML(config_soft)                    # Объект работы с XML
branches = AccHelper.Branches(config_soft)          # Объект работы с филиалами
rp = replaceUZiZP.replace(path=config_soft['SETTINGS']['months_path'])


class Ui_MainWindow(object):

    def __init__(self, font: str = "Tahoma", font_size: int = 14, month_default: int = 4, files_path = ""):
        self.font = font
        self.font_size = font_size
        self.month_default = month_default - 1
        self.files_path = files_path
        self.log_text = "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
        "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
        "p, li { white-space: pre-wrap; }\n"
        "</style></head><body style=\" font-family:\'Tahoma\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
        self.replace_thread = None
        self.rp = None
        self.start_time = time.time()
        self.end_time = time.time()

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(882, 520)
        MainWindow.setMinimumSize(QtCore.QSize(882, 520))
        MainWindow.setMaximumSize(QtCore.QSize(882, 520))
        font = QtGui.QFont()
        font.setFamily(self.font)
        font.setPointSize(10)
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(12, 0, 861, 472))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.processView = QtWidgets.QTextBrowser(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily(self.font)
        self.processView.setFont(font)
        self.processView.setObjectName("processView")
        self.horizontalLayout_13.addWidget(self.processView)
        self.verticalLayout_2.addLayout(self.horizontalLayout_13)
        self.horizontalLayout_14 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_14.setObjectName("horizontalLayout_14")
        self.autofind_btn = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily(self.font)
        font.setPointSize(self.font_size)
        self.autofind_btn.setFont(font)
        self.autofind_btn.setObjectName("autofind_btn")
        self.horizontalLayout_14.addWidget(self.autofind_btn)
        self.start_btn = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily(self.font)
        font.setPointSize(self.font_size)
        self.start_btn.setFont(font)
        self.start_btn.setObjectName("start_btn")
        self.horizontalLayout_14.addWidget(self.start_btn)
        self.verticalLayout_2.addLayout(self.horizontalLayout_14)
        self.progressBar = QtWidgets.QProgressBar(self.verticalLayoutWidget_2)
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        self.verticalLayout_2.addWidget(self.progressBar)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 882, 22))
        self.menubar.setObjectName("menubar")
        self.settings_menu = QtWidgets.QMenu(self.menubar)
        self.settings_menu.setObjectName("settings_menu")
        self.manual_menu = QtWidgets.QMenu(self.menubar)
        self.manual_menu.setObjectName("manual_menu")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.settings_action = QtWidgets.QAction(MainWindow)
        self.settings_action.setObjectName("settings_action")
        self.about_action = QtWidgets.QAction(MainWindow)
        self.about_action.setObjectName("about_action")
        self.checkUpdate_action = QtWidgets.QAction(MainWindow)
        self.checkUpdate_action.setObjectName("checkUpdate_action")
        self.settings_menu.addAction(self.settings_action)
        self.manual_menu.addAction(self.about_action)
        self.manual_menu.addAction(self.checkUpdate_action)
        self.menubar.addAction(self.settings_menu.menuAction())
        self.menubar.addAction(self.manual_menu.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "xml editor"))
        self.processView.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Tahoma\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"))
        self.autofind_btn.setText(_translate("MainWindow", "Найти файлы"))
        self.start_btn.setText(_translate("MainWindow", "Запуск"))
        self.settings_menu.setTitle(_translate("MainWindow", "Настройки"))
        self.manual_menu.setTitle(_translate("MainWindow", "Справка"))
        self.settings_action.setText(_translate("MainWindow", "Параметры"))
        self.about_action.setText(_translate("MainWindow", "О программе"))
        self.checkUpdate_action.setText(_translate("MainWindow", "Проверить обновление"))


    # Функция логирования действий
    def logs(self, text: str)->None:
        current_time = datetime.now().time()
        self.log_text = (
                            f"{self.log_text}"
                            f"<p style='margin:0; -qt-block-indent:0; text-indent:0px;'>"
                            f"<span style='font-family:\"MS Shell Dlg 2\"; font-size:8.25pt; color:#949494;'>"
                            f"<b>{current_time.strftime('%H:%M:%S')}</b> {text}</span></p>\n"
                        )
        if text[-1] == '%':
            self.progressBar.setProperty("value", int(text[:-1]))
            if int(text[:-1]) == 100:
                self.end_time = time.time()
                elapsed_time = self.end_time - self.start_time
                self.processView.setHtml(f'{self.log_text}Скрипт завершил работу за {str(elapsed_time)} секунд.\n')
            return None
        self.processView.setHtml(self.log_text)

    def log_progress(self, percent_text: str) -> None:
        self.logs(f"Обработка: {percent_text}")

    # Выбор имени филиала из всего имени файла
    def splitShortName(self, file_name: str)->str:
        pattern = r"([^\s]+).xml$"
        return re.search(pattern, file_name).group(1)

    # Обработчик нажатия кнопки Автопоиск
    def on_autofind_btn_clicked(self):
        tmp = ''
        branch_files = xml.autofind_xml(config_soft['BRANCHES'], config_soft['SETTINGS']['months_path'])
        for file in branch_files:
            tmp = 0
            for branch in config_soft['BRANCHES']:
                if tmp == 0:
                    self.logs(f"Найден файл: {file}")
                    tmp = 1
                else:
                    continue

    # Обработчик нажатия кнопки Старт
    def on_start_btn_clicked(self):
        self.start_time = time.time()
        self.log_text = f"{self.log_text}<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; color:#949494;\"><b>_______________________________________________________________________________</b></span></p>\n"
        self.processView.setHtml(self.log_text)
        self.logs('Скрипт начал работу')

        self.replace_thread = ReplaceThread(path=config_soft['SETTINGS']['months_path'])
        self.replace_thread.progress.connect(self.logs)
        self.replace_thread.start()
