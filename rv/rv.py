import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from rv.gui import Ui_MainWindow


class RequestViewer:
    def __init__(self):
        self.app = QApplication(sys.argv)
        window = QMainWindow()
        form = Ui_MainWindow()
        form.setupUi(window)
        window.show()
        self.app.exec()
