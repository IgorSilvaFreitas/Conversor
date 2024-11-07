import tabula as tb
import pandas as pd
import PyPDF2
from PySide6.QtWidgets import QMessageBox

from models import tabela




def checaOpcoes(self):

    path = self.caminho_ql.text()
    if path == '':
        message_salv = 'Selecione o arquivo pdf'
        dlg_salv = QMessageBox(parent=self, text=message_salv)
        dlg_salv.exec()
        return

    sep_preproc = self.edit_area.text()
    if sep_preproc == '' and self.lattice.isChecked() == False:
        message_salv = 'Selecione as áreas de cada coluna'
        dlg_salv = QMessageBox(parent=self, text=message_salv)
        dlg_salv.exec()
        return

    if sep_preproc.replace(',','').isnumeric():
        list_sep = sep_preproc.split(',')
        columns_sep = []
        for i in list_sep:
            columns_sep.append(int(i))
    else:
        if  self.lattice.isChecked() == False:
            message_salv = 'Há algum erro na área de separação'
            dlg_salv = QMessageBox(parent=self, text=message_salv)
            dlg_salv.exec()
            return
        columns_sep = []

    
 
    #columns_sep = columns_sep.sort()

    if self.lattice.isChecked():
        lat_opt =True
        str_opt = False
    else:
        lat_opt = False
        str_opt = True


    pagina_inicial = self.edit_inicial.text()
    if pagina_inicial == '':
        pagina_inicial = 1

    elif pagina_inicial.isnumeric() == False:
        message_salv = 'O campo página inicial precisa ser númerico'
        dlg_salv = QMessageBox(parent=self, text=message_salv)
        dlg_salv.exec()
        return

    pagina_final = self.edit_final.text()
    if pagina_final == '':
        pdfToExcel(self, path, pagina_inicial, lat_opt, str_opt, columns_sep)
        return

    if pagina_final.isnumeric():
        pdfToExcel(self, path, pagina_inicial, lat_opt, str_opt, columns_sep, int(pagina_final))
        return

    if pagina_final.isnumeric() == False:
        message_salv = 'O campo página inicial precisa ser númerico'
        dlg_salv = QMessageBox(parent=self, text=message_salv)
        dlg_salv.exec()
        return



def pdfToExcel(self, path: str, pagina_inicial: int, lat_opt: bool, str_opt: bool, columns_sep, pagina_final: str | int = 'nIden'):

    if pagina_final == 'nIden':
        reader = PyPDF2.PdfReader(path)
        pagina_final = len(reader.pages)

    
    dfc = pd.DataFrame()

    if str_opt == True:

        for i in range(pagina_inicial, pagina_final+1):
            
            dfs = tb.read_pdf(path,
            pages=str(i),
            relative_area=True,
            relative_columns=True,
            area=[0,0,100,100],
            columns=columns_sep,
            lattice=lat_opt,
            stream=str_opt,
            guess=False,
            pandas_options={'header':None})

            tbl = dfs[0].copy()
            
            dfc = pd.concat([dfc, tbl], axis=0,ignore_index=True)

    if lat_opt == True:

        for i in range(pagina_inicial, pagina_final+1):
            
            dfs = tb.read_pdf(path,
            pages=str(i),
            lattice=lat_opt,
            stream=str_opt,
            pandas_options={'header':None})

            tbl = dfs[0].copy()
            
            dfc = pd.concat([dfc, tbl], axis=0,ignore_index=True)

    popularTabela(self, dfc)
    return
        
def popularTabela(self, df: pd.DataFrame):
    self.model = tabela(df)
    self.tableView.setModel(self.model)
    return
   
