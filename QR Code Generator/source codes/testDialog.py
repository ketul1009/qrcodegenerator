from PyQt5 import QtCore, QtGui, QtWidgets
import PyQt5
import pyqrcode
import testMainWindow
import sys

class DialogBox(QtWidgets.QDialog):
    def __init__(self, parent = None):
        super(DialogBox, self).__init__(parent)
        self.setObjectName("Dialog")
        self.setWindowIcon(QtGui.QIcon('Resources/logo.png'))
        self.resize(400, 300)
        self.linkInput = QtWidgets.QLineEdit(self)
        self.linkInput.setGeometry(QtCore.QRect(20, 90, 361, 31))
        self.linkInput.setObjectName("linkInput")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self)
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

        self.retranslateUi(self)
        self.cancelButton.clicked.connect(self.cancelButtonPressed)
        self.okButton.clicked.connect(self.okButtonPressed)
        QtCore.QMetaObject.connectSlotsByName(self)

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

    def cancelButtonPressed(self):
        testMainWindow.qrcode.setPixmap(QtGui.QPixmap("Resources/qrcode.png"))
        self.close

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    ex = DialogBox()
    ex.show()
    sys.exit(app.exec_())