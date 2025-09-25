

import webbrowser
from time import sleep
import pyautogui
import pyperclip
from model import Aura
aura = Aura()

class Google:
    def open_google(self):
        webbrowser.open_new_tab("https://www.google.com")
        sleep(5) 

    def serch_google(self,query):
        webbrowser.open_new_tab("https://www.google.com")
        sleep(1)
        new_search = aura.search(query)
        pyautogui.hotkey("ctrl","e")
        sleep(1)
        pyperclip.copy(new_search)
        sleep(1)
        pyautogui.hotkey("ctrl","v")
        sleep(1)
        pyautogui.press("enter") 

    def quit_google(self):
        pyautogui.hotkey("alt","F4") 


