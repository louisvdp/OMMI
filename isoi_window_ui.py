# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'isoi_window.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(799, 326)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, 10, 791, 281))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.expSlider = QtWidgets.QSlider(self.tab)
        self.expSlider.setGeometry(QtCore.QRect(400, 50, 160, 19))
        self.expSlider.setOrientation(QtCore.Qt.Horizontal)
        self.expSlider.setObjectName("expSlider")
        self.liveBtn = QtWidgets.QPushButton(self.tab)
        self.liveBtn.setGeometry(QtCore.QRect(30, 50, 75, 23))
        self.liveBtn.setObjectName("liveBtn")
        self.cropBtn = QtWidgets.QPushButton(self.tab)
        self.cropBtn.setGeometry(QtCore.QRect(210, 50, 75, 23))
        self.cropBtn.setObjectName("cropBtn")
        self.expLabel = QtWidgets.QLabel(self.tab)
        self.expLabel.setGeometry(QtCore.QRect(320, 50, 71, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.expLabel.setFont(font)
        self.expLabel.setObjectName("expLabel")
        self.histoBtn = QtWidgets.QPushButton(self.tab)
        self.histoBtn.setGeometry(QtCore.QRect(120, 50, 75, 23))
        self.histoBtn.setObjectName("histoBtn")
        self.label = QtWidgets.QLabel(self.tab)
        self.label.setGeometry(QtCore.QRect(30, 10, 151, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.C_expSb = QtWidgets.QDoubleSpinBox(self.tab)
        self.C_expSb.setGeometry(QtCore.QRect(570, 50, 62, 22))
        self.C_expSb.setObjectName("C_expSb")
        self.label_2 = QtWidgets.QLabel(self.tab)
        self.label_2.setGeometry(QtCore.QRect(40, 190, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.Green = QtWidgets.QCheckBox(self.tab)
        self.Green.setGeometry(QtCore.QRect(120, 200, 75, 17))
        self.Green.setObjectName("Green")
        self.Red = QtWidgets.QCheckBox(self.tab)
        self.Red.setGeometry(QtCore.QRect(210, 200, 75, 17))
        self.Red.setObjectName("Red")
        self.BLUE = QtWidgets.QCheckBox(self.tab)
        self.BLUE.setGeometry(QtCore.QRect(280, 200, 75, 17))
        self.BLUE.setObjectName("BLUE")
        self.layoutWidget = QtWidgets.QWidget(self.tab)
        self.layoutWidget.setGeometry(QtCore.QRect(31, 101, 352, 26))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_7 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout.addWidget(self.label_7)
        self.binBox = QtWidgets.QComboBox(self.layoutWidget)
        self.binBox.setObjectName("binBox")
        self.horizontalLayout.addWidget(self.binBox)
        self.label_3 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout.addWidget(self.label_3)
        self.bitBox = QtWidgets.QComboBox(self.layoutWidget)
        self.bitBox.setObjectName("bitBox")
        self.horizontalLayout.addWidget(self.bitBox)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.SaveEBtn = QtWidgets.QPushButton(self.tab_2)
        self.SaveEBtn.setGeometry(QtCore.QRect(570, 20, 154, 23))
        self.SaveEBtn.setObjectName("SaveEBtn")
        self.progressBar = QtWidgets.QProgressBar(self.tab_2)
        self.progressBar.setGeometry(QtCore.QRect(550, 70, 225, 21))
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName("progressBar")
        self.widget = QtWidgets.QWidget(self.tab_2)
        self.widget.setGeometry(QtCore.QRect(20, 20, 301, 191))
        self.widget.setObjectName("widget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.widget)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_11 = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.gridLayout_2.addWidget(self.label_11, 0, 0, 1, 1)
        self.name = QtWidgets.QLineEdit(self.widget)
        self.name.setObjectName("name")
        self.gridLayout_2.addWidget(self.name, 0, 2, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.gridLayout_2.addWidget(self.label_4, 1, 0, 1, 2)
        self.dur = QtWidgets.QDoubleSpinBox(self.widget)
        self.dur.setObjectName("dur")
        self.gridLayout_2.addWidget(self.dur, 1, 2, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.gridLayout_2.addWidget(self.label_5, 2, 0, 1, 1)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.label_6 = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 0, 0, 1, 1)
        self.gRatio = QtWidgets.QDoubleSpinBox(self.widget)
        self.gRatio.setObjectName("gRatio")
        self.gridLayout.addWidget(self.gRatio, 0, 1, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.gridLayout.addWidget(self.label_8, 1, 0, 1, 1)
        self.rRatio = QtWidgets.QDoubleSpinBox(self.widget)
        self.rRatio.setObjectName("rRatio")
        self.gridLayout.addWidget(self.rRatio, 1, 1, 1, 1)
        self.label_9 = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.gridLayout.addWidget(self.label_9, 2, 0, 1, 1)
        self.bRatio = QtWidgets.QDoubleSpinBox(self.widget)
        self.bRatio.setObjectName("bRatio")
        self.gridLayout.addWidget(self.bRatio, 2, 1, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 2, 1, 1, 2)
        self.tabWidget.addTab(self.tab_2, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 799, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "ISOI Software"))
        self.liveBtn.setText(_translate("MainWindow", "LIVE"))
        self.cropBtn.setText(_translate("MainWindow", "Crop"))
        self.expLabel.setText(_translate("MainWindow", "Exposure :"))
        self.histoBtn.setText(_translate("MainWindow", "Histogram"))
        self.label.setText(_translate("MainWindow", "Camera settings"))
        self.label_2.setText(_translate("MainWindow", "LEDs"))
        self.Green.setText(_translate("MainWindow", "GREEN"))
        self.Red.setText(_translate("MainWindow", "RED"))
        self.BLUE.setText(_translate("MainWindow", "BLUE"))
        self.label_7.setText(_translate("MainWindow", "Bit depth :"))
        self.label_3.setText(_translate("MainWindow", "Binning :"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Control"))
        self.SaveEBtn.setText(_translate("MainWindow", "RUN AND SAVE"))
        self.label_11.setText(_translate("MainWindow", "Name :"))
        self.label_4.setText(_translate("MainWindow", "Duration (s) :"))
        self.label_5.setText(_translate("MainWindow", "LEDs ratio :"))
        self.label_6.setText(_translate("MainWindow", "Green"))
        self.label_8.setText(_translate("MainWindow", "Red"))
        self.label_9.setText(_translate("MainWindow", "Blue"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Run and Save"))

