# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'isoi_window_V2.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1013, 694)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(10, 10, 791, 621))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.label = QtWidgets.QLabel(self.tab)
        self.label.setGeometry(QtCore.QRect(30, 10, 151, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.layoutWidget = QtWidgets.QWidget(self.tab)
        self.layoutWidget.setGeometry(QtCore.QRect(32, 102, 721, 26))
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
        self.bitBox = QtWidgets.QComboBox(self.layoutWidget)
        self.bitBox.setObjectName("bitBox")
        self.horizontalLayout.addWidget(self.bitBox)
        self.label_3 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout.addWidget(self.label_3)
        self.binBox = QtWidgets.QComboBox(self.layoutWidget)
        self.binBox.setObjectName("binBox")
        self.horizontalLayout.addWidget(self.binBox)
        self.label_13 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_13.setFont(font)
        self.label_13.setObjectName("label_13")
        self.horizontalLayout.addWidget(self.label_13)
        self.shutBox = QtWidgets.QComboBox(self.layoutWidget)
        self.shutBox.setObjectName("shutBox")
        self.horizontalLayout.addWidget(self.shutBox)
        self.layoutWidget1 = QtWidgets.QWidget(self.tab)
        self.layoutWidget1.setGeometry(QtCore.QRect(270, 130, 484, 30))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_14 = QtWidgets.QLabel(self.layoutWidget1)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_14.setFont(font)
        self.label_14.setObjectName("label_14")
        self.horizontalLayout_2.addWidget(self.label_14)
        self.triggerBox = QtWidgets.QComboBox(self.layoutWidget1)
        self.triggerBox.setObjectName("triggerBox")
        self.horizontalLayout_2.addWidget(self.triggerBox)
        self.trigBtn = QtWidgets.QPushButton(self.layoutWidget1)
        self.trigBtn.setObjectName("trigBtn")
        self.horizontalLayout_2.addWidget(self.trigBtn)
        self.label_18 = QtWidgets.QLabel(self.layoutWidget1)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_18.setFont(font)
        self.label_18.setObjectName("label_18")
        self.horizontalLayout_2.addWidget(self.label_18)
        self.overLapBox = QtWidgets.QComboBox(self.layoutWidget1)
        self.overLapBox.setObjectName("overLapBox")
        self.horizontalLayout_2.addWidget(self.overLapBox)
        self.label_17 = QtWidgets.QLabel(self.tab)
        self.label_17.setGeometry(QtCore.QRect(30, 250, 181, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_17.setFont(font)
        self.label_17.setObjectName("label_17")
        self.layoutWidget_2 = QtWidgets.QWidget(self.tab)
        self.layoutWidget_2.setGeometry(QtCore.QRect(30, 300, 301, 191))
        self.layoutWidget_2.setObjectName("layoutWidget_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.layoutWidget_2)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_11 = QtWidgets.QLabel(self.layoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.gridLayout_2.addWidget(self.label_11, 0, 0, 1, 1)
        self.name = QtWidgets.QLineEdit(self.layoutWidget_2)
        self.name.setObjectName("name")
        self.gridLayout_2.addWidget(self.name, 0, 2, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.layoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.gridLayout_2.addWidget(self.label_4, 1, 0, 1, 2)
        self.dur = QtWidgets.QDoubleSpinBox(self.layoutWidget_2)
        self.dur.setObjectName("dur")
        self.gridLayout_2.addWidget(self.dur, 1, 2, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.layoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.gridLayout_2.addWidget(self.label_5, 2, 0, 1, 1)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.label_6 = QtWidgets.QLabel(self.layoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 0, 0, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.layoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.gridLayout.addWidget(self.label_8, 1, 0, 1, 1)
        self.label_9 = QtWidgets.QLabel(self.layoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.gridLayout.addWidget(self.label_9, 2, 0, 1, 1)
        self.gRatio = QtWidgets.QSpinBox(self.layoutWidget_2)
        self.gRatio.setObjectName("gRatio")
        self.gridLayout.addWidget(self.gRatio, 0, 1, 1, 1)
        self.rRatio = QtWidgets.QSpinBox(self.layoutWidget_2)
        self.rRatio.setObjectName("rRatio")
        self.gridLayout.addWidget(self.rRatio, 1, 1, 1, 1)
        self.bRatio = QtWidgets.QSpinBox(self.layoutWidget_2)
        self.bRatio.setObjectName("bRatio")
        self.gridLayout.addWidget(self.bRatio, 2, 1, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 2, 1, 1, 2)
        self.layoutWidget_3 = QtWidgets.QWidget(self.tab)
        self.layoutWidget_3.setGeometry(QtCore.QRect(500, 380, 253, 129))
        self.layoutWidget_3.setObjectName("layoutWidget_3")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget_3)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_16 = QtWidgets.QLabel(self.layoutWidget_3)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_16.setFont(font)
        self.label_16.setObjectName("label_16")
        self.horizontalLayout_3.addWidget(self.label_16)
        self.ledTrigBox = QtWidgets.QComboBox(self.layoutWidget_3)
        self.ledTrigBox.setObjectName("ledTrigBox")
        self.horizontalLayout_3.addWidget(self.ledTrigBox)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.SaveEBtn = QtWidgets.QPushButton(self.layoutWidget_3)
        self.SaveEBtn.setObjectName("SaveEBtn")
        self.verticalLayout.addWidget(self.SaveEBtn)
        self.abortBtn = QtWidgets.QPushButton(self.layoutWidget_3)
        self.abortBtn.setObjectName("abortBtn")
        self.verticalLayout.addWidget(self.abortBtn)
        self.progressBar = QtWidgets.QProgressBar(self.layoutWidget_3)
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName("progressBar")
        self.verticalLayout.addWidget(self.progressBar)
        self.layoutWidget_4 = QtWidgets.QWidget(self.tab)
        self.layoutWidget_4.setGeometry(QtCore.QRect(500, 320, 251, 55))
        self.layoutWidget_4.setObjectName("layoutWidget_4")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.layoutWidget_4)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.label_12 = QtWidgets.QLabel(self.layoutWidget_4)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")
        self.gridLayout_3.addWidget(self.label_12, 0, 0, 1, 1)
        self.fileSize = QtWidgets.QDoubleSpinBox(self.layoutWidget_4)
        self.fileSize.setObjectName("fileSize")
        self.gridLayout_3.addWidget(self.fileSize, 0, 1, 1, 1)
        self.label_10 = QtWidgets.QLabel(self.layoutWidget_4)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.gridLayout_3.addWidget(self.label_10, 1, 0, 1, 1)
        self.framesPerFileLabel = QtWidgets.QLabel(self.layoutWidget_4)
        self.framesPerFileLabel.setObjectName("framesPerFileLabel")
        self.gridLayout_3.addWidget(self.framesPerFileLabel, 1, 1, 1, 1)
        self.layoutWidget_5 = QtWidgets.QWidget(self.tab)
        self.layoutWidget_5.setGeometry(QtCore.QRect(420, 200, 261, 24))
        self.layoutWidget_5.setObjectName("layoutWidget_5")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.layoutWidget_5)
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_15 = QtWidgets.QLabel(self.layoutWidget_5)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_15.setFont(font)
        self.label_15.setObjectName("label_15")
        self.horizontalLayout_7.addWidget(self.label_15)
        self.expRatio = QtWidgets.QDoubleSpinBox(self.layoutWidget_5)
        self.expRatio.setObjectName("expRatio")
        self.horizontalLayout_7.addWidget(self.expRatio)
        self.layoutWidget2 = QtWidgets.QWidget(self.tab)
        self.layoutWidget2.setGeometry(QtCore.QRect(470, 10, 281, 71))
        self.layoutWidget2.setObjectName("layoutWidget2")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.layoutWidget2)
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.expLabel = QtWidgets.QLabel(self.layoutWidget2)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.expLabel.setFont(font)
        self.expLabel.setObjectName("expLabel")
        self.gridLayout_4.addWidget(self.expLabel, 0, 0, 1, 1)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.expSlider = QtWidgets.QSlider(self.layoutWidget2)
        self.expSlider.setOrientation(QtCore.Qt.Horizontal)
        self.expSlider.setObjectName("expSlider")
        self.horizontalLayout_4.addWidget(self.expSlider)
        self.C_expSb = QtWidgets.QDoubleSpinBox(self.layoutWidget2)
        self.C_expSb.setObjectName("C_expSb")
        self.horizontalLayout_4.addWidget(self.C_expSb)
        self.gridLayout_4.addLayout(self.horizontalLayout_4, 0, 1, 1, 2)
        self.expLabel_2 = QtWidgets.QLabel(self.layoutWidget2)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.expLabel_2.setFont(font)
        self.expLabel_2.setObjectName("expLabel_2")
        self.gridLayout_4.addWidget(self.expLabel_2, 1, 0, 1, 2)
        self.realExp = QtWidgets.QLabel(self.layoutWidget2)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.realExp.setFont(font)
        self.realExp.setText("")
        self.realExp.setObjectName("realExp")
        self.gridLayout_4.addWidget(self.realExp, 1, 2, 1, 1)
        self.layoutWidget3 = QtWidgets.QWidget(self.tab)
        self.layoutWidget3.setGeometry(QtCore.QRect(30, 50, 395, 30))
        self.layoutWidget3.setObjectName("layoutWidget3")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.layoutWidget3)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.histoBtn = QtWidgets.QPushButton(self.layoutWidget3)
        self.histoBtn.setObjectName("histoBtn")
        self.horizontalLayout_5.addWidget(self.histoBtn)
        self.cropBtn = QtWidgets.QPushButton(self.layoutWidget3)
        self.cropBtn.setObjectName("cropBtn")
        self.horizontalLayout_5.addWidget(self.cropBtn)
        self.loadBtn = QtWidgets.QPushButton(self.layoutWidget3)
        self.loadBtn.setObjectName("loadBtn")
        self.horizontalLayout_5.addWidget(self.loadBtn)
        self.unloadBtn = QtWidgets.QPushButton(self.layoutWidget3)
        self.unloadBtn.setObjectName("unloadBtn")
        self.horizontalLayout_5.addWidget(self.unloadBtn)
        self.layoutWidget4 = QtWidgets.QWidget(self.tab)
        self.layoutWidget4.setGeometry(QtCore.QRect(30, 190, 321, 41))
        self.layoutWidget4.setObjectName("layoutWidget4")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.layoutWidget4)
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_2 = QtWidgets.QLabel(self.layoutWidget4)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_6.addWidget(self.label_2)
        self.Green = QtWidgets.QCheckBox(self.layoutWidget4)
        self.Green.setObjectName("Green")
        self.horizontalLayout_6.addWidget(self.Green)
        self.Red = QtWidgets.QCheckBox(self.layoutWidget4)
        self.Red.setObjectName("Red")
        self.horizontalLayout_6.addWidget(self.Red)
        self.Blue = QtWidgets.QCheckBox(self.layoutWidget4)
        self.Blue.setObjectName("Blue")
        self.horizontalLayout_6.addWidget(self.Blue)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.tabWidget.addTab(self.tab_2, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1013, 26))
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
        self.label.setText(_translate("MainWindow", "Camera settings"))
        self.label_7.setText(_translate("MainWindow", "Bit depth :"))
        self.label_3.setText(_translate("MainWindow", "Binning :"))
        self.label_13.setText(_translate("MainWindow", "Shutter mode :"))
        self.label_14.setText(_translate("MainWindow", "Trigger mode :"))
        self.trigBtn.setText(_translate("MainWindow", "Trig"))
        self.label_18.setText(_translate("MainWindow", "Overlap :"))
        self.label_17.setText(_translate("MainWindow", "Acquisition settings"))
        self.label_11.setText(_translate("MainWindow", "Name :"))
        self.label_4.setText(_translate("MainWindow", "Duration (s) :"))
        self.label_5.setText(_translate("MainWindow", "LEDs ratio :"))
        self.label_6.setText(_translate("MainWindow", "Green"))
        self.label_8.setText(_translate("MainWindow", "Red"))
        self.label_9.setText(_translate("MainWindow", "Blue"))
        self.label_16.setText(_translate("MainWindow", "LED trigger mode :"))
        self.SaveEBtn.setText(_translate("MainWindow", "RUN AND SAVE"))
        self.abortBtn.setText(_translate("MainWindow", "ABORT"))
        self.label_12.setText(_translate("MainWindow", "Max file size (GB) :"))
        self.label_10.setText(_translate("MainWindow", "Frames per file :"))
        self.framesPerFileLabel.setText(_translate("MainWindow", "5787"))
        self.label_15.setText(_translate("MainWindow", "Interval LED ON (%exp)"))
        self.expLabel.setText(_translate("MainWindow", "Exposure :"))
        self.expLabel_2.setText(_translate("MainWindow", "Real exposure :"))
        self.histoBtn.setText(_translate("MainWindow", "Live Histogram"))
        self.cropBtn.setText(_translate("MainWindow", "Crop"))
        self.loadBtn.setText(_translate("MainWindow", "load Zyla"))
        self.unloadBtn.setText(_translate("MainWindow", "Unload Zyla"))
        self.label_2.setText(_translate("MainWindow", "LEDs"))
        self.Green.setText(_translate("MainWindow", "GREEN"))
        self.Red.setText(_translate("MainWindow", "RED"))
        self.Blue.setText(_translate("MainWindow", "BLUE"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Run and Save"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Images Analysis"))

