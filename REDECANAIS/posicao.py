import pyautogui
import time
import webbrowser

url = 'https://sinalpublico.com/player3/serverf2hlb.php?vid=DBZFILME15'
chrome_path = 'C:/Program Files/Google/Chrome/Application/chrome.exe %s'
webbrowser.get(chrome_path).open(url)

time.sleep(5)
pyautogui.click(940,574)
time.sleep(3)
pyautogui.click(940,574)

from pynput.keyboard import Key, Controller

keyb = Controller()

with keyb.pressed(Key.ctrl):
    keyb.press('s')
    keyb.release('s')

time.sleep(3)
keyb.press(Key.right)
keyb.release(Key.right)

keyb.type('.txt')
keyb.press(Key.enter)
keyb.release(Key.enter)