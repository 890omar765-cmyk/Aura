# type: ignore
import google.generativeai as genai
from model import Aura
import asyncio
import sqlite3
aura = Aura()
from rapidfuzz import fuzz, process
class chat:

    def create_friendly_ai(self):
        genai.configure(api_key="api_key_here")
        self.model = genai.GenerativeModel(
            "gemini-2.5-flash",
            system_instruction="""
        أنت مساعد ذكي اسمك "أورا" وأنت صديق مقرب للمستخدم. 
        - اسأل المستخدم بناء اخر كلامه    
        - استخدم العامية المصرية أحياناً
        - ردود قصيرة ومباشرة
            
            """,
            generation_config={
                "temperature": 0.3,
                "top_p": 0.9,
                "max_output_tokens": 512
            }
        )
        self.chat = self.model.start_chat()          
    def chat_with_friend(self, message ,conversation_history=[]):

        sql = sqlite3.connect('sql_data_base.db')
        cursor = sql.cursor()
        
        system_prompt = self.create_friendly_ai()
        messages = [{"role": "system", "content": system_prompt}]
        for msg in conversation_history[-10:]:  # آخر 10 رسائل فقط
            messages.append(msg)

        rows = cursor.execute("SELECT user, aura FROM Aura").fetchall()
        best_match = None
        best_score = 0
        best_answer = None

        for saved_q, saved_a in rows:
            samury =  fuzz.partial_ratio(message,saved_q)
            if samury> best_score:
                best_score = samury
                best_match = saved_q
                best_answer = saved_a
        if best_score> 70:
            fact = f"المستخدم قال قبل كدا: '{best_match}'، وكان ردك: '{best_answer}'. دلوقتي جاوب على '{message}' بنفس المعنى لكن بشكل مختلف."
            
            self.model = genai.GenerativeModel(
            "gemini-2.5-flash",
            system_instruction=f'''{fact}
                أنت مساعد ذكي اسمك "أورا" وأنت صديق مقرب للمستخدم. 
        - اسأل المستخدم بناء اخر كلامه    
        - استخدم العامية المصرية أحياناً
        -  ردود قصيرة ومباشرة مترددش الكلام
                       
               
                 '''

            )
            self.chatt = self.model.start_chat()
            response = self.chatt.send_message(fact)
            ai_response = response.text      
            
        else:

            response = self.chat.send_message(final_message)
            ai_response = response.text

            cursor.execute("INSERT INTO Aura (user, aura) VALUES (?, ?)", (message, ai_response))
            sql.commit()

        sql.close()
        return ai_response
    
    def main(self, query):
            ai_response = self.chat_with_friend(query)
            asyncio.run(aura.aura(ai_response, lang="ar"))



