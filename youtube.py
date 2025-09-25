

import webbrowser
from time import sleep
import pyautogui
import pyperclip
from model import Aura
aura = Aura()

class Youtube:

    def open_youtube(self):
        webbrowser.open_new_tab("https://www.youtube.com")
        
    def search_youtube(self,query):
        ser2 = aura.search(query)
        pyautogui.hotkey("/")
        pyperclip.copy(ser2)
        sleep(3)
        pyautogui.hotkey("ctrl","v") 
        sleep(3) 
        pyautogui.press("enter")    