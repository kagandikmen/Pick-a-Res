from PyQt6 import QtCore, QtGui, QtWidgets
from PySide6.QtCore import QObject, Signal, Slot
from mainwindow import Ui_MainWindow
from src.apiaccess import ApiAccess
import sys

def main():

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()

    dkAccess = ApiAccess()
    dkAccess.access()

    ui.resistorCategorySignal.connect(dkAccess.onResistorCategorySignal)

    sys.exit(app.exec())

main()