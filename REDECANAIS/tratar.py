from tkinter import Tk
from tkinter.filedialog import askopenfilename
#from openpyxl import workbook, load_workbook

Tk().withdraw() # Isto torna oculto a janela principal
filename = askopenfilename() # Isto te permite selecionar um arquivo


arquivo = open(filename,"r", encoding="utf-8")
msg=arquivo.readlines()
frases = list()

for linha in msg:
    if "<b>Assistir</b>" in linha:
        nome = linha[:linha.find("- <a href=\"")]
        link = linha[linha.find("- <a href=\"")+11:linha.rfind("\" target=\"")]


        frases.append("NOME: " + nome + '\n')
        frases.append("LINK: https://redecanais.la" + link + '\n')




arquivo = open("nome e link.txt", "w")

arquivo.writelines(frases)
