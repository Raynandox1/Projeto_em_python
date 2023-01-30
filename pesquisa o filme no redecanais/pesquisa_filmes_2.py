from tkinter import*
from bs4 import BeautifulSoup
import requests
import tkinter.ttk as ttk
import webbrowser


def buscadados():
    txt1.place_forget()
    lb_filmes.delete(0,END)
    lista.clear()
    link_do_filme.clear()

    url = 'https://redecanais.la/mapafilmes.html'

    #Criação da variável page com URL no método request.get
    page = requests.get(url)

    #coleta,analisa e configura como um objeto BeautifulSoup
    soup = BeautifulSoup(page.text,'html.parser')
    links = soup.find_all('a')

    
    ppesquisa = vnome.get()
    vnome.delete(0,END)
    ppesquisa = str(ppesquisa.replace(" ","-"))

    for link in links:
        href= str(link)
        nome = href[href.find("/")+1:href.find("_")]
        nome = nome.replace("-"," ")
        if ppesquisa.casefold() in href.casefold():
            href = href[href.find('<a href="')+9:href.find('" target="')]
            href = "https://redecanais.la"+href  
            lista.append(nome)
                
                
                
            url = href

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
                    link_do_filme.append(href) 
    

    if len(lista) == 0:
        #txt1=Label(app,text='NADA ENCONTRADO!!!',background="#ff0",foreground='#000',font=("arial", 25))
        txt1.place(x=10,y=40,width=480,height=168)
        return

    for lfilmes in lista:
        lb_filmes.insert(END,lfilmes) 

   
    
    lb_filmes.place(x=10,y=40)

def abre_o_navegador(linkfilme):
    
    url = link_do_filme[linkfilme]
    chrome_path = 'C:/Program Files/Google/Chrome/Application/chrome.exe %s'
    webbrowser.get(chrome_path).open(url)


lista = list()
link_do_filme = list()

app=Tk()
app.title('BUSCAR POR FILMES NO REDECANAIS')
app.geometry('500x215')
app.configure(background="#000")


vnome=Entry(app)
vnome.place(x=10,y=10,width=370,height=20)
vnome.bind("<Return>", (lambda event: buscadados()))

Button(app,text="PESQUISA",command=buscadados,background="#ff0",foreground='#000').place(x=390,y=10,width=100,height=21)

lb_filmes=Listbox(app,width=79)
lb_filmes.place(x=10,y=40)
lb_filmes.bind("<Return>", (lambda event: abre_o_navegador(lb_filmes.index(ACTIVE))))
lb_filmes.bind("<Double-Button-1>", (lambda event: abre_o_navegador(lb_filmes.index(ACTIVE))))
lb_filmes.place_forget()

txt1=Label(app,text='NADA ENCONTRADO!!!',background="#000",foreground='#fff',font=("arial", 25))
txt1.place(x=10,y=40,width=480,height=168)
txt1.place_forget()

app.mainloop()