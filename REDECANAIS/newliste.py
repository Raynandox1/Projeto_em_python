from tkinter import *
import webbrowser

def weblink(*args):
    index = lb.curselection()[0]
    item = lb.get(index)
    if 'https://' in item:
        webbrowser.open_new(item)

list_of_items = ['Google news',
                 'https://news.google.com/',
                 'Yahoo news',
                 'https://news.yahoo.com/']
root = Tk()
lb = Listbox(root)
lb.bind('<<ListboxSelect>>', weblink)
for item in list_of_items:
    lb.insert(END, item)
lb.pack()
root.mainloop()