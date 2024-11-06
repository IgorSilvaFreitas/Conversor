from PySide6.QtWidgets import  QMainWindow
from ui_Regua import Ui_Regua

class MainWindow(QMainWindow, Ui_Regua):
    oldPos = None
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)

def regua(self):
    self.regua = MainWindow()
    self.regua.show()