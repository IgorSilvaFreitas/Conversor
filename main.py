from PySide6.QtWidgets import QApplication, QMainWindow
from seletorpdf import abrir
from conversor import checaOpcoes
from salvar import gerarExcel
from ui_Main import Ui_Conversor
from regua import regua
import sys

class MainWindow(QMainWindow, Ui_Conversor):

    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        #self.setWindowFlags(Qt.WindowType.FramelessWindowHint)
        
        #salvar caminho do arquivo do arquivo
        self.pesquisar_bt.clicked.connect(lambda: abrir(self))

        #converter pdf em excel
        self.converter_bt.clicked.connect(lambda: checaOpcoes(self))

        #salva o excel
        self.salvar_bt.clicked.connect(lambda: gerarExcel(self))

        #abre a regua
        self.calc_sep.clicked.connect(lambda: regua(self))

    def dragEnterEvent(self, event):
        if event.mimeData().hasUrls():
            event.accept()
        else:
            event.ignore()

    def dropEvent(self, event):
        files = [u.toLocalFile() for u in event.mimeData().urls()]
        for f in files:
            self.caminho_ql.setText(f)
        

if __name__ == '__main__':

    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()