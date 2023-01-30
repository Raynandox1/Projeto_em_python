from tkinter import*
from bs4 import BeautifulSoup
import requests
import tkinter.ttk as ttk
import webbrowser

def buscar():
    txt1.place_forget()
    lb_series.delete(0,END)
    lista.clear()
    link_da_serie.clear()
       
    url = 'https://redecanais.cx/mapa.html'

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
        nome = href[href.find('browse-')+7:href.find("-vi")]
        nome = nome.replace("-"," ")
        

        if ppesquisa.casefold() in href.casefold():
            href = href[href.find('<a href="')+9:href.find('" target="')]
            href = "https://redecanais.la"+href  
            lista.append(nome)
            link_da_serie.append(href)
    
    if len(lista) == 0:
        
        #txt1=Label(app,text='NADA ENCONTRADO!!!',background="#ff0",foreground='#000',font=("arial", 25))
        txt1.place(x=10,y=40,width=480,height=168)
        return
    
    for lfilmes in lista:
        lb_series.insert(END,lfilmes)

    lb_series.place(x=10,y=40)




def abre_o_link(linkfilme):

    url = linkfilme
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



def busca_o_link(link):

    if "https://redecanais.cx" in link_da_serie[link]:
        abre_o_link(link_da_serie[link])
    else:

        lb_series.delete(0,END)
        lista.clear()
        

        Nnome = str(lb_series.get(ACTIVE)) #nome da series
        url = link_da_serie[link]
        link_da_serie.clear()

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
                    lista.append(nome+"\n")
                    link_da_serie.append(href)
        
        for lfilmes in lista:
                lb_series.insert(END,lfilmes)


#####################################################################CORPO DO MEU USERFOM##############################################################################
lista = list()
link_da_serie = list()

app=Tk()
app.title('BUSCAR POR SÉRIES NO REDECANAIS')
app.geometry('500x215')
app.configure(background="#000")


vnome=Entry(app)
vnome.place(x=10,y=10,width=370,height=20)
vnome.bind("<Return>", (lambda event: buscar()))

Button(app,text="PESQUISA",command=buscar,background="#ff0",foreground='#000').place(x=390,y=10,width=100,height=21)

lb_series=Listbox(app,width=79)
#lb_series.place(x=10,y=40)
lb_series.bind("<Return>", (lambda event: busca_o_link(lb_series.index(ACTIVE))))
lb_series.bind("<Double-Button-1>", (lambda event: busca_o_link(lb_series.index(ACTIVE))))
#lb_series.place_forget()

txt1=Label(app,text='NADA ENCONTRADO!!!',background="#000",foreground='#fff',font=("arial", 25))
#txt1.place(x=10,y=40,width=480,height=168)
txt1.place_forget()

app.mainloop()