from PySide6.QtWidgets import QMainWindow, QMessageBox, QFileDialog
import pandas as pd
import numpy as np

def gerarExcel(self):

    salv_path = QFileDialog.getSaveFileName(self, "Salvar Excel", "", "Excel(*.xlsx)")
        
    modelo = self.tableView.model()
    n_row = modelo.rowCount()
    n_col = modelo.columnCount()   

    tbl_list = []
    for linhas in range(n_row):
        tbl_list2 = []
        for colunas in range(n_col):
            tbl_list2.append(str(modelo.data2(linhas,colunas)))
        tbl_list.append(tbl_list2)

    df = pd.DataFrame(tbl_list)

    df.to_excel(salv_path[0], index=False)

    message_salv = 'Excel salvo'
    dlg_salv = QMessageBox(parent=self, text=message_salv)
    dlg_salv.exec()

    return