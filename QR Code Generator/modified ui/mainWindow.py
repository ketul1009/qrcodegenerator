from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import about
import help

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
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
        self.qrcode.setPixmap(QtGui.QPixmap("../qrcode.svg"))
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
        self.actionAbout_QR_Code_CV = QtWidgets.QAction(MainWindow)
        self.actionAbout_QR_Code_CV.setObjectName("actionAbout_QR_Code_CV")
        self.Help.addAction(self.actionQR_Code_CV_Help)
        self.Help.addAction(self.actionAbout_QR_Code_CV)
        self.menubar.addAction(self.Help.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.actionAbout_QR_Code_CV.triggered.connect(self.about)
        self.actionQR_Code_CV_Help.triggered.connect(self.help)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.generateButton.setText(_translate("MainWindow", "Generate New"))
        self.updateButton.setText(_translate("MainWindow", "Update"))
        self.Help.setTitle(_translate("MainWindow", "Help"))
        self.actionQR_Code_CV_Help.setText(_translate("MainWindow", "QR Code CV Help"))
        self.actionAbout_QR_Code_CV.setText(_translate("MainWindow", "About QR Code CV"))

    def about(self):
        About = QtWidgets.QDialog()
        ui = about.Ui_About()
        ui.setupUi(About)
        About.exec()

    def help(self):
        Help = QtWidgets.QDialog()
        ui = help.Ui_Help()
        ui.setupUi(Help)
        Help.exec()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
