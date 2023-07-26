# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_window.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1012, 837)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        Form.setMinimumSize(QtCore.QSize(500, 0))
        self.gridLayout = QtWidgets.QGridLayout(Form)
        self.gridLayout.setObjectName("gridLayout")
        self.scrollArea = QtWidgets.QScrollArea(Form)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 988, 813))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.gridLayout_35 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_35.setObjectName("gridLayout_35")
        self.configurationTabWidget = QtWidgets.QTabWidget(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.configurationTabWidget.sizePolicy().hasHeightForWidth())
        self.configurationTabWidget.setSizePolicy(sizePolicy)
        self.configurationTabWidget.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.configurationTabWidget.setFont(font)
        self.configurationTabWidget.setMovable(True)
        self.configurationTabWidget.setObjectName("configurationTabWidget")
        self.optimizerTab = QtWidgets.QWidget()
        self.optimizerTab.setObjectName("optimizerTab")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.optimizerTab)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.optimizerConfigurationTabWidget = QtWidgets.QTabWidget(self.optimizerTab)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.optimizerConfigurationTabWidget.setFont(font)
        self.optimizerConfigurationTabWidget.setTabPosition(QtWidgets.QTabWidget.West)
        self.optimizerConfigurationTabWidget.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.optimizerConfigurationTabWidget.setMovable(True)
        self.optimizerConfigurationTabWidget.setObjectName("optimizerConfigurationTabWidget")
        self.optimizerMainTab = QtWidgets.QWidget()
        self.optimizerMainTab.setObjectName("optimizerMainTab")
        self.gridLayout_17 = QtWidgets.QGridLayout(self.optimizerMainTab)
        self.gridLayout_17.setObjectName("gridLayout_17")
        self.textBrowser = QtWidgets.QTextBrowser(self.optimizerMainTab)
        self.textBrowser.setStyleSheet("background-color: rgb(249, 249, 249);")
        self.textBrowser.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.textBrowser.setObjectName("textBrowser")
        self.gridLayout_17.addWidget(self.textBrowser, 2, 1, 1, 1)
        self.optimizerDataLabel = QtWidgets.QLabel(self.optimizerMainTab)
        self.optimizerDataLabel.setText("")
        self.optimizerDataLabel.setObjectName("optimizerDataLabel")
        self.gridLayout_17.addWidget(self.optimizerDataLabel, 3, 1, 1, 1)
        self.optimizerConfigurationTabWidget.addTab(self.optimizerMainTab, "")
        self.optimizerDateTab = QtWidgets.QWidget()
        self.optimizerDateTab.setObjectName("optimizerDateTab")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.optimizerDateTab)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.textBrowser_2 = QtWidgets.QTextBrowser(self.optimizerDateTab)
        self.textBrowser_2.setStyleSheet("background-color: rgb(249, 249, 249);")
        self.textBrowser_2.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.textBrowser_2.setObjectName("textBrowser_2")
        self.verticalLayout_3.addWidget(self.textBrowser_2)
        self.optimizerConfigurationTabWidget.addTab(self.optimizerDateTab, "")
        self.verticalLayout_2.addWidget(self.optimizerConfigurationTabWidget)
        self.configurationTabWidget.addTab(self.optimizerTab, "")
        self.mainTab = QtWidgets.QWidget()
        self.mainTab.setObjectName("mainTab")
        self.gridLayout_14 = QtWidgets.QGridLayout(self.mainTab)
        self.gridLayout_14.setObjectName("gridLayout_14")
        self.mainOptionsGroupBox = QtWidgets.QGroupBox(self.mainTab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mainOptionsGroupBox.sizePolicy().hasHeightForWidth())
        self.mainOptionsGroupBox.setSizePolicy(sizePolicy)
        self.mainOptionsGroupBox.setTitle("")
        self.mainOptionsGroupBox.setObjectName("mainOptionsGroupBox")
        self.gridLayout_13 = QtWidgets.QGridLayout(self.mainOptionsGroupBox)
        self.gridLayout_13.setObjectName("gridLayout_13")
        self.credentialsGroupBox = QtWidgets.QGroupBox(self.mainOptionsGroupBox)
        self.credentialsGroupBox.setObjectName("credentialsGroupBox")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.credentialsGroupBox)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.selectfile = QtWidgets.QPushButton(self.credentialsGroupBox)
        self.selectfile.setAutoDefault(False)
        self.selectfile.setObjectName("selectfile")
        self.horizontalLayout.addWidget(self.selectfile)
        self.filesite = QtWidgets.QLineEdit(self.credentialsGroupBox)
        self.filesite.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.filesite.setObjectName("filesite")
        self.horizontalLayout.addWidget(self.filesite)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.gridLayout_13.addWidget(self.credentialsGroupBox, 6, 0, 1, 3)
        self.tickerLabel = QtWidgets.QLabel(self.mainOptionsGroupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tickerLabel.sizePolicy().hasHeightForWidth())
        self.tickerLabel.setSizePolicy(sizePolicy)
        self.tickerLabel.setObjectName("tickerLabel")
        self.gridLayout_13.addWidget(self.tickerLabel, 0, 0, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_13.addItem(spacerItem1, 0, 2, 1, 1)
        self.accountTypeGroupBox = QtWidgets.QGroupBox(self.mainOptionsGroupBox)
        self.accountTypeGroupBox.setObjectName("accountTypeGroupBox")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.accountTypeGroupBox)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.pHis = QtWidgets.QRadioButton(self.accountTypeGroupBox)
        self.pHis.setObjectName("pHis")
        self.horizontalLayout_2.addWidget(self.pHis)
        self.pLys = QtWidgets.QRadioButton(self.accountTypeGroupBox)
        self.pLys.setChecked(True)
        self.pLys.setObjectName("pLys")
        self.horizontalLayout_2.addWidget(self.pLys)
        self.pArg = QtWidgets.QRadioButton(self.accountTypeGroupBox)
        self.pArg.setChecked(False)
        self.pArg.setObjectName("pArg")
        self.horizontalLayout_2.addWidget(self.pArg)
        self.gridLayout_13.addWidget(self.accountTypeGroupBox, 7, 0, 1, 1)
        self.example = QtWidgets.QPushButton(self.mainOptionsGroupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.example.sizePolicy().hasHeightForWidth())
        self.example.setSizePolicy(sizePolicy)
        self.example.setAutoDefault(False)
        self.example.setObjectName("example")
        self.gridLayout_13.addWidget(self.example, 0, 1, 1, 1)
        self.fastatext = QtWidgets.QTextEdit(self.mainOptionsGroupBox)
        self.fastatext.setObjectName("fastatext")
        self.gridLayout_13.addWidget(self.fastatext, 3, 0, 1, 3)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.submit = QtWidgets.QPushButton(self.mainOptionsGroupBox)
        self.submit.setObjectName("submit")
        self.horizontalLayout_3.addWidget(self.submit)
        self.reset = QtWidgets.QPushButton(self.mainOptionsGroupBox)
        self.reset.setAutoDefault(False)
        self.reset.setObjectName("reset")
        self.horizontalLayout_3.addWidget(self.reset)
        self.gridLayout_13.addLayout(self.horizontalLayout_3, 9, 0, 2, 1)
        self.gridLayout_14.addWidget(self.mainOptionsGroupBox, 0, 0, 1, 1)
        self.configurationTabWidget.addTab(self.mainTab, "")
        self.simulationWidget = QtWidgets.QWidget()
        self.simulationWidget.setObjectName("simulationWidget")
        self.gridLayout_29 = QtWidgets.QGridLayout(self.simulationWidget)
        self.gridLayout_29.setObjectName("gridLayout_29")
        self.textBrowser_3 = QtWidgets.QTextBrowser(self.simulationWidget)
        self.textBrowser_3.setStyleSheet("background-color: rgb(249, 249, 249);")
        self.textBrowser_3.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.textBrowser_3.setObjectName("textBrowser_3")
        self.gridLayout_29.addWidget(self.textBrowser_3, 0, 0, 1, 1)
        self.configurationTabWidget.addTab(self.simulationWidget, "")
        self.gridLayout_35.addWidget(self.configurationTabWidget, 0, 1, 1, 1)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout.addWidget(self.scrollArea, 0, 0, 1, 1)

        self.retranslateUi(Form)
        self.configurationTabWidget.setCurrentIndex(1)
        self.optimizerConfigurationTabWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "prediction"))
        self.textBrowser.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:18pt;\"><br /></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'微软雅黑\'; font-size:18pt; font-weight:600; color:#000000;\"><br /></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'微软雅黑\'; font-size:18pt; font-weight:600; color:#000000;\"><br /></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:18pt;\"><br /></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'微软雅黑\'; font-size:18pt; font-weight:600; color:#000000;\">Welcome to the DTL-RespLys</span></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:18pt; font-weight:600; color:#000000;\"><br /></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:18pt; color:#000000;\">DTL-RespLys is a web server that could predict human lysine and arginine phosphorylation sites. It contains two classifers. DTL-RespLys takes protein sequence data as input and uses One-Hot encoding scheme and One-Dimensional Convolutional Convolutional Neural Network (1-D CNN) based on residual structure and deep-transfer learning strategy to predict human lysine phosphorylation sites.DeeppArg takes protein sequence data as input and uses One-Hot encoding scheme and One-Dimensional Convolutional Convolutional Neural Network (1-D CNN) to predict human arginine phosphorylation sites.</span></p></body></html>"))
        self.optimizerConfigurationTabWidget.setTabText(self.optimizerConfigurationTabWidget.indexOf(self.optimizerMainTab), _translate("Form", "Welcome"))
        self.textBrowser_2.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Tahoma\'; font-size:11pt; font-weight:600;\"><br /></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Tahoma\'; font-size:11pt; font-weight:600;\"><br /></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Tahoma\'; font-size:11pt; font-weight:600;\">Contact For using DTL-RespLys</span></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Calibri\'; font-size:11pt;\">Please cite:</span></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Calibri\'; font-size:11pt;\">Xulin Chang et al.</span></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Calibri\'; font-size:11pt;\">DTL-RespLys: A Deep-Transfer Learning Architecture for prediction of Lysine </span></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Calibri\'; font-size:11pt;\">Phosphorylations Sites base on Residual</span></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Calibri\'; font-size:11pt;\">(article link)</span></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Calibri\'; font-size:11pt;\"><br /></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Calibri\'; font-size:11pt;\"><br /></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Calibri\'; font-size:11pt;\"><br /></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Calibri\'; font-size:11pt;\"><br /></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Tahoma\'; font-size:11pt; font-weight:600;\">Contact:</span></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Calibri\'; font-size:11pt;\">    *Xulin Chang</span></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Tahoma\'; font-size:11pt; font-weight:600;\">Address</span><span style=\" font-family:\'Tahoma\'; font-size:11pt;\">: School of Computer Science And Technology</span></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Tahoma\'; font-size:11pt;\">             Qingdao University</span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Tahoma\'; font-size:11pt;\">             Qingdao, China</span></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Tahoma\'; font-size:11pt;\"><br /></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Tahoma\'; font-size:11pt; font-weight:600;\">E-mail</span><span style=\" font-family:\'Tahoma\'; font-size:11pt;\">: 1623956013@qq.com,  lileime@hotmail.com</span></p></body></html>"))
        self.optimizerConfigurationTabWidget.setTabText(self.optimizerConfigurationTabWidget.indexOf(self.optimizerDateTab), _translate("Form", "Please citation"))
        self.configurationTabWidget.setTabText(self.configurationTabWidget.indexOf(self.optimizerTab), _translate("Form", "Home"))
        self.credentialsGroupBox.setTitle(_translate("Form", "Or upload a Fasta"))
        self.selectfile.setToolTip(_translate("Form", "Load Binance and Telegram credentials. Program will try to load credentials automatically from default.json."))
        self.selectfile.setText(_translate("Form", "Select File"))
        self.tickerLabel.setText(_translate("Form", "Input your protein sequences with the FASTA format."))
        self.accountTypeGroupBox.setTitle(_translate("Form", "Prediction Type"))
        self.pHis.setText(_translate("Form", "pH"))
        self.pLys.setToolTip(_translate("Form", "Select this if the asset you are trading is isolated."))
        self.pLys.setText(_translate("Form", "pK"))
        self.pArg.setToolTip(_translate("Form", "Select this if the asset you are trading is not isolated."))
        self.pArg.setText(_translate("Form", "pR"))
        self.example.setToolTip(_translate("Form", "Saves Binance and Telegram credentials. By default, they will save to default.json."))
        self.example.setText(_translate("Form", "Example"))
        self.submit.setText(_translate("Form", "Submit"))
        self.reset.setToolTip(_translate("Form", "Test Binance API credentials."))
        self.reset.setText(_translate("Form", "Reset"))
        self.configurationTabWidget.setTabText(self.configurationTabWidget.indexOf(self.mainTab), _translate("Form", "Prediction"))
        self.textBrowser_3.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:9pt;\"><br /></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Calibri\'; font-size:26pt; font-weight:600;\"><br /></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Calibri\'; font-size:26pt; font-weight:600;\">Help for Using DTL-RespLys</span></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Calibri\'; font-size:26pt; font-weight:600;\"><br /></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Tahoma\'; font-size:16pt;\">1.Input</span></p>\n"
