from tkinter import*
from bs4 import BeautifulSoup
import requests
import tkinter.ttk as ttk

import pyautogui
import time
import webbrowser

def buscar():
    #inicio da segunda funciton
    app.geometry('500x215')
       

    def busca_o_link(link):
        filmes = list()
        listfilme = list()
        Nnome = str(lb_filmes.get(ACTIVE))
        lb_filmes.destroy()


        url = lista_se[link]

            
        page = requests.get(url)

            
        soup = BeautifulSoup(page.text,'html.parser')
        links = soup.find_all('a')

            
        ppesquisa = Nnome
        ppesquisa = str(ppesquisa.replace(" ","-"))

        for link in links:
            href= str(link)
            nome = href[href.find('href="/')+7:href.find("_")]
            nome = nome.replace("-"," ")
            if ppesquisa.casefold() in href.casefold():
                if 'rel="noo' in href.casefold():
                    href = href[href.find('<a href="')+9:href.find('" r')]
                    href = "https://redecanais.cx"+href  
                    filmes.append(nome+"\n")
                    listfilme.append(href)  


        #inicio da terceira funciton
        def abre_o_link(linkfilme):

            url = listfilme[linkfilme]
            page = requests.get(url)
            soup = BeautifulSoup(page.text,'html.parser')
            links = soup.find_all('iframe')

                
            for link in links:
                href= str(link)
                if "Player" in href:
                    href = href[href.find('src="')+5:href.find('" width="')]
                    href = "https://sinalpublico.com"+href.replace(".php","hlb.php")   
                    url = href



            chrome_path = 'C:/Program Files/Google/Chrome/Application/chrome.exe %s'
            webbrowser.get(chrome_path).open(url)



        def verifica():
            app.geometry('500x40')
            if s_filmes:
                s_filmes.destroy()

            if lb_filmes:
                lb_filmes.destroy()

        s_filmes=Listbox(app,width=79)
        s_filmes.place(x=10,y=40)
        s_filmes.bind("<Return>", (lambda event: abre_o_link(s_filmes.index(ACTIVE))))
        s_filmes.bind("<Double-Button-1>", (lambda event: abre_o_link(s_filmes.index(ACTIVE))))
        vnome.bind("<Button-1>", (lambda event: verifica()))
        







        for lfilmes in filmes:
            s_filmes.insert(END,lfilmes)




    #inicio da primeiro function
    
    url = 'https://redecanais.cx/mapa.html'

    #Criação da variável page com URL no método request.get
    page = requests.get(url)

    #coleta,analisa e configura como um objeto BeautifulSoup
    soup = BeautifulSoup(page.text,'html.parser')
    links = soup.find_all('a')


    ppesquisa = vnome.get()
    ppesquisa = str(ppesquisa.replace(" ","-"))

    for link in links:
        href= str(link)
        nome = href[href.find('browse-')+7:href.find("-vi")]
        nome = nome.replace("-"," ")
        

        if ppesquisa.casefold() in href.casefold():
            href = href[href.find('<a href="')+9:href.find('" target="')]
            href = "https://redecanais.cx"+href  
            filmes.append(nome)
            lista_se.append(href)

    

    lb_filmes=Listbox(app,width=79)
    lb_filmes.place(x=10,y=40)
    lb_filmes.bind("<Return>", (lambda event: busca_o_link(lb_filmes.index(ACTIVE))))
    lb_filmes.bind("<Double-Button-1>", (lambda event: busca_o_link(lb_filmes.index(ACTIVE))))

    #lb_filmes.place()
    for lfilmes in filmes:
        lb_filmes.insert(END,lfilmes)












filmes_link = list()
filmes = list()
lista_se = list()




app=Tk()
app.title('BUSCAR POR FILMES NO REDECANAIS')
app.geometry('500x40')
app.configure(background="#000")


vnome=Entry(app)
vnome.place(x=10,y=10,width=370,height=20)
vnome.bind("<Return>", (lambda event: buscar()))

Button(app,text="PESQUISA",command=buscar,background="#ff0",foreground='#000').place(x=390,y=10,width=100,height=21)



app.mainloop()