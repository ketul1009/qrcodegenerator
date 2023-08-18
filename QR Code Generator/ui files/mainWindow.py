from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import dialog


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
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
        self.qrcode.setPixmap(QtGui.QPixmap("qrcode.svg"))
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
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.generateButton.clicked.connect(self.generateButtonPressed)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.generateButton.setText(_translate("MainWindow", "Generate New"))

    def generateButtonPressed(self):
        Dialog = QtWidgets.QDialog()
        ui = dialog.Ui_Dialog()
        ui.setupUi(Dialog)
        self.qrcode.setPixmap(QtGui.QPixmap("qrcode.svg"))
        Dialog.exec()
