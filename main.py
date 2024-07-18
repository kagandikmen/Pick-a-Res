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
    
    ui.basicCriteriaSignal.connect(dkAccess.onBasicCriteriaChanged)
    ui.relationInputSignal.connect(dkAccess.onRelationInputChanged)
    ui.comboBox_R1_Signal.connect(dkAccess.onCombo_R1_Changed)
    ui.comboBox_R2_Signal.connect(dkAccess.onCombo_R2_Changed)
    ui.filtersSignal.connect(dkAccess.onFiltersClicked)
    dkAccess.resistorValuesSignal.connect(ui.onResistorValuesCalculated)
    dkAccess.resistorDataSignal.connect(ui.buildTables)

    ui.searchSignal.connect(dkAccess.onSearchInitiated)

    sys.exit(app.exec())

main()