import sys
import pyqrcode
import dialog
import mainWindow
import PyQt5.QtWidgets as pq

if __name__ == "__main__":
    import sys
    app = pq.QApplication(sys.argv)
    mw = pq.QMainWindow()
    ui = mainWindow.Ui_MainWindow()
    ui.setupUi(mw)
    mw.show()
    sys.exit(app.exec_())

