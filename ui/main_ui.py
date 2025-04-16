from PyQt5 import QtCore, QtGui, QtWidgets
import re

class Ui_MainWindow(object):

    def __init__(self, font: str = "Tahoma", font_size: int = 14, month_default: int = 4, files_path = ""):
        self.font = font
        self.font_size = font_size
        self.month_default = month_default - 1
        self.files_path = files_path

    def setupUi(self, MainWindow):

        self.window = MainWindow

        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(882, 520)
        MainWindow.setMinimumSize(QtCore.QSize(882, 520))
        MainWindow.setMaximumSize(QtCore.QSize(882, 520))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
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
        font.setFamily("Tahoma")
        self.processView.setFont(font)
        self.processView.setObjectName("processView")
        self.horizontalLayout_13.addWidget(self.processView)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_15 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_15.setObjectName("horizontalLayout_15")
        self.month_box = QtWidgets.QComboBox(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.month_box.setFont(font)
        self.month_box.setObjectName("month_box")
        self.month_box.addItem("")
        self.month_box.addItem("")
        self.month_box.addItem("")
        self.month_box.addItem("")
        self.month_box.addItem("")
        self.month_box.addItem("")
        self.month_box.addItem("")
        self.month_box.addItem("")
        self.month_box.addItem("")
        self.month_box.addItem("")
        self.month_box.addItem("")
        self.month_box.addItem("")
        self.horizontalLayout_15.addWidget(self.month_box)
        self.year_box = QtWidgets.QComboBox(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.year_box.setFont(font)
        self.year_box.setObjectName("year_box")
        self.year_box.addItem("")
        self.year_box.addItem("")
        self.year_box.addItem("")
        self.year_box.addItem("")
        self.year_box.addItem("")
        self.year_box.addItem("")
        self.horizontalLayout_15.addWidget(self.year_box)
        self.verticalLayout.addLayout(self.horizontalLayout_15)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.JK_lable = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(14)
        self.JK_lable.setFont(font)
        self.JK_lable.setObjectName("JK_lable")
        self.horizontalLayout_5.addWidget(self.JK_lable)
        self.JK_file_label = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(14)
        self.JK_file_label.setFont(font)
        self.JK_file_label.setObjectName("JK_file_label")
        self.horizontalLayout_5.addWidget(self.JK_file_label)
        self.JK_select_btn = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.JK_select_btn.setObjectName("JK_select_btn")
        self.horizontalLayout_5.addWidget(self.JK_select_btn)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.IL_label = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(14)
        self.IL_label.setFont(font)
        self.IL_label.setObjectName("IL_label")
        self.horizontalLayout.addWidget(self.IL_label)
        self.IL_file_label = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(14)
        self.IL_file_label.setFont(font)
        self.IL_file_label.setObjectName("IL_file_label")
        self.horizontalLayout.addWidget(self.IL_file_label)
        self.IL_select_btn = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.IL_select_btn.setObjectName("IL_select_btn")
        self.horizontalLayout.addWidget(self.IL_select_btn)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.KB_label = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(14)
        self.KB_label.setFont(font)
        self.KB_label.setObjectName("KB_label")
        self.horizontalLayout_8.addWidget(self.KB_label)
        self.KB_file_label = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(14)
        self.KB_file_label.setFont(font)
        self.KB_file_label.setObjectName("KB_file_label")
        self.horizontalLayout_8.addWidget(self.KB_file_label)
        self.KB_select_btn = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.KB_select_btn.setObjectName("KB_select_btn")
        self.horizontalLayout_8.addWidget(self.KB_select_btn)
        self.verticalLayout.addLayout(self.horizontalLayout_8)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.KV_label = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(14)
        self.KV_label.setFont(font)
        self.KV_label.setObjectName("KV_label")
        self.horizontalLayout_4.addWidget(self.KV_label)
        self.KV_file_label = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(14)
        self.KV_file_label.setFont(font)
        self.KV_file_label.setObjectName("KV_file_label")
        self.horizontalLayout_4.addWidget(self.KV_file_label)
        self.KV_select_btn = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.KV_select_btn.setObjectName("KV_select_btn")
        self.horizontalLayout_4.addWidget(self.KV_select_btn)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.KP_label = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(14)
        self.KP_label.setFont(font)
        self.KP_label.setObjectName("KP_label")
        self.horizontalLayout_12.addWidget(self.KP_label)
        self.KP_file_label = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(14)
        self.KP_file_label.setFont(font)
        self.KP_file_label.setObjectName("KP_file_label")
        self.horizontalLayout_12.addWidget(self.KP_file_label)
        self.KP_select_btn = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.KP_select_btn.setObjectName("KP_select_btn")
        self.horizontalLayout_12.addWidget(self.KP_select_btn)
        self.verticalLayout.addLayout(self.horizontalLayout_12)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.NR_label = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(14)
        self.NR_label.setFont(font)
        self.NR_label.setObjectName("NR_label")
        self.horizontalLayout_6.addWidget(self.NR_label)
        self.NR_file_label = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(14)
        self.NR_file_label.setFont(font)
        self.NR_file_label.setObjectName("NR_file_label")
        self.horizontalLayout_6.addWidget(self.NR_file_label)
        self.NR_select_btn = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.NR_select_btn.setObjectName("NR_select_btn")
        self.horizontalLayout_6.addWidget(self.NR_select_btn)
        self.verticalLayout.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.PK_label = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(14)
        self.PK_label.setFont(font)
        self.PK_label.setObjectName("PK_label")
        self.horizontalLayout_7.addWidget(self.PK_label)
        self.PK_file_label = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(14)
        self.PK_file_label.setFont(font)
        self.PK_file_label.setObjectName("PK_file_label")
        self.horizontalLayout_7.addWidget(self.PK_file_label)
        self.PK_select_btn = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.PK_select_btn.setObjectName("PK_select_btn")
        self.horizontalLayout_7.addWidget(self.PK_select_btn)
        self.verticalLayout.addLayout(self.horizontalLayout_7)
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.SL_label = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(14)
        self.SL_label.setFont(font)
        self.SL_label.setObjectName("SL_label")
        self.horizontalLayout_11.addWidget(self.SL_label)
        self.SL_file_label = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(14)
        self.SL_file_label.setFont(font)
        self.SL_file_label.setObjectName("SL_file_label")
        self.horizontalLayout_11.addWidget(self.SL_file_label)
        self.SL_select_btn = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.SL_select_btn.setObjectName("SL_select_btn")
        self.horizontalLayout_11.addWidget(self.SL_select_btn)
        self.verticalLayout.addLayout(self.horizontalLayout_11)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.SK_label = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(14)
        self.SK_label.setFont(font)
        self.SK_label.setObjectName("SK_label")
        self.horizontalLayout_9.addWidget(self.SK_label)
        self.SK_file_label = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(14)
        self.SK_file_label.setFont(font)
        self.SK_file_label.setObjectName("SK_file_label")
        self.horizontalLayout_9.addWidget(self.SK_file_label)
        self.SK_select_btn = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.SK_select_btn.setObjectName("SK_select_btn")
        self.horizontalLayout_9.addWidget(self.SK_select_btn)
        self.verticalLayout.addLayout(self.horizontalLayout_9)
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.SM_label = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(14)
        self.SM_label.setFont(font)
        self.SM_label.setObjectName("SM_label")
        self.horizontalLayout_10.addWidget(self.SM_label)
        self.SM_file_label = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(14)
        self.SM_file_label.setFont(font)
        self.SM_file_label.setObjectName("SM_file_label")
        self.horizontalLayout_10.addWidget(self.SM_file_label)
        self.SM_select_btn = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.SM_select_btn.setObjectName("SM_select_btn")
        self.horizontalLayout_10.addWidget(self.SM_select_btn)
        self.verticalLayout.addLayout(self.horizontalLayout_10)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.UN_label = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(14)
        self.UN_label.setFont(font)
        self.UN_label.setObjectName("UN_label")
        self.horizontalLayout_3.addWidget(self.UN_label)
        self.UN_file_label = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(14)
        self.UN_file_label.setFont(font)
        self.UN_file_label.setObjectName("UN_file_label")
        self.horizontalLayout_3.addWidget(self.UN_file_label)
        self.UN_select_btn = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.UN_select_btn.setObjectName("UN_select_btn")
        self.horizontalLayout_3.addWidget(self.UN_select_btn)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.autofind_btn = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(14)
        self.autofind_btn.setFont(font)
        self.autofind_btn.setObjectName("autofind_btn")
        self.verticalLayout.addWidget(self.autofind_btn)
        self.horizontalLayout_13.addLayout(self.verticalLayout)
        self.verticalLayout_2.addLayout(self.horizontalLayout_13)
        self.horizontalLayout_14 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_14.setObjectName("horizontalLayout_14")
        self.check_btn = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(14)
        self.check_btn.setFont(font)
        self.check_btn.setObjectName("check_btn")
        self.horizontalLayout_14.addWidget(self.check_btn)
        self.start_btn = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(14)
        self.start_btn.setFont(font)
        self.start_btn.setObjectName("start_btn")
        self.horizontalLayout_14.addWidget(self.start_btn)
        self.verticalLayout_2.addLayout(self.horizontalLayout_14)
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
        self.month_box.setCurrentIndex(2)
        self.year_box.setCurrentIndex(5)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "xml editor"))
        self.processView.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
        "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
        "p, li { white-space: pre-wrap; }\n"
        "</style></head><body style=\" font-family:\'Tahoma\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
        "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; color:#949494;\">Прогресс ...</span></p>\n"
        "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; color:#949494;\">Данилин - основное место работы КБ</span></p>\n"
        "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; color:#949494;\">Поиск в других филиалах</span></p>\n"
        "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; color:#949494;\">Найден в ПК</span></p>\n"
        "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; color:#949494;\">Перенос в КБ</span></p>\n"
        "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; color:#949494;\">Чистка данных из ПК</span></p>\n"
        "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; color:#949494;\">...</span></p>\n"
        "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; color:#949494;\">Работа программы завершена успешно за ??? секунд.</span></p></body></html>"))
        self.month_box.setItemText(0, _translate("MainWindow", "Январь"))
        self.month_box.setItemText(1, _translate("MainWindow", "Февраль"))
        self.month_box.setItemText(2, _translate("MainWindow", "Март"))
        self.month_box.setItemText(3, _translate("MainWindow", "Апрель"))
        self.month_box.setItemText(4, _translate("MainWindow", "Май"))
        self.month_box.setItemText(5, _translate("MainWindow", "Июнь"))
        self.month_box.setItemText(6, _translate("MainWindow", "Июль"))
        self.month_box.setItemText(7, _translate("MainWindow", "Август"))
        self.month_box.setItemText(8, _translate("MainWindow", "Сентябрь"))
        self.month_box.setItemText(9, _translate("MainWindow", "Октябрь"))
        self.month_box.setItemText(10, _translate("MainWindow", "Ноябрь"))
        self.month_box.setItemText(11, _translate("MainWindow", "Декабрь"))
        self.year_box.setCurrentText(_translate("MainWindow", "2025"))
        self.year_box.setItemText(0, _translate("MainWindow", "2020"))
        self.year_box.setItemText(1, _translate("MainWindow", "2021"))
        self.year_box.setItemText(2, _translate("MainWindow", "2022"))
        self.year_box.setItemText(3, _translate("MainWindow", "2023"))
        self.year_box.setItemText(4, _translate("MainWindow", "2024"))
        self.year_box.setItemText(5, _translate("MainWindow", "2025"))
        self.JK_lable.setText(_translate("MainWindow", "ЖК"))
        self.JK_file_label.setText(_translate("MainWindow", "Не выбрано"))
        self.JK_select_btn.setText(_translate("MainWindow", "Выбрать"))
        self.IL_label.setText(_translate("MainWindow", "ил"))
        self.IL_file_label.setText(_translate("MainWindow", "Не выбрано"))
        self.IL_select_btn.setText(_translate("MainWindow", "Выбрать"))
        self.KB_label.setText(_translate("MainWindow", "КБ"))
        self.KB_file_label.setText(_translate("MainWindow", "Не выбрано"))
        self.KB_select_btn.setText(_translate("MainWindow", "Выбрать"))
        self.KV_label.setText(_translate("MainWindow", "Кирова"))
        self.KV_file_label.setText(_translate("MainWindow", "Не выбрано"))
        self.KV_select_btn.setText(_translate("MainWindow", "Выбрать"))
        self.KP_label.setText(_translate("MainWindow", "Крупской"))
        self.KP_file_label.setText(_translate("MainWindow", "Не выбрано"))
        self.KP_select_btn.setText(_translate("MainWindow", "Выбрать"))
        self.NR_label.setText(_translate("MainWindow", "Нарат"))
        self.NR_file_label.setText(_translate("MainWindow", "Не выбрано"))
        self.NR_select_btn.setText(_translate("MainWindow", "Выбрать"))
        self.PK_label.setText(_translate("MainWindow", "ПК"))
        self.PK_file_label.setText(_translate("MainWindow", "Не выбрано"))
        self.PK_select_btn.setText(_translate("MainWindow", "Выбрать"))
        self.SL_label.setText(_translate("MainWindow", "Салют"))
        self.SL_file_label.setText(_translate("MainWindow", "Не выбрано"))
        self.SL_select_btn.setText(_translate("MainWindow", "Выбрать"))
        self.SK_label.setText(_translate("MainWindow", "СКФНКЦ"))
        self.SK_file_label.setText(_translate("MainWindow", "Не выбрано"))
        self.SK_select_btn.setText(_translate("MainWindow", "Выбрать"))
        self.SM_label.setText(_translate("MainWindow", "Смена"))
        self.SM_file_label.setText(_translate("MainWindow", "Не выбрано"))
        self.SM_select_btn.setText(_translate("MainWindow", "Выбрать"))
        self.UN_label.setText(_translate("MainWindow", "Юность"))
        self.UN_file_label.setText(_translate("MainWindow", "Не выбрано"))
        self.UN_select_btn.setText(_translate("MainWindow", "Выбрать"))
        self.autofind_btn.setText(_translate("MainWindow", "Найти автоматически"))
        self.check_btn.setText(_translate("MainWindow", "Проверка"))
        self.start_btn.setText(_translate("MainWindow", "Запуск"))
        self.settings_menu.setTitle(_translate("MainWindow", "Настройки"))
        self.manual_menu.setTitle(_translate("MainWindow", "Справка"))
        self.settings_action.setText(_translate("MainWindow", "Параметры"))
        self.about_action.setText(_translate("MainWindow", "О программе"))
        self.checkUpdate_action.setText(_translate("MainWindow", "Проверить обновление"))

        ### Клики ###
        #  Выбор файла  #
        self.JK_select_btn.clicked.connect(self.on_JK_select_btn_clicked)
        self.IL_select_btn.clicked.connect(self.on_IL_select_btn_clicked)
        self.KB_select_btn.clicked.connect(self.on_KB_select_btn_clicked)
        self.KV_select_btn.clicked.connect(self.on_KV_select_btn_clicked)
        self.KP_select_btn.clicked.connect(self.on_KP_select_btn_clicked)
        self.NR_select_btn.clicked.connect(self.on_NR_select_btn_clicked)
        self.PK_select_btn.clicked.connect(self.on_PK_select_btn_clicked)
        self.SL_select_btn.clicked.connect(self.on_SL_select_btn_clicked)
        self.SK_select_btn.clicked.connect(self.on_SK_select_btn_clicked)
        self.SM_select_btn.clicked.connect(self.on_SM_select_btn_clicked)
        self.UN_select_btn.clicked.connect(self.on_UN_select_btn_clicked)

        # #  Автопоиск файлов  #
        # self.autofind_btn.clicked.connect(self.autofind_btn_clicked)

        # #  Проверка и запуск  #
        # self.check_btn.clicked.connect()
        # self.start_btn.clicked.connect()

    # Выбор имени филиала из всего имени файла
    def splitShortName(self, file_name: str)->str:
        pattern = r"([^\s]+).xml$"
        return re.search(pattern, file_name).group(1)

    # Вызов окна с выбором файла XML
    def selectXML(self, title: str = "Выбрать файл" ):
        file_name, _ = QtWidgets.QFileDialog.getOpenFileName(self.window, title, self.files_path, "XMLька(*.xml)")
        return file_name

    # Обработчик нажатия выбора файла для ЖК
    def on_JK_select_btn_clicked(self):
        file_name = self.selectXML('Выберите файл ЖК')
        if file_name:
            print("Выбран файл:", file_name)
            self.JK_SELECT = file_name

            self.JK_file_label.setText(f'{self.splitShortName(file_name)}.xml')

    # Обработчик нажатия выбора файла для ИЛ
    def on_IL_select_btn_clicked(self):
        file_name = self.selectXML('Выберите файл ИЛ')
        if file_name:
            print("Выбран файл:", file_name)
            self.IL_SELECT = file_name

            self.IL_file_label.setText(f'{self.splitShortName(file_name)}.xml')

    # Обработчик нажатия выбора файла для КБ
    def on_KB_select_btn_clicked(self):
        file_name = self.selectXML('Выберите файл КБ')
        if file_name:
            print("Выбран файл:", file_name)
            self.KB_SELECT = file_name

            self.KB_file_label.setText(f'{self.splitShortName(file_name)}.xml')

    # Обработчик нажатия выбора файла для Кирова
    def on_KV_select_btn_clicked(self):
        file_name = self.selectXML('Выберите файл Кирова')
        if file_name:
            print("Выбран файл:", file_name)
            self.KV_SELECT = file_name

            self.KV_file_label.setText(f'{self.splitShortName(file_name)}.xml')

    # Обработчик нажатия выбора файла для Крупской
    def on_KP_select_btn_clicked(self):
        file_name = self.selectXML('Выберите файл Крупской')
        if file_name:
            print("Выбран файл:", file_name)
            self.KP_SELECT = file_name

            self.KP_file_label.setText(f'{self.splitShortName(file_name)}.xml')

    # Обработчик нажатия выбора файла для Нарата
    def on_NR_select_btn_clicked(self):
        file_name = self.selectXML('Выберите файл Нарата')
        if file_name:
            print("Выбран файл:", file_name)
            self.NR_SELECT = file_name

            self.NR_file_label.setText(f'{self.splitShortName(file_name)}.xml')

    # Обработчик нажатия выбора файла для ПК
    def on_PK_select_btn_clicked(self):
        file_name = self.selectXML('Выберите файл ПК')
        if file_name:
            print("Выбран файл:", file_name)
            self.PK_SELECT = file_name

            self.PK_file_label.setText(f'{self.splitShortName(file_name)}.xml')

    # Обработчик нажатия выбора файла для Салюта
    def on_SL_select_btn_clicked(self):
        file_name = self.selectXML('Выберите файл Салюта')
        if file_name:
            print("Выбран файл:", file_name)
            self.SL_SELECT = file_name

            self.SL_file_label.setText(f'{self.splitShortName(file_name)}.xml')

    # Обработчик нажатия выбора файла для СКФНКЦ
    def on_SK_select_btn_clicked(self):
        file_name = self.selectXML('Выберите файл СКФНКЦ')
        if file_name:
            print("Выбран файл:", file_name)
            self.SK_SELECT = file_name

            self.SK_file_label.setText(f'{self.splitShortName(file_name)}.xml')

    # Обработчик нажатия выбора файла для Смены
    def on_SM_select_btn_clicked(self):
        file_name = self.selectXML('Выберите файл Смены')
        if file_name:
            print("Выбран файл:", file_name)
            self.SM_SELECT = file_name

            self.SM_file_label.setText(f'{self.splitShortName(file_name)}.xml')

    # Обработчик нажатия выбора файла для Юности
    def on_UN_select_btn_clicked(self):
        file_name = self.selectXML('Выберите файл Юности')
        if file_name:
            print("Выбран файл:", file_name)
            self.UN_SELECT = file_name

            self.UN_file_label.setText(f'{self.splitShortName(file_name)}.xml')
