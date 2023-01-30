from bs4 import BeautifulSoup
import requests

from tkinter import Tk
from tkinter.filedialog import askopenfilename
#from openpyxl import workbook, load_workbook

Tk().withdraw() # Isto torna oculto a janela principal
filename = askopenfilename() # Isto te permite selecionar um arquivo

arquivo = open(filename,"r", encoding="utf-8")
msg=arquivo.readlines()

frases = list()

def link_do_filme(resultado):
    url = resultado

    #Criação da variável page com URL no método request.get
    page = requests.get(url)

    #coleta,analisa e configura como um objeto BeautifulSoup
    soup = BeautifulSoup(page.text,'html.parser')
    links = soup.find_all('iframe')

    #retorna os todos os links do Junho de 2017 da página

    for link in links:
        href= str(link)
        #print(href)
        if "Player" in href:
            href = href[href.find('src="')+5:href.find('" width="')]
            href = "LINK: https://sinalpublico.com"+href.replace(".php","hlb.php")    
            frases.append(href+'\n')



for linha in msg:
    if '<b>Assistir</b>' in linha:
        nome = linha[:linha.find('- <a href="')]
        link2 = 'https://redecanais.la' + linha[linha.find('ref="')+5:linha.find('" target="')]
        frases.append("NOME: " + nome + '\n')
        link_do_filme(link2)
        
        
arquivo = open("LISTA FINAL.TXT", "w")

arquivo.writelines(frases) 



  


