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

    ui.resistorCategorySignal.connect(dkAccess.onResistorCategoryChanged)
    ui.inStockCheckboxSignal.connect(dkAccess.onInStockSelectionChanged)
    ui.relationInputSignal.connect(dkAccess.onRelationInputChanged)
    ui.approxValueSignal.connect(dkAccess.onApproxValueInputChanged)
    ui.doesNotMatterButtonSignal.connect(dkAccess.onDoesNotMatterButtonToggled)
    ui.searchSignal.connect(dkAccess.onSearchInitiated)

    sys.exit(app.exec())

main()