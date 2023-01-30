import webbrowser

url = 'https://redecanais.la/mapafilmes.html'
chrome_path = 'C:/Program Files/Google/Chrome/Application/chrome.exe %s'
webbrowser.get(chrome_path).open(url)

#abrir o site
import time

time.sleep(2)
    
from pynput.keyboard import Key, Controller

keyb = Controller()

with keyb.pressed(Key.ctrl):
    keyb.press('s')
    keyb.release('s')

time.sleep(3)


keyb.type('lista de filmes.txt')
keyb.press(Key.enter)
keyb.release(Key.enter)