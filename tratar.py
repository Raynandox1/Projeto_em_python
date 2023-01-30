#SELECIONA O ARQUIVO E SEPARA O NOME E O LINK

from tkinter import Tk
from tkinter.filedialog import askopenfilename
#from openpyxl import workbook, load_workbook

Tk().withdraw() # Isto torna oculto a janela principal
filename = askopenfilename() # Isto te permite selecionar um arquivo


arquivo = open(filename,"r", encoding='utf-8')
msg=arquivo.readlines()
frases = list()

for linha in msg:
    if "<a href=\"" in linha:
        
        nome = linha[:linha.find("- <a href=\"")]
        nome = "NOME: " +  nome

        link = "LINK: " + linha[linha.find("- <a href=\""):linha.find("\" target=\"")]

        
        
        frases.append(nome)
        frases.append(link)

arquivo = open("nome.txt", "w")

arquivo.writelines(frases)
