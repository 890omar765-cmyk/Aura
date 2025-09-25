
import os
import speech_recognition as sr
from gtts import gTTS
from sentence_transformers import SentenceTransformer, util
import asyncio
import edge_tts
import json
import pickle
from playsound import playsound
from time import sleep
import pygame

class Aura:
    
    def __init__(self):
        
        self.model = SentenceTransformer("E:/Aura/models/arabert")
        commands ={
            'youtube': ['افتح اليوتيوب', 'افتح يوتيوب', 'فتح يوتيوب', 'افتح لي اليوتيوب', 'يوتيوب', 'عايز اليوتيوب', 'ممكن تفتح اليوتيوب', 'هات لي اليوتيوب', 'هاتلي اليوتيوب', 'شغل اليوتيوب', 'شغل يوتيوب'], 
            
            'search_youtube':['عايز اشوف فيديوهات', 'فيديوهات', 'افتح موقع الفيديوهات', 'هات مقاطع من يوتيوب', 'ابحث لي عن', 'هات لي فيديو', 'ابحث عن', 'شغل فيديو', 'عايز فيديو', 'شغل',"ابحث لي عن","شوف لي","بحث عن","سيرش عن","بحث"],
            
            'google': ['جوجل', 'فتح جوجل', 'هاتلي جوجل', 'عايز جووجل', 'افتح جوجل', 'شغل جوجل'],

            "search_google":['ابحث في جوجل', 'ممكن جوجل', 'ابحث لي على جوجل', 'محرك البحث', 'عايز ابحث في جوجل', 'ابحث لي في جوجل عن', 'ابحث لي في جوجل عن', 'ابحث في جوجل', 'افتح لي', 'افتح', 'ابحث لي', 'افتح', "افتح في جوجل", 'افنح لي في جوجل',"فتح"],
            
            'quit_google': ['اطلع من جوجل', 'اخرج من جوجل', 'اقفل جوجل', 'قفل جوجل', 'اطلع من جوجل', 'جووجل'],
            
            'facebook': ['افتح لي فيس بوك', 'افتح لي فيسبوك', 'افتح فيسبوك', 'عايز فيسبوك', 'فيس', 'فيس بوك', 'شغل فيسبوك', 'هاتلي فيسبوك', 'افتح حسابي على فيسبوك', 'ادخل فيسبوك', 'افتح لي فيسبوك', 'فيسبوك'],
            
            'post_facebook': ['عايز انزل بوست على فيسبوك', 'عايز انزل منشور على الفيس بوك', 'نزل بوست', 'بوست', 'نزل منشور فيس', 'بوست الفيس', 'بوست فيسبوك'], 
        
            'quit_facebook': ['اخرج من فيسبوك', 'اخرج من فيس', 'اطلع من فيسبوك', 'اطلع من فيس', 'اقفل فيسبوك', 'اقفل فيس', 'خروج فيسبوك'],    
            
            'whatsapp': ['افتح وتساب', 'افتح لي وتساب', 'افتح الوتساب', 'شغل واتس', 
            
            'عايز الواتساب', 'ممكن واتساب', 'هاتلي الواتساب', 'ادخل وتساب', 'ممكن تفتح الواتساب', 'هات الواتس', 'وتساب', 'واتس', 'افتح واتساب'],
            
            'quit_whatsapp': ['اقفل واتساب', 'اخرج من الوتساب', 'اطلع من الوتساب', 'اطلع من وتس', 'قفل الوتس', 'اخرج من الوتس', 'اطلع من وتس'], 
            
            'search_whatsapp': ['عايز اكلم', 'كلم لي', 'افتح شات', 'كلم', 'عايزك تكلم لي', 'عايز اكلم'], 
            
            'send_whatsapp': ['ابعت له', 'ابعث له', 'ارسل له', 'ابعت', 'ابعث', 'ابعث له', 'اكتب', 'اكتب له'], 
            
            'instagram': ['افتح انستقرام', 'افتح انستا', 'فتح انستا', 'فتح انستقرام', 'ابحثلي عن انستا', 'انستجرام', 'انستا', 'عايز انستقرام', 'عايز انستا', 'ممكن تفتح انستقرام', 'عايز انستا'], 
            
            'quit_instagram': ['اقفل انستقرام', 'اقفل انستا', 'قفل انستا', 'اطلع من انستجرام', 'اطلع من انستا'], 
            
            'post_instagram': ['عايز انزل بوست فالانستحرام', 'ابحث لي فالانستجرام', 'عايز انزل بوست فالانستا', 'عايز انزل منشور فالانستجرام', 'انزل بوست فالانستجرام', 'بوست انستا', 'بوستات انستا', 'بوست انستاا', 'منشور فالانستجرام'],
            
            "user_name": ["انا اسمي ايه","اسمي","اسمي ايه"],

            "user_age":["انا عندي كام سنه","انا سني ايه"],

            "quit_aura":["اقفلي يا اورا خلاص","اقفلي البرنامج",]
      
      
      
      
        }

        self.intent_vectors = {intent: self.model.encode(sentences, convert_to_tensor=True)
                        for intent, sentences in commands.items()}


    def dump_data(self,data):
        with open("data.json","w",encoding="utf-8")as file:
            json.dump(data,file)


    def data_cut(self,data_cut):
        with open("data.json","r",encoding="utf-8")as file:
            data = json.load(file)
        return data.get(data_cut,None)
    

    def lode_data(self):
        with open("data.json","r",encoding="utf-8")as file:
            json.load(file)

    def search(self, text):
        if not text:
            return ""


        keywords = [
                "افتح","افتحلي","افتح لي" ,"عايز ابحث عن","عايز فيديوهات","ابحث لي عن","ممكن تبحث لي عن","دورلي عن","بحث عن","عن",
                "واكتب لو","واكتب لو","وابعث له","ابعث له" ,"فتح"  ,"وابعث له','عايز اشوف فيديوهات', 'فيديوهات', 'افتح موقع الفيديوهات'"
                ", 'هات مقاطع من يوتيوب', 'ابحث لي عن', 'هات لي فيديو', 'ابحث عن', 'شغل فيديو', 'عايز فيديو","شغل","ابحث لي عن","شوف لي","بحث عن","سيرش عن","بحث","ابحث لي في جوجل عن",
                "ابحث في جوجل عن","افتح لي في جوجل","بحث في جوجل","افتح في جوجل","سيرش في جوجل عن",'عايز اكلم', 'كلم لي', 'افتح شات', 'كلم', 'عايزك تكلم لي', 'عايز اكلم','كلملي',"عايز اكلم","افتح لي شات",
                "عايز شات"

                      
                ]
        

        keywords.sort(key=len, reverse=True)
        for keyword in keywords:
            if keyword in text:
                clean_text = text.replace(keyword, '').strip()
                break  # لو لقيت كلمة، امسكها ومتكملش
        
        return clean_text if clean_text else text

    async def aura(self,text,lang="ar"):#تاخد الكلام او الصوت وتحوله لصوت كمبيوتر
    
        save_file = "ooop.mp3"
        gTTS(text=text, lang=lang).save(save_file)
        pygame.mixer.init(frequency=22050, size=-16, channels=2, buffer=512)

        pygame.mixer.music.load(save_file)
        pygame.mixer.music.play() 
        while pygame.mixer.music.get_busy():
            pygame.time.Clock().tick(10)
        pygame.mixer.music.stop() 
        pygame.mixer.quit()
        os.remove(save_file)

    def command(self,lang="ar-EG"):
        recognizer = sr.Recognizer() 
        recognizer.energy_threshold = 300
        recognizer.dynamic_energy_threshold = True
        recognizer.pause_threshold = 0.8
        with sr.Microphone() as mic:
            print("Aura ...")
            recognizer.adjust_for_ambient_noise(mic, duration=0.5)
            recognizer.phrase_threshold=0.4
            audio = recognizer.listen(mic,phrase_time_limit=50)              
            print("recording ....")
            try:
                ar = recognizer.recognize_google(audio, language=lang)
                print("Arabic recognized:", ar)
                return ar.lower()
            except :
                pass

      
                try:
                    en = recognizer.recognize_google(audio, language=lang)
                    print("English recognized:", en)
                    return en.lower()
                except sr.UnknownValueError:
                    pass


    def get_intent(self,query):

        user_vector = self.model.encode(query, convert_to_tensor=True)

        # تحديد أقرب intent
        best_intent = None
        best_score = -1
        for intent, vectors in self.intent_vectors.items():
            score = util.cos_sim(user_vector, vectors).max().item()
            if score > best_score:
                best_score = score
                best_intent = intent
        return best_intent 