"<ul style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 1;\"><li style=\" font-family:\'Tahoma,Geneva,sans-serif\'; font-size:9pt; color:#333333;\" align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">To obtain the predicted results ,The protein sequences input to our server should be FASTA format.<span style=\" font-family:\'Tahoma\';\"> </span></li>\n"
"<li style=\" font-family:\'Tahoma\'; font-size:12pt;\" align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Tahoma,Geneva,sans-serif\'; font-size:13px; color:#333333;\">The accepted characters are: A, C, D, E, F, G, H, I, K, L, M, N, P, Q, R, S, T, V, W, Y, and the dummy code X. To ensure accurate prediction, please do not include illegal characters in the query sequence.</span>              </li></ul>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Tahoma\'; font-size:12pt;\"><br /></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Tahoma\'; font-size:16pt;\">2.Output</span></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Tahoma,Geneva,sans-serif\'; font-size:12pt; color:#333333;\">The prediction output consists of four items:</span></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Tahoma,Geneva,sans-serif\'; font-size:12pt; color:#333333;\"><br /></p>\n"
"<ul style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 1;\"><li style=\" font-family:\'Tahoma,Geneva,sans-serif\'; font-size:12pt; color:#333333;\" align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:13px;\">Protein name</span></li>\n"
"<li style=\" font-family:\'Tahoma\'; font-size:12pt;\" align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Tahoma,Geneva,sans-serif\'; font-size:13px; color:#333333;\">Position</span>  </li>\n"
"<li style=\" font-family:\'Tahoma\'; font-size:12pt;\" align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Tahoma,Geneva,sans-serif\'; font-size:13px; color:#333333;\">Sequence </span></li>\n"
"<li style=\" font-family:\'Tahoma,Geneva,sans-serif\'; font-size:12pt; color:#333333;\" align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:13px;\">Prediction score</span></li>\n"
"<li style=\" font-family:\'Tahoma,Geneva,sans-serif\'; font-size:12pt; color:#333333;\" align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a name=\"tooplate_wrapper\"></a><span style=\" font-size:13px;\">P</span><span style=\" font-size:13px;\">rediction category</span></li></ul></body></html>"))
        self.configurationTabWidget.setTabText(self.configurationTabWidget.indexOf(self.simulationWidget), _translate("Form", "Help"))
