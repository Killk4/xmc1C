import sys
import AccHelper
import ui.main_ui as mui
from PyQt5 import QtWidgets

config_soft = AccHelper.Config().read_config_file()
xml = AccHelper.XML(config_soft)
branches = AccHelper.Branches(config_soft)

# result = xml.autofind_xml(branches.getBranchesName(), config_soft['SETTINGS']['months_path'])
# print(result)

app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()

main_ui = mui.Ui_MainWindow(month_default=3,
                       font=config_soft['SETTINGS']['font_family'],
                       font_size=int(config_soft['SETTINGS']['font_size']))

main_ui.setupUi(MainWindow)
MainWindow.show()

sys.exit(app.exec_())