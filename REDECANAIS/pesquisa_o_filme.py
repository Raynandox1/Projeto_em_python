from bs4 import BeautifulSoup
import requests

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
            href = "https://sinalpublico.com"+href.replace(".php","hlb.php")    
            print(href+"\n")

    


url = 'https://redecanais.la/mapafilmes.html'

#Criação da variável page com URL no método request.get
page = requests.get(url)

#coleta,analisa e configura como um objeto BeautifulSoup
soup = BeautifulSoup(page.text,'html.parser')
links = soup.find_all('a')

import easygui
ppesquisa = easygui.enterbox("FILMES: ")
ppesquisa = str(ppesquisa.replace(" ","-"))

for link in links:
    href= str(link)
    nome = "NOME: " + href[href.find("/")+1:href.find("_")]
    nome = nome.replace("-"," ")
    if ppesquisa.casefold() in href.casefold():
        href = href[href.find('<a href="')+9:href.find('" target="')]
        href = "https://redecanais.la"+href  
        
        print(nome)
        link_do_filme(href)
        



