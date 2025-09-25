
import os
from time import sleep
import pyautogui
import pyperclip
from model import Aura
aura = Aura()

class Whatsapp:
    def open_whatsapp(self):
        sleep(1)
        os.system("start whatsapp:")
        sleep(3) 

    def search_whatsapp(self,query):
        call = aura.search(query)          
        pyperclip.copy(call)
        pyautogui.hotkey("ctrl","f")
        sleep(1)
        pyautogui.hotkey("ctrl","v") 
        sleep(2)
        pyautogui.hotkey("ctrl","1") 
        sleep(2)


    def send_whatsapp(self,query):
        sleep(1)
        pyperclip.copy(query)
        sleep(1)
        pyautogui.hotkey("ctrl","v")
        sleep(1)
        pyautogui.press("enter")

    def quit_whatsapp():
        pyautogui.hotkey("alt","F4")         

