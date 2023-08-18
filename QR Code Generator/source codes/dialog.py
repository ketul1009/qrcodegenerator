from PyQt5 import QtCore, QtGui, QtWidgets
import PyQt5
import pyqrcode
import mainWindow


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.setWindowIcon(QtGui.QIcon('Resources/logo.png'))
        Dialog.resize(400, 300)
        self.linkInput = QtWidgets.QLineEdit(Dialog)
        self.linkInput.setGeometry(QtCore.QRect(20, 90, 361, 31))
        self.linkInput.setObjectName("linkInput")
        self.horizontalLayoutWidget = QtWidgets.QWidget(Dialog)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(20, 229, 361, 51))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.dlgButtonLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.dlgButtonLayout.setContentsMargins(0, 0, 0, 0)
        self.dlgButtonLayout.setObjectName("dlgButtonLayout")
        self.okButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.okButton.sizePolicy().hasHeightForWidth())
        self.okButton.setSizePolicy(sizePolicy)
        self.okButton.setObjectName("okButton")
        self.dlgButtonLayout.addWidget(self.okButton)
        self.cancelButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cancelButton.sizePolicy().hasHeightForWidth())
        self.cancelButton.setSizePolicy(sizePolicy)
        self.cancelButton.setObjectName("cancelButton")
        self.dlgButtonLayout.addWidget(self.cancelButton)

        self.retranslateUi(Dialog)
        self.cancelButton.clicked.connect(Dialog.close)
        self.okButton.clicked.connect(self.okButtonPressed)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.okButton.setText(_translate("Dialog", "OK"))
        self.cancelButton.setText(_translate("Dialog", "Cancel"))

    def okButtonPressed(self):
        self.link = self.linkInput.text()
        url = pyqrcode.create(self.link)
        url.png('Resources/qrcode.png', scale=8)
        self.okButton.setVisible(False)
        self.cancelButton.setText("Close")
