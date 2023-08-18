from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QFileDialog
from PyQt5 import QtCore
import sys
import dialog
import pyqrcode

class FileDialog():
    
    def __init__(self):
    
        self.file , self.check = QFileDialog.getSaveFileName(None, "Save QR Code",
                                                "", "All Files (*);;Python Files (*.py);;Text Files (*.txt)")
        if self.check:
            self.link = dialog.Ui_Dialog().getLink()
            url = pyqrcode.create(self.link)
            url.svg(self.file, scale=5)