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



#  Клики  #
main_ui.autofind_btn.clicked.connect(main_ui.on_autofind_btn_clicked)   # "Найти автоматически"
main_ui.start_btn.clicked.connect(main_ui.on_start_btn_clicked)         # "Запуск"

# Вывести форму
MainWindow.show()

sys.exit(app.exec_())