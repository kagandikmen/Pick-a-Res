# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt6 UI code generator 6.7.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets
from PySide6.QtCore import QObject, Signal, Slot


class Ui_MainWindow(QObject):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1004, 665)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.resistorCategoriesList = QtWidgets.QListWidget(parent=self.centralwidget)
        self.resistorCategoriesList.setGeometry(QtCore.QRect(20, 50, 240, 125))
        self.resistorCategoriesList.setSelectionMode(QtWidgets.QAbstractItemView.SelectionMode.SingleSelection)
        self.resistorCategoriesList.setObjectName("resistorCategoriesList")
        item = QtWidgets.QListWidgetItem()
        self.resistorCategoriesList.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.resistorCategoriesList.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.resistorCategoriesList.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.resistorCategoriesList.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.resistorCategoriesList.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.resistorCategoriesList.addItem(item)
        self.resistorCategoriesLabel = QtWidgets.QLabel(parent=self.centralwidget)
        self.resistorCategoriesLabel.setGeometry(QtCore.QRect(20, 20, 151, 20))
        self.resistorCategoriesLabel.setObjectName("resistorCategoriesLabel")
        self.inStockCheckBox = QtWidgets.QCheckBox(parent=self.centralwidget)
        self.inStockCheckBox.setGeometry(QtCore.QRect(30, 190, 93, 26))
        self.inStockCheckBox.setChecked(True)
        self.inStockCheckBox.setObjectName("inStockCheckBox")
        self.relationInputBox = QtWidgets.QDoubleSpinBox(parent=self.centralwidget)
        self.relationInputBox.setGeometry(QtCore.QRect(20, 290, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.relationInputBox.setFont(font)
        self.relationInputBox.setObjectName("relationInputBox")
        self.relationInputLabel = QtWidgets.QLabel(parent=self.centralwidget)
        self.relationInputLabel.setGeometry(QtCore.QRect(20, 260, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.relationInputLabel.setFont(font)
        self.relationInputLabel.setObjectName("relationInputLabel")
        self.approxValueTextInput_R1 = QtWidgets.QPlainTextEdit(parent=self.centralwidget)
        self.approxValueTextInput_R1.setGeometry(QtCore.QRect(80, 380, 181, 41))
        self.approxValueTextInput_R1.setObjectName("approxValueTextInput_R1")
        self.approxValueLabel = QtWidgets.QLabel(parent=self.centralwidget)
        self.approxValueLabel.setGeometry(QtCore.QRect(20, 350, 201, 20))
        self.approxValueLabel.setObjectName("approxValueLabel")
        self.rohsCompliantCheckBox = QtWidgets.QCheckBox(parent=self.centralwidget)
        self.rohsCompliantCheckBox.setGeometry(QtCore.QRect(30, 220, 151, 26))
        self.rohsCompliantCheckBox.setObjectName("rohsCompliantCheckBox")
        self.searchButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.searchButton.setGeometry(QtCore.QRect(20, 570, 240, 41))
        self.searchButton.setObjectName("searchButton")
        self.filtersButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.filtersButton.setGeometry(QtCore.QRect(20, 510, 111, 29))
        self.filtersButton.setObjectName("filtersButton")
        self.resultsLabel = QtWidgets.QLabel(parent=self.centralwidget)
        self.resultsLabel.setGeometry(QtCore.QRect(280, 20, 151, 20))
        self.resultsLabel.setObjectName("resultsLabel")
        self.resultsTable = QtWidgets.QTableWidget(parent=self.centralwidget)
        self.resultsTable.setEnabled(True)
        self.resultsTable.setGeometry(QtCore.QRect(280, 50, 700, 560))
        self.resultsTable.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.SizeAdjustPolicy.AdjustIgnored)
        self.resultsTable.setShowGrid(True)
        self.resultsTable.setGridStyle(QtCore.Qt.PenStyle.SolidLine)
        self.resultsTable.setObjectName("resultsTable")
        self.resultsTable.setColumnCount(2)
        self.resultsTable.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.resultsTable.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.resultsTable.setHorizontalHeaderItem(1, item)
        self.resultsTable.horizontalHeader().setVisible(True)
        self.resultsTable.horizontalHeader().setCascadingSectionResizes(False)
        self.resultsTable.horizontalHeader().setDefaultSectionSize(349)
        self.resultsTable.horizontalHeader().setMinimumSectionSize(43)
        self.approxValueTextInput_R2 = QtWidgets.QPlainTextEdit(parent=self.centralwidget)
        self.approxValueTextInput_R2.setGeometry(QtCore.QRect(80, 430, 181, 41))
        self.approxValueTextInput_R2.setObjectName("approxValueTextInput_R2")
        self.R1_Label = QtWidgets.QLabel(parent=self.centralwidget)
        self.R1_Label.setGeometry(QtCore.QRect(20, 390, 41, 20))
        self.R1_Label.setObjectName("R1_Label")
        self.L2_Label = QtWidgets.QLabel(parent=self.centralwidget)
        self.L2_Label.setGeometry(QtCore.QRect(20, 440, 41, 20))
        self.L2_Label.setObjectName("L2_Label")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1004, 25))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

    	#####
        self.resistorCategoriesList.itemSelectionChanged.connect(self.resistorCategoryChanged)
        self.inStockCheckBox.stateChanged.connect(self.inStockSelectionChanged)
        self.rohsCompliantCheckBox.stateChanged.connect(self.rohsSelectionChanged)
        self.relationInputBox.valueChanged.connect(self.relationInputChanged)
        self.approxValueTextInput_R1.textChanged.connect(self.approxValueInput_R1_Changed)
        self.approxValueTextInput_R2.textChanged.connect(self.approxValueInput_R2_Changed)
        self.filtersButton.clicked.connect(self.filtersClicked)
        self.searchButton.clicked.connect(self.searchInitiated)
        self.newApproxValueAtR1 = False
        self.newApproxValueAtR2 = False

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        __sortingEnabled = self.resistorCategoriesList.isSortingEnabled()
        self.resistorCategoriesList.setSortingEnabled(False)
        item = self.resistorCategoriesList.item(0)
        item.setText(_translate("MainWindow", "Chassis Mount Resistors"))
        item = self.resistorCategoriesList.item(1)
        item.setText(_translate("MainWindow", "Chip Resistor - Surface Mount"))
        item = self.resistorCategoriesList.item(2)
        item.setText(_translate("MainWindow", "Precision Trimmed Resistors"))
        item = self.resistorCategoriesList.item(3)
        item.setText(_translate("MainWindow", "Resistor Networks - Arrays"))
        item = self.resistorCategoriesList.item(4)
        item.setText(_translate("MainWindow", "Specialized Resistors"))
        item = self.resistorCategoriesList.item(5)
        item.setText(_translate("MainWindow", "Through Hole Resistors"))
        self.resistorCategoriesList.setSortingEnabled(__sortingEnabled)
        self.resistorCategoriesLabel.setText(_translate("MainWindow", "Resistor Categories"))
        self.inStockCheckBox.setText(_translate("MainWindow", "In Stock"))
        self.relationInputLabel.setText(_translate("MainWindow", "Voltage Ratio"))
        self.approxValueLabel.setText(_translate("MainWindow", "Approx. value for resistances"))
        self.rohsCompliantCheckBox.setText(_translate("MainWindow", "RoHS Compliant"))
        self.searchButton.setText(_translate("MainWindow", "Search"))
        self.filtersButton.setText(_translate("MainWindow", "Filters"))
        self.resultsLabel.setText(_translate("MainWindow", "Results"))
        item = self.resultsTable.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "First Resistor"))
        item = self.resultsTable.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Second Resistor"))
        self.R1_Label.setText(_translate("MainWindow", "R1 = "))
        self.L2_Label.setText(_translate("MainWindow", "R2 = "))

    #####
    resistorCategorySignal = Signal(int)
    
    def resistorCategoryChanged(self):
    
        sel = self.resistorCategoriesList.selectedItems()[0]
        match sel.text():
            case 'Chassis Mount Resistors':
                self.resistorCategorySignal.emit(54)
            case 'Chip Resistor - Surface Mount':
                self.resistorCategorySignal.emit(52)
            case 'Precision Trimmed Resistors':
                self.resistorCategorySignal.emit(56)
            case 'Resistor Networks - Arrays':
                self.resistorCategorySignal.emit(50)
            case 'Specialized Resistors':
                self.resistorCategorySignal.emit(55)
            case 'Through Hole Resistors':
                self.resistorCategorySignal.emit(53)
            case _:
                self.resistorCategorySignal.emit(0)

    #####
    inStockCheckboxSignal = Signal(bool)

    def inStockSelectionChanged(self):
        
        sel = self.inStockCheckBox.isChecked()
        self.inStockCheckboxSignal.emit(sel)

    #####
    rohsSelectionSignal = Signal(bool)
    
    def rohsSelectionChanged(self):

        self.rohsSelectionSignal.emit(self.rohsCompliantCheckBox.isChecked())

    #####
    relationInputSignal = Signal(float)

    def relationInputChanged(self):

        self.relationInputSignal.emit(self.relationInputBox.value())


    #####
    approxValue_R1_Signal = Signal(str)
    approxValue_R2_Signal = Signal(str)

    def approxValueInput_R1_Changed(self):
        self.newApproxValueAtR1 = True
        if (self.newApproxValueAtR2 == False):
            self.approxValueTextInput_R2.clear()
        self.approxValue_R1_Signal.emit(self.approxValueTextInput_R1.copy())
        self.newApproxValueAtR1 = False

    def approxValueInput_R2_Changed(self):
        self.newApproxValueAtR2 = True
        if (self.newApproxValueAtR1 == False):
            self.approxValueTextInput_R1.clear()
        self.approxValue_R2_Signal.emit(self.approxValueTextInput_R2.copy())
        self.newApproxValueAtR2 = False


    #####
    searchSignal = Signal()
    
    def searchInitiated(self):

        self.searchSignal.emit()

    #####
    filtersSignal = Signal()
    
    def filtersClicked(self):

        self.filtersSignal.emit()



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
