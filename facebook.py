
import webbrowser
from time import sleep
import pyautogui
from model import Aura
aura = Aura()

class Facebook:
    def open_facebook(self):
        webbrowser.open_new_tab("https://www.facebook.com") 

    def post_facebook(self):
        aura.Aura("اكتب منشورك عشان انشره ف الفيسبوك",lang="ar")
        post = input("Enter your post: ")
        webbrowser.open_new_tab("https://www.facebook.com")        
        sleep(10)
        pyautogui.hotkey("p")
        sleep(3)
        pyautogui.typewrite(post)
        sleep(3)
        pyautogui.click(678,583)  

