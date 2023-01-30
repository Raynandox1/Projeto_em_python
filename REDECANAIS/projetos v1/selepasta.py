#gostei muito desse código
from tkinter import Tk
from tkinter.filedialog import askopenfilename
from openpyxl import workbook, load_workbook

Tk().withdraw() # Isto torna oculto a janela principal
filename = askopenfilename() # Isto te permite selecionar um arquivo

arquivo = open(filename,"r")
msg=arquivo.readlines()
frases = list()

planilha = load_workbook("postev5.xlsm", read_only=False, keep_vba=True)
aba_ativa = planilha.active
lcont = 2

for linha in msg:
    if "POINT Z" in linha:
        linha = linha[linha.find("(")+1:linha.rfind(")")]
        
        longitude = linha[:linha.find(".")]
        p1 = linha.find(" ")
        latitude = linha[p1:linha.find(".",p1+4)]

        aba_ativa[f"a{lcont}"] = longitude
        aba_ativa[f"b{lcont}"] = latitude

        lcont = lcont + 1
       
planilha.save("postev5.xlsm")

import xlwings as xw

wb = xw.Book('postev5.xlsm')

login = wb.macro('mACADText.AddTextUpdated')
login()

wb.save

if len(wb.app.books)==1:
    wb.app.quit()
else:
    wb.close()