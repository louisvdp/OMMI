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
        MainWindow.resize(825, 573)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(10, 0, 791, 531))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.groupBox = QtWidgets.QGroupBox(self.tab)
        self.groupBox.setGeometry(QtCore.QRect(20, 20, 310, 481))
        self.groupBox.setAutoFillBackground(True)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.expLabel = QtWidgets.QLabel(self.groupBox)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.expLabel.setFont(font)
        self.expLabel.setObjectName("expLabel")
        self.gridLayout_2.addWidget(self.expLabel, 0, 0, 1, 1)
        self.realExp = QtWidgets.QLabel(self.groupBox)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.realExp.setFont(font)
        self.realExp.setText("")
        self.realExp.setObjectName("realExp")
        self.gridLayout_2.addWidget(self.realExp, 1, 3, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.approxFramerateBtn = QtWidgets.QPushButton(self.groupBox)
        self.approxFramerateBtn.setObjectName("approxFramerateBtn")
        self.horizontalLayout.addWidget(self.approxFramerateBtn)
        self.approxFramerateLabel = QtWidgets.QLabel(self.groupBox)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.approxFramerateLabel.setFont(font)
        self.approxFramerateLabel.setObjectName("approxFramerateLabel")
        self.horizontalLayout.addWidget(self.approxFramerateLabel)
        self.gridLayout_2.addLayout(self.horizontalLayout, 2, 0, 1, 3)
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.testFramerateBtn = QtWidgets.QPushButton(self.groupBox)
        self.testFramerateBtn.setObjectName("testFramerateBtn")
        self.horizontalLayout_10.addWidget(self.testFramerateBtn)
        self.testFramerateLabel = QtWidgets.QLabel(self.groupBox)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.testFramerateLabel.setFont(font)
        self.testFramerateLabel.setObjectName("testFramerateLabel")
        self.horizontalLayout_10.addWidget(self.testFramerateLabel)
        self.gridLayout_2.addLayout(self.horizontalLayout_10, 2, 3, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.groupBox)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.gridLayout_2.addWidget(self.label_7, 3, 0, 1, 1)
        self.bitBox = QtWidgets.QComboBox(self.groupBox)
        self.bitBox.setObjectName("bitBox")
        self.gridLayout_2.addWidget(self.bitBox, 3, 3, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.gridLayout_2.addWidget(self.label_3, 4, 0, 1, 1)
        self.binBox = QtWidgets.QComboBox(self.groupBox)
        self.binBox.setObjectName("binBox")
        self.gridLayout_2.addWidget(self.binBox, 4, 3, 1, 1)
        self.label_13 = QtWidgets.QLabel(self.groupBox)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_13.setFont(font)
        self.label_13.setObjectName("label_13")
        self.gridLayout_2.addWidget(self.label_13, 5, 0, 1, 2)
        self.shutBox = QtWidgets.QComboBox(self.groupBox)
        self.shutBox.setObjectName("shutBox")
        self.gridLayout_2.addWidget(self.shutBox, 5, 3, 1, 1)
        self.label_14 = QtWidgets.QLabel(self.groupBox)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_14.setFont(font)
        self.label_14.setObjectName("label_14")
        self.gridLayout_2.addWidget(self.label_14, 6, 0, 1, 2)
        self.triggerBox = QtWidgets.QComboBox(self.groupBox)
        self.triggerBox.setObjectName("triggerBox")
        self.gridLayout_2.addWidget(self.triggerBox, 6, 3, 1, 1)
        self.label_18 = QtWidgets.QLabel(self.groupBox)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_18.setFont(font)
        self.label_18.setObjectName("label_18")
        self.gridLayout_2.addWidget(self.label_18, 7, 0, 1, 1)
        self.overlapBox = QtWidgets.QComboBox(self.groupBox)
        self.overlapBox.setObjectName("overlapBox")
        self.gridLayout_2.addWidget(self.overlapBox, 7, 3, 1, 1)
        self.histoBtn = QtWidgets.QPushButton(self.groupBox)
        self.histoBtn.setObjectName("histoBtn")
        self.gridLayout_2.addWidget(self.histoBtn, 8, 0, 1, 2)
        self.cropBtn = QtWidgets.QPushButton(self.groupBox)
        self.cropBtn.setObjectName("cropBtn")
        self.gridLayout_2.addWidget(self.cropBtn, 8, 2, 1, 2)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_6.addWidget(self.label_2)
        self.Green = QtWidgets.QCheckBox(self.groupBox)
        self.Green.setObjectName("Green")
        self.horizontalLayout_6.addWidget(self.Green)
        self.Red = QtWidgets.QCheckBox(self.groupBox)
        self.Red.setObjectName("Red")
        self.horizontalLayout_6.addWidget(self.Red)
        self.Blue = QtWidgets.QCheckBox(self.groupBox)
        self.Blue.setObjectName("Blue")
        self.horizontalLayout_6.addWidget(self.Blue)
        self.gridLayout_2.addLayout(self.horizontalLayout_6, 9, 0, 1, 4)
        self.defaultSettingsBtn = QtWidgets.QPushButton(self.groupBox)
        self.defaultSettingsBtn.setObjectName("defaultSettingsBtn")
        self.gridLayout_2.addWidget(self.defaultSettingsBtn, 10, 0, 1, 2)
        self.loadBtn = QtWidgets.QPushButton(self.groupBox)
        self.loadBtn.setObjectName("loadBtn")
        self.gridLayout_2.addWidget(self.loadBtn, 11, 0, 1, 2)
        self.expLabel_2 = QtWidgets.QLabel(self.groupBox)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.expLabel_2.setFont(font)
        self.expLabel_2.setObjectName("expLabel_2")
        self.gridLayout_2.addWidget(self.expLabel_2, 1, 0, 1, 2)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.expSlider = QtWidgets.QSlider(self.groupBox)
        self.expSlider.setOrientation(QtCore.Qt.Horizontal)
        self.expSlider.setObjectName("expSlider")
        self.horizontalLayout_4.addWidget(self.expSlider)
        self.C_expSb = QtWidgets.QDoubleSpinBox(self.groupBox)
        self.C_expSb.setObjectName("C_expSb")
        self.horizontalLayout_4.addWidget(self.C_expSb)
        self.gridLayout_2.addLayout(self.horizontalLayout_4, 0, 1, 1, 3)
        self.loadSettingsFileBtn = QtWidgets.QPushButton(self.groupBox)
        self.loadSettingsFileBtn.setObjectName("loadSettingsFileBtn")
        self.gridLayout_2.addWidget(self.loadSettingsFileBtn, 10, 3, 1, 1)
        self.unloadBtn = QtWidgets.QPushButton(self.groupBox)
        self.unloadBtn.setObjectName("unloadBtn")
        self.gridLayout_2.addWidget(self.unloadBtn, 11, 3, 1, 1)
        self.label_7.raise_()
        self.bitBox.raise_()
        self.label_3.raise_()
        self.binBox.raise_()
        self.histoBtn.raise_()
        self.cropBtn.raise_()
        self.expLabel_2.raise_()
        self.expLabel.raise_()
        self.realExp.raise_()
        self.shutBox.raise_()
        self.label_13.raise_()
        self.label_14.raise_()
        self.triggerBox.raise_()
        self.overlapBox.raise_()
        self.label_18.raise_()
        self.defaultSettingsBtn.raise_()
        self.loadSettingsFileBtn.raise_()
        self.unloadBtn.raise_()
        self.loadBtn.raise_()
        self.groupBox_2 = QtWidgets.QGroupBox(self.tab)
        self.groupBox_2.setGeometry(QtCore.QRect(350, 20, 377, 470))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.groupBox_2.setFont(font)
        self.groupBox_2.setAutoFillBackground(True)
        self.groupBox_2.setObjectName("groupBox_2")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.groupBox_2)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.label_4 = QtWidgets.QLabel(self.groupBox_2)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.gridLayout_3.addWidget(self.label_4, 0, 0, 1, 1)
        self.experimentDuration = QtWidgets.QDoubleSpinBox(self.groupBox_2)
        self.experimentDuration.setObjectName("experimentDuration")
        self.gridLayout_3.addWidget(self.experimentDuration, 0, 1, 1, 1)
        self.label_15 = QtWidgets.QLabel(self.groupBox_2)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_15.setFont(font)
        self.label_15.setObjectName("label_15")
        self.gridLayout_3.addWidget(self.label_15, 0, 2, 1, 3)
        self.expRatio = QtWidgets.QDoubleSpinBox(self.groupBox_2)
        self.expRatio.setObjectName("expRatio")
        self.gridLayout_3.addWidget(self.expRatio, 0, 5, 1, 1)
        self.rgbMode = QtWidgets.QCheckBox(self.groupBox_2)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.rgbMode.setFont(font)
        self.rgbMode.setObjectName("rgbMode")
        self.gridLayout_3.addWidget(self.rgbMode, 1, 0, 1, 2)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.label_6 = QtWidgets.QLabel(self.groupBox_2)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 0, 0, 1, 1)
        self.gRatio = QtWidgets.QSpinBox(self.groupBox_2)
        self.gRatio.setObjectName("gRatio")
        self.gridLayout.addWidget(self.gRatio, 0, 1, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.groupBox_2)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.gridLayout.addWidget(self.label_8, 1, 0, 1, 1)
        self.rRatio = QtWidgets.QSpinBox(self.groupBox_2)
        self.rRatio.setObjectName("rRatio")
        self.gridLayout.addWidget(self.rRatio, 1, 1, 1, 1)
        self.label_9 = QtWidgets.QLabel(self.groupBox_2)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.gridLayout.addWidget(self.label_9, 2, 0, 1, 1)
        self.bRatio = QtWidgets.QSpinBox(self.groupBox_2)
        self.bRatio.setObjectName("bRatio")
        self.gridLayout.addWidget(self.bRatio, 2, 1, 1, 1)
        self.gridLayout_3.addLayout(self.gridLayout, 1, 4, 1, 1)
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.rbMode = QtWidgets.QCheckBox(self.groupBox_2)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.rbMode.setFont(font)
        self.rbMode.setObjectName("rbMode")
        self.horizontalLayout_11.addWidget(self.rbMode)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.label_20 = QtWidgets.QLabel(self.groupBox_2)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_20.setFont(font)
        self.label_20.setObjectName("label_20")
        self.horizontalLayout_9.addWidget(self.label_20)
        self.gInterval = QtWidgets.QSpinBox(self.groupBox_2)
        self.gInterval.setMaximum(10000)
        self.gInterval.setObjectName("gInterval")
        self.horizontalLayout_9.addWidget(self.gInterval)
        self.verticalLayout_2.addLayout(self.horizontalLayout_9)
        self.rbColorBox = QtWidgets.QComboBox(self.groupBox_2)
        self.rbColorBox.setMinimumSize(QtCore.QSize(247, 0))
        self.rbColorBox.setObjectName("rbColorBox")
        self.verticalLayout_2.addWidget(self.rbColorBox)
        self.horizontalLayout_11.addLayout(self.verticalLayout_2)
        self.gridLayout_3.addLayout(self.horizontalLayout_11, 2, 0, 1, 6)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_19 = QtWidgets.QLabel(self.groupBox_2)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_19.setFont(font)
        self.label_19.setObjectName("label_19")
        self.horizontalLayout_5.addWidget(self.label_19)
        self.savingPath = QtWidgets.QLineEdit(self.groupBox_2)
        self.savingPath.setObjectName("savingPath")
        self.horizontalLayout_5.addWidget(self.savingPath)
        self.savingPathBtn = QtWidgets.QPushButton(self.groupBox_2)
        self.savingPathBtn.setObjectName("savingPathBtn")
        self.horizontalLayout_5.addWidget(self.savingPathBtn)
        self.gridLayout_3.addLayout(self.horizontalLayout_5, 3, 0, 1, 6)
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.label_11 = QtWidgets.QLabel(self.groupBox_2)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.horizontalLayout_12.addWidget(self.label_11)
        self.experimentName = QtWidgets.QLineEdit(self.groupBox_2)
        self.experimentName.setObjectName("experimentName")
        self.horizontalLayout_12.addWidget(self.experimentName)
        self.gridLayout_3.addLayout(self.horizontalLayout_12, 4, 0, 1, 4)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_10 = QtWidgets.QLabel(self.groupBox_2)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.horizontalLayout_7.addWidget(self.label_10)
        self.framePerFileBox = QtWidgets.QSpinBox(self.groupBox_2)
        self.framePerFileBox.setMaximum(10000)
        self.framePerFileBox.setProperty("value", 512)
        self.framePerFileBox.setObjectName("framePerFileBox")
        self.horizontalLayout_7.addWidget(self.framePerFileBox)
        self.gridLayout_3.addLayout(self.horizontalLayout_7, 5, 0, 1, 3)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.label_12 = QtWidgets.QLabel(self.groupBox_2)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")
        self.horizontalLayout_8.addWidget(self.label_12)
        self.sizePerFileLabel = QtWidgets.QLabel(self.groupBox_2)
        self.sizePerFileLabel.setObjectName("sizePerFileLabel")
        self.horizontalLayout_8.addWidget(self.sizePerFileLabel)
        self.gridLayout_3.addLayout(self.horizontalLayout_8, 5, 3, 1, 3)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_16 = QtWidgets.QLabel(self.groupBox_2)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_16.setFont(font)
        self.label_16.setObjectName("label_16")
        self.horizontalLayout_3.addWidget(self.label_16)
        self.ledTrigBox = QtWidgets.QComboBox(self.groupBox_2)
        self.ledTrigBox.setObjectName("ledTrigBox")
        self.horizontalLayout_3.addWidget(self.ledTrigBox)
        self.gridLayout_3.addLayout(self.horizontalLayout_3, 6, 0, 1, 4)
        self.arduinoBtn = QtWidgets.QPushButton(self.groupBox_2)
        self.arduinoBtn.setObjectName("arduinoBtn")
        self.gridLayout_3.addWidget(self.arduinoBtn, 7, 0, 1, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.runSaveBtn = QtWidgets.QPushButton(self.groupBox_2)
        self.runSaveBtn.setObjectName("runSaveBtn")
        self.horizontalLayout_2.addWidget(self.runSaveBtn)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.startTriggerBox = QtWidgets.QCheckBox(self.groupBox_2)
        self.startTriggerBox.setObjectName("startTriggerBox")
        self.verticalLayout.addWidget(self.startTriggerBox)
        self.stopTriggerBox = QtWidgets.QCheckBox(self.groupBox_2)
        self.stopTriggerBox.setObjectName("stopTriggerBox")
        self.verticalLayout.addWidget(self.stopTriggerBox)
        self.horizontalLayout_2.addLayout(self.verticalLayout)
        self.gridLayout_3.addLayout(self.horizontalLayout_2, 8, 0, 1, 3)
        self.loopBtn = QtWidgets.QPushButton(self.groupBox_2)
        self.loopBtn.setObjectName("loopBtn")
        self.gridLayout_3.addWidget(self.loopBtn, 9, 0, 1, 1)
        self.abortBtn = QtWidgets.QPushButton(self.groupBox_2)
        self.abortBtn.setObjectName("abortBtn")
        self.gridLayout_3.addWidget(self.abortBtn, 10, 0, 1, 1)
        self.progressBar = QtWidgets.QProgressBar(self.groupBox_2)
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName("progressBar")
        self.gridLayout_3.addWidget(self.progressBar, 11, 0, 1, 3)
        self.label_15.raise_()
        self.expRatio.raise_()
        self.arduinoBtn.raise_()
        self.abortBtn.raise_()
        self.progressBar.raise_()
        self.label_4.raise_()
        self.experimentDuration.raise_()
        self.rgbMode.raise_()
        self.loopBtn.raise_()
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.groupBox_3 = QtWidgets.QGroupBox(self.tab_2)
        self.groupBox_3.setGeometry(QtCore.QRect(20, 20, 701, 211))
        self.groupBox_3.setAutoFillBackground(True)
        self.groupBox_3.setObjectName("groupBox_3")
        self.splitAllBtn = QtWidgets.QPushButton(self.groupBox_3)
        self.splitAllBtn.setGeometry(QtCore.QRect(280, 80, 151, 23))
        self.splitAllBtn.setObjectName("splitAllBtn")
        self.loadFileBtn = QtWidgets.QPushButton(self.groupBox_3)
        self.loadFileBtn.setGeometry(QtCore.QRect(10, 20, 135, 23))
        self.loadFileBtn.setObjectName("loadFileBtn")
        self.subDirList = QtWidgets.QListWidget(self.groupBox_3)
        self.subDirList.setGeometry(QtCore.QRect(10, 50, 256, 151))
        self.subDirList.setObjectName("subDirList")
        self.folderName = QtWidgets.QLabel(self.groupBox_3)
        self.folderName.setGeometry(QtCore.QRect(150, 20, 361, 16))
        self.folderName.setObjectName("folderName")
        self.splitBtn = QtWidgets.QPushButton(self.groupBox_3)
        self.splitBtn.setGeometry(QtCore.QRect(280, 50, 151, 23))
        self.splitBtn.setObjectName("splitBtn")
        self.groupBox_4 = QtWidgets.QGroupBox(self.tab_2)
        self.groupBox_4.setGeometry(QtCore.QRect(20, 240, 701, 211))
        self.groupBox_4.setAutoFillBackground(True)
        self.groupBox_4.setObjectName("groupBox_4")
        self.loadExpFileBtn = QtWidgets.QPushButton(self.groupBox_4)
        self.loadExpFileBtn.setGeometry(QtCore.QRect(10, 20, 135, 23))
        self.loadExpFileBtn.setObjectName("loadExpFileBtn")
        self.dataStimList = QtWidgets.QListWidget(self.groupBox_4)
        self.dataStimList.setGeometry(QtCore.QRect(10, 50, 256, 151))
        self.dataStimList.setObjectName("dataStimList")
        self.experimentFolderName = QtWidgets.QLabel(self.groupBox_4)
        self.experimentFolderName.setGeometry(QtCore.QRect(150, 20, 291, 16))
        self.experimentFolderName.setStyleSheet("border-color: rgb(0, 0, 0);")
        self.experimentFolderName.setObjectName("experimentFolderName")
        self.splitFilesOdourBtn = QtWidgets.QPushButton(self.groupBox_4)
        self.splitFilesOdourBtn.setGeometry(QtCore.QRect(280, 100, 151, 23))
        self.splitFilesOdourBtn.setObjectName("splitFilesOdourBtn")
        self.loadStimSeqBtn = QtWidgets.QPushButton(self.groupBox_4)
        self.loadStimSeqBtn.setGeometry(QtCore.QRect(460, 20, 135, 23))
        self.loadStimSeqBtn.setObjectName("loadStimSeqBtn")
        self.stimList = QtWidgets.QListWidget(self.groupBox_4)
        self.stimList.setGeometry(QtCore.QRect(460, 50, 231, 151))
        self.stimList.setObjectName("stimList")
        self.splitStimFileBtn = QtWidgets.QPushButton(self.groupBox_4)
        self.splitStimFileBtn.setGeometry(QtCore.QRect(280, 60, 151, 23))
        self.splitStimFileBtn.setObjectName("splitStimFileBtn")
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.groupBox_5 = QtWidgets.QGroupBox(self.tab_3)
        self.groupBox_5.setGeometry(QtCore.QRect(20, 20, 701, 271))
        self.groupBox_5.setAutoFillBackground(True)
        self.groupBox_5.setObjectName("groupBox_5")
        self.splittedChannelsList = QtWidgets.QListWidget(self.groupBox_5)
        self.splittedChannelsList.setGeometry(QtCore.QRect(10, 50, 231, 151))
        self.splittedChannelsList.setObjectName("splittedChannelsList")
        self.label = QtWidgets.QLabel(self.groupBox_5)
        self.label.setGeometry(QtCore.QRect(270, 30, 151, 16))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.baselineLength = QtWidgets.QSpinBox(self.groupBox_5)
        self.baselineLength.setGeometry(QtCore.QRect(450, 30, 42, 22))
        self.baselineLength.setObjectName("baselineLength")
        self.label_5 = QtWidgets.QLabel(self.groupBox_5)
        self.label_5.setGeometry(QtCore.QRect(270, 60, 171, 16))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.stimLength = QtWidgets.QSpinBox(self.groupBox_5)
        self.stimLength.setGeometry(QtCore.QRect(450, 60, 42, 22))
        self.stimLength.setObjectName("stimLength")
        self.redProcess = QtWidgets.QCheckBox(self.groupBox_5)
        self.redProcess.setGeometry(QtCore.QRect(280, 90, 70, 17))
        self.redProcess.setObjectName("redProcess")
        self.blueProcess = QtWidgets.QCheckBox(self.groupBox_5)
        self.blueProcess.setGeometry(QtCore.QRect(280, 120, 70, 17))
        self.blueProcess.setObjectName("blueProcess")
        self.mapBtn = QtWidgets.QPushButton(self.groupBox_5)
        self.mapBtn.setGeometry(QtCore.QRect(340, 100, 111, 23))
        self.mapBtn.setObjectName("mapBtn")
        self.layoutWidget = QtWidgets.QWidget(self.groupBox_5)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 20, 231, 25))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.loadOdourFolderBtn = QtWidgets.QPushButton(self.layoutWidget)
        self.loadOdourFolderBtn.setObjectName("loadOdourFolderBtn")
        self.horizontalLayout_13.addWidget(self.loadOdourFolderBtn)
        self.odourFolder = QtWidgets.QLabel(self.layoutWidget)
        self.odourFolder.setObjectName("odourFolder")
        self.horizontalLayout_13.addWidget(self.odourFolder)
        self.tabWidget.addTab(self.tab_3, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 825, 21))
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
        MainWindow.setWindowTitle(_translate("MainWindow", "OMMI"))
        self.groupBox.setTitle(_translate("MainWindow", "Camera Settings"))
        self.expLabel.setText(_translate("MainWindow", "Exposure :"))
        self.approxFramerateBtn.setText(_translate("MainWindow", "Approx Framerate"))
        self.approxFramerateLabel.setText(_translate("MainWindow", "press btn"))
        self.testFramerateBtn.setText(_translate("MainWindow", "Test Framerate"))
        self.testFramerateLabel.setText(_translate("MainWindow", "press btn"))
        self.label_7.setText(_translate("MainWindow", "Bit depth :"))
        self.label_3.setText(_translate("MainWindow", "Binning :"))
        self.label_13.setText(_translate("MainWindow", "Shutter mode :"))
        self.label_14.setText(_translate("MainWindow", "Trigger mode :"))
        self.label_18.setText(_translate("MainWindow", "Overlap :"))
        self.histoBtn.setText(_translate("MainWindow", "Live Histogram"))
        self.cropBtn.setText(_translate("MainWindow", "Crop"))
        self.label_2.setText(_translate("MainWindow", "LEDs"))
        self.Green.setText(_translate("MainWindow", "GREEN"))
        self.Red.setText(_translate("MainWindow", "RED"))
        self.Blue.setText(_translate("MainWindow", "BLUE"))
        self.defaultSettingsBtn.setText(_translate("MainWindow", "Default Settings"))
        self.loadBtn.setText(_translate("MainWindow", "load Zyla"))
        self.expLabel_2.setText(_translate("MainWindow", "Real exposure :"))
        self.loadSettingsFileBtn.setText(_translate("MainWindow", "Load Settings"))
        self.unloadBtn.setText(_translate("MainWindow", "Unload Zyla"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Acquisition Settings"))
        self.label_4.setText(_translate("MainWindow", "Duration (s) :"))
        self.label_15.setText(_translate("MainWindow", "Interval LED ON (%exp)"))
        self.rgbMode.setText(_translate("MainWindow", "Sequential"))
        self.label_6.setText(_translate("MainWindow", "Green"))
        self.label_8.setText(_translate("MainWindow", "Red"))
        self.label_9.setText(_translate("MainWindow", "Blue"))
        self.rbMode.setText(_translate("MainWindow", "R-B"))
        self.label_20.setText(_translate("MainWindow", "Green frame each (nb frames) :"))
        self.label_19.setText(_translate("MainWindow", "Saving folder :"))
        self.savingPathBtn.setText(_translate("MainWindow", "Browse..."))
        self.label_11.setText(_translate("MainWindow", "Name :"))
        self.label_10.setText(_translate("MainWindow", "Frames per file :"))
        self.label_12.setText(_translate("MainWindow", "Max file size (GB) :"))
        self.sizePerFileLabel.setText(_translate("MainWindow", "0.00"))
        self.label_16.setText(_translate("MainWindow", "LED trigger mode :"))
        self.arduinoBtn.setText(_translate("MainWindow", "ARDUINO SYNC"))
        self.runSaveBtn.setText(_translate("MainWindow", "RUN AND SAVE"))
        self.startTriggerBox.setText(_translate("MainWindow", "Start Trigger"))
        self.stopTriggerBox.setText(_translate("MainWindow", "Stop Trigger"))
        self.loopBtn.setText(_translate("MainWindow", "LOOP"))
        self.abortBtn.setText(_translate("MainWindow", "ABORT"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Run and Save"))
        self.groupBox_3.setTitle(_translate("MainWindow", "Classic File"))
        self.splitAllBtn.setText(_translate("MainWindow", "Process whole folder"))
        self.loadFileBtn.setText(_translate("MainWindow", "Load Mouse Folder"))
        self.folderName.setText(_translate("MainWindow", "load a folder..."))
        self.splitBtn.setText(_translate("MainWindow", "Split channels and .txt files"))
        self.groupBox_4.setTitle(_translate("MainWindow", "Loop File"))
        self.loadExpFileBtn.setText(_translate("MainWindow", "Load Experiment Folder"))
        self.experimentFolderName.setText(_translate("MainWindow", "load a folder..."))
        self.splitFilesOdourBtn.setText(_translate("MainWindow", "Split files by odour"))
        self.loadStimSeqBtn.setText(_translate("MainWindow", "Load Stim Sequence File"))
        self.splitStimFileBtn.setText(_translate("MainWindow", "Split Stim file"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "File Splitting"))
        self.groupBox_5.setTitle(_translate("MainWindow", "Map Creation"))
        self.label.setText(_translate("MainWindow", "Baseline of (frames) :"))
        self.label_5.setText(_translate("MainWindow", "Stimulation of (frames) :"))
        self.redProcess.setText(_translate("MainWindow", "Red"))
        self.blueProcess.setText(_translate("MainWindow", "Blue"))
        self.mapBtn.setText(_translate("MainWindow", "Create Odour Map"))
        self.loadOdourFolderBtn.setText(_translate("MainWindow", "Load Odour Folder"))
        self.odourFolder.setText(_translate("MainWindow", "load a folder..."))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "Odour Map Creation"))

