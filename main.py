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
    ui.rohsSelectionSignal.connect(dkAccess.onRohsSelectionChanged)
    ui.relationInputSignal.connect(dkAccess.onRelationInputChanged)
    ui.approxValue_R1_Signal.connect(dkAccess.onApproxValueInput_R1_Changed)
    ui.approxValue_R2_Signal.connect(dkAccess.onApproxValueInput_R2_Changed)
    ui.filtersSignal.connect(dkAccess.onFiltersClicked)

    ui.searchSignal.connect(dkAccess.onSearchInitiated)

    sys.exit(app.exec())

main()