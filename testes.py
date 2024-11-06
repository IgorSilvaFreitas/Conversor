import tabula as tb
import pandas as pd

path = r'\\192.168.25.225\PRIVADO_Contabilidade\RED TEAM\2024 - CONTROLES\CONTABIL - INTEGRAÇÃO E ANÁLISE\GRUPO SERRA AZUL\2104 - J PINTO COMERCIO DE ALIMENTOS LTDA (SÃO GERALDO) - 1\09 - SETEMBRO\EXTRATOS\Extrato Consolidado.pdf'

sep_preproc = '40,70,80,90,110'
if sep_preproc.replace(',','').isnumeric():
    list_sep = sep_preproc.split(',')
columns_sep = []
for i in list_sep:
    columns_sep.append(int(i))

print(columns_sep)



# dfc = pd.DataFrame()

# for i in range(1, 1+1):
    
#     dfs = tb.read_pdf(path,
#     pages=str(i),
#     relative_area=True,
#     relative_columns=True,
#     area=[0,0,100,100],
#     columns=columns_sep,
#     lattice=False,
#     stream=True,
#     guess=False,
#     pandas_options={'header':None})

#     tbl = dfs[0].copy()
    
#     dfc = pd.concat([dfc, tbl], axis=0,ignore_index=True)

# print(dfc.head(30))
