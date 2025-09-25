
import warnings
warnings.filterwarnings("ignore", category=UserWarning)
from time import sleep
import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "1"
from model import Aura
from youtube import Youtube
from facebook import Facebook
from my_google import Google
from whatsapp import Whatsapp
from instgram import Instgram
from google.api_core.exceptions import ResourceExhausted
from Googlee import chat
from grok import groq
gpt = chat()
grok = groq()
aura = Aura()
yt = Youtube()
gl = Google()
wt = Whatsapp()
fc = Facebook()
ins = Instgram()

command_keywords = ["افتح","افتحلي","افتح لي" ,"عايز ابحث عن","عايز فيديوهات","ابحث لي عن","ممكن تبحث لي عن","دورلي عن","بحث عن","عن",
                "واكتب لو","واكتب لو","وابعث له","ابعث له" ,"فتح"  ,"وابعث له','عايز اشوف فيديوهات', 'فيديوهات', 'افتح موقع الفيديوهات'"
                ", 'هات مقاطع من يوتيوب', 'ابحث لي عن', 'هات لي فيديو', 'ابحث عن', 'شغل فيديو', 'عايز فيديو","شغل","ابحث لي عن","شوف لي","بحث عن","سيرش عن","بحث","ابحث لي في جوجل عن",
                "ابحث في جوجل عن","افتح لي في جوجل","بحث في جوجل","افتح في جوجل","سيرش في جوجل عن",'عايز اكلم', 'كلم لي', 'افتح شات', 'كلم', 'عايزك تكلم لي', 'عايز اكلم','كلملي',"عايز اكلم","افتح لي شات",
                "عايز شات"]
while True:
    query = aura.command()
    if query is None:
        continue 
    # chatt = gpt.main(query)
    intent = aura.get_intent(query)
  

    if any(query.startswith(word) for word in command_keywords):



        if  intent == "whatsapp":
            try:
                wt.open_whatsapp()
            except:   
                continue 
        
        elif intent == "search_whatsapp": 
            try: 
                sleep(1)    
                wt.search_whatsapp(query)
            except:
                continue 

        elif intent == "send_whatsapp":
            try:  
                sleep(1)     
                wt.send_whatsapp(query)
            except:
                continue 

        elif intent == "quit_whatsapp":    
            sleep(1)
            try:
                wt.quit_whatsapp()
            except:
                continue 
        

                    

        elif intent == "facebook":  
            try:          
                fc.open_facebook()

            except:
                continue 

        elif intent == "post_facebook":

            try:
                sleep(3)
                fc.post_facebook()
            except:
                continue 




        elif intent == "youtube":
            try:
                yt.open_youtube()
            except:
                continue 
        elif intent == "search_youtube":
            try:
                sleep(1)
                yt.search_youtube(query)
            except:
                continue 




        elif intent == "google":
            try:
                gl.open_google()
            except:
                continue 

        elif intent == "search_google":
            try:
                sleep(1)
                gl.serch_google(query)
            except:
                continue 

        elif intent == "quit_google":
        
            try:
                gl.quit_google()
            except:
                continue 



        elif intent == 'instagram':
            try:
                ins.open_intgram()
                
            except:
                continue 

        if intent == "quit_Aura":
            break

    else:
        try:
            gpt.main(query)
        except ResourceExhausted:
            grok.main()  






          
             




