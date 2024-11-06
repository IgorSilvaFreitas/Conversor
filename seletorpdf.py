from PySide6.QtWidgets import QMessageBox, QFileDialog

def abrir(self):

        ### abrir explorado de arquivo para selecionar extrato
        #if self.caminhoFile.text() == '':
        path = QFileDialog.getOpenFileName()


        #### verifica se escolheram algum arquivo ou cancelaram
        if path[0].count('/')!=0:   
            ### Salvando do caminho do extrato no campo desejado
            self.caminho_ql.setText(path[0])
        
        self.pesquisar_bt.clicked["bool"].disconnect()

        return