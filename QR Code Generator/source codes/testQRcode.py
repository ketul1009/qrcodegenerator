import sys
import pyqrcode
import testDialog
import testMainWindow
import PyQt5.QtWidgets as pq

if __name__ == '__main__':
    app = pq.QApplication(sys.argv)
    ex = testMainWindow.MainWindow()
    ex.show()
    sys.exit(app.exec_())

