from tkinter import*
from bs4 import BeautifulSoup
import requests
import tkinter.ttk as ttk

import pyautogui
import time
import webbrowser

def abre_o_navegador(linkfilme):

    url = filmes_link[linkfilme]
    chrome_path = 'C:/Program Files/Google/Chrome/Application/chrome.exe %s'
    webbrowser.get(chrome_path).open(url)

    


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
            filmes_link.append(href) 
            

          
                
            


def buscadados():
    url = 'https://redecanais.la/mapafilmes.html'

    #Criação da variável page com URL no método request.get
    page = requests.get(url)

    #coleta,analisa e configura como um objeto BeautifulSoup
    soup = BeautifulSoup(page.text,'html.parser')
    links = soup.find_all('a')

    
    ppesquisa = vnome.get()
    ppesquisa = str(ppesquisa.replace(" ","-"))

    for link in links:
        href= str(link)
        nome = href[href.find("/")+1:href.find("_")]
        nome = nome.replace("-"," ")
        if ppesquisa.casefold() in href.casefold():
            href = href[href.find('<a href="')+9:href.find('" target="')]
            href = "https://redecanais.la"+href  
            filmes.append(nome)
            
            link_do_filme(href)
    


    lb_filmes=Listbox(app,width=79)
    lb_filmes.place(x=10,y=40)
    lb_filmes.bind("<Return>", (lambda event: abre_o_navegador(lb_filmes.index(ACTIVE))))
    lb_filmes.bind("<Double-Button-1>", (lambda event: abre_o_navegador(lb_filmes.index(ACTIVE))))

    for lfilmes in filmes:
        lb_filmes.insert(END,lfilmes)  



filmes = list()
filmes_link = list()

app=Tk()
app.title('BUSCAR POR FILMES NO REDECANAIS')
app.geometry('500x215')
app.configure(background="#000")

#txt1=Label(app,text='PESQUISA',background="#ff0",foreground="#000")
#txt1.place(x=10,y=10,width=100,height=20)
vnome=Entry(app)
vnome.place(x=10,y=10,width=370,height=20)
vnome.bind("<Return>", (lambda event: buscadados()))

Button(app,text="PESQUISA",command=buscadados,background="#ff0",foreground='#000').place(x=390,y=10,width=100,height=21)



app.mainloop()