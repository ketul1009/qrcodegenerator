from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import help
import dialog

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowIcon(QtGui.QIcon('Resources/logo.png'))
        MainWindow.setWindowModality(QtCore.Qt.NonModal)
        MainWindow.resize(787, 539)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(220, 50, 351, 261))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.qrcodeLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.qrcodeLayout.setContentsMargins(0, 0, 0, 0)
        self.qrcodeLayout.setObjectName("qrcodeLayout")
        self.qrcode = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.qrcode.setText("")
        self.qrcode.setTextFormat(QtCore.Qt.AutoText)
        self.qrcode.setPixmap(QtGui.QPixmap("Resources/qrcode.png"))
        self.qrcode.setAlignment(QtCore.Qt.AlignCenter)
        self.qrcode.setObjectName("qrcode")
        self.qrcodeLayout.addWidget(self.qrcode)
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(220, 340, 351, 80))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.generateLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.generateLayout.setContentsMargins(0, 0, 0, 0)
        self.generateLayout.setObjectName("generateLayout")
        self.generateButton = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.generateButton.setObjectName("generateButton")
        self.generateLayout.addWidget(self.generateButton)
        self.updateButton = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.updateButton.setObjectName("updateButton")
        self.generateLayout.addWidget(self.updateButton)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 787, 29))
        self.menubar.setObjectName("menubar")
        self.Help = QtWidgets.QMenu(self.menubar)
        self.Help.setObjectName("Help")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionQR_Code_CV_Help = QtWidgets.QAction(MainWindow)
        self.actionQR_Code_CV_Help.setObjectName("actionQR_Code_CV_Help")
        self.Help.addAction(self.actionQR_Code_CV_Help)
        self.menubar.addAction(self.Help.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.actionQR_Code_CV_Help.triggered.connect(self.help)
        self.generateButton.clicked.connect(self.generateButtonPressed)
        self.updateButton.clicked.connect(self.updateButtonPressed)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "QR Code Generator"))
        self.generateButton.setText(_translate("MainWindow", "Generate New"))
        self.updateButton.setText(_translate("MainWindow", "Update"))
        self.Help.setTitle(_translate("MainWindow", "Help"))
        self.actionQR_Code_CV_Help.setText(_translate("MainWindow", "QR Code CV Help"))

    def generateButtonPressed(self):
        Dialog = QtWidgets.QDialog()
        ui = dialog.Ui_Dialog()
        ui.setupUi(Dialog)
        Dialog.exec()

    def updateButtonPressed(self):
        self.qrcode.setPixmap(QtGui.QPixmap("Resources/qrcode.png"))

    def help(self):
        Help = QtWidgets.QDialog()
        ui = help.Ui_Help()
        ui.setupUi(Help)
        Help.exec()