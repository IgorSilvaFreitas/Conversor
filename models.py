from PySide6.QtCore import Qt, QAbstractTableModel, QModelIndex

import pandas as pd


class tabela(QAbstractTableModel):

    def __init__(self, data: pd.DataFrame, parent=None):
        QAbstractTableModel.__init__(self,parent)
        #criando uma variável com os dados 
        self._data = data

    # def flags(self, index):

    #     return Qt.ItemFlag.ItemIsEnabled | Qt.ItemFlag.ItemIsSelectable | Qt.ItemFlag.ItemIsEditable

        
    def rowCount(self, parent=QModelIndex()):
        #retorna número de linhas do data frame
        if parent == QModelIndex():
            return len(self._data)

    def columnCount(self, parent=QModelIndex()):
        #retorna número de colunas do data frame
        if parent == QModelIndex():
            return len(self._data.columns)
        return 0

    def data(self, index: QModelIndex, role=Qt.ItemDataRole):

        if role == Qt.ItemDataRole.DisplayRole or role == Qt.ItemDataRole.EditRole:
            
            return self._data.iloc[index.row(),index.column()]
            
                
        return None

    def headerData(
        self, section: int, orientation: Qt.Orientation, role: Qt.ItemDataRole
    ):
        
        if role == Qt.ItemDataRole.DisplayRole:
            if orientation == Qt.Orientation.Horizontal:
                return str(self._data.columns[section])


        return None
    

    def data2(self, row, column):
        return self._data.iloc[row, column]
 
    