from tkinter import*
from bs4 import BeautifulSoup
import requests
import tkinter.ttk as ttk

import pyautogui
import time
import webbrowser

  
filmes = list()
app=Tk()
app.title('BUSCAR POR FILMES NO REDECANAIS')
app.geometry('500x300')
app.configure(background="#000")

#txt1=Label(app,text='PESQUISA',background="#ff0",foreground="#000")
#txt1.place(x=10,y=10,width=100,height=20)
def additem():
    #lb_filmes.insert(END,str(vnome.get()))
    lista.append(vnome.get())
    vnome.delete(0,END)
    #lista.clear()

def addlista():
    for lfilmes in lista:
        lb_filmes.insert(END,lfilmes)

def some():
    global estado
    if estado == 0:
        lb_filmes.place_forget()
        estado = 1
    else:
        lb_filmes.place(x=10,y=40)
        estado = 0

    
    

def aparece():
    lb_filmes.place(x=10,y=40)

vnome=Entry(app)
vnome.place(x=10,y=10,width=370,height=20)
vnome.bind("<Return>", (lambda event: additem()))
def apaga():
    lb_filmes.delete(0,END)


estado = 0
Button(app,text="delete",command=apaga,background="#ff0",foreground='#000').place(x=390,y=10,width=100,height=21)
Button(app,text="some",command=some,background="#ff0",foreground='#000').place(x=390,y=40,width=100,height=21)
Button(app,text="add lista",command=addlista,background="#ff0",foreground='#000').place(x=390,y=70,width=100,height=21)

lista = ['raynando','henriquer','lima','santos']

lb_filmes=Listbox(app,width=40)
lb_filmes.place(x=10,y=40)


#lb_filmes.bind("<Return>", (lambda event: busca_o_link(lb_filmes.index(ACTIVE))))
#lb_filmes.bind("<Double-Button-1>", (lambda event: busca_o_link(lb_filmes.index(ACTIVE))))



app.mainloop()