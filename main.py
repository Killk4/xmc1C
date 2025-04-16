import sys
import AccHelper
import ui.main_ui as mui
from PyQt5 import QtWidgets

config_soft = AccHelper.Config().read_config_file() # Чтение фала конфигурации
xml = AccHelper.XML(config_soft)                    # Объект работы с XML
branches = AccHelper.Branches(config_soft)          # Объект работы с филиалами

app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()

# Инициализация главного окна
main_ui = mui.Ui_MainWindow(month_default=3,
                       font=config_soft['SETTINGS']['font_family'],
                       font_size=int(config_soft['SETTINGS']['font_size']),
                       files_path=config_soft['SETTINGS']['months_path'])

# Инициализация элементов формы
main_ui.setupUi(MainWindow)

### Клики ###
#  Выбор файла  #
main_ui.JK_select_btn.clicked.connect(main_ui.on_JK_select_btn_clicked) # Железноводская клиника
main_ui.IL_select_btn.clicked.connect(main_ui.on_IL_select_btn_clicked) # Испытательная лаборатория?
main_ui.KB_select_btn.clicked.connect(main_ui.on_KB_select_btn_clicked) # Клиническая больница № 101
main_ui.KV_select_btn.clicked.connect(main_ui.on_KV_select_btn_clicked) # Санаторий им. Кирова
main_ui.KP_select_btn.clicked.connect(main_ui.on_KP_select_btn_clicked) # Санаторий им. Крупской
main_ui.NR_select_btn.clicked.connect(main_ui.on_NR_select_btn_clicked) # Санаторий Нарат
main_ui.PK_select_btn.clicked.connect(main_ui.on_PK_select_btn_clicked) # Пятигорская Клиника
main_ui.SL_select_btn.clicked.connect(main_ui.on_SL_select_btn_clicked) # Санаторий Салют
main_ui.SK_select_btn.clicked.connect(main_ui.on_SK_select_btn_clicked) # СКФНКЦ
main_ui.SM_select_btn.clicked.connect(main_ui.on_SM_select_btn_clicked) # Санаторий Смена
main_ui.UN_select_btn.clicked.connect(main_ui.on_UN_select_btn_clicked) # Медицинский центр Юность

# #  Автопоиск файлов  #
main_ui.autofind_btn.clicked.connect(main_ui.on_autofind_btn_clicked)   # "Найти автоматически"

# #  Проверка и запуск  #
main_ui.check_btn.clicked.connect(main_ui.on_check_btn_clicked)         # "Проверка"
main_ui.start_btn.clicked.connect(main_ui.on_start_btn_clicked)         # "Запуск"

# Вывести форму
MainWindow.show()

sys.exit(app.exec_())