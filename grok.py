
from rapidfuzz import fuzz, process
import sqlite3
from groq import Groq
API_KEY = "api_key_here"

client = Groq(api_key=API_KEY)
class groq:
    def create_friendly_ai(self):

        # شخصية المساعد الذكي
        system_prompt = """
        أنت مساعد ذكي اسمك "أورا" وأنت صديق مقرب للمستخدم. 
        - اسأل المستخدم بناء اخر كلامه    
        - استخدم العامية المصرية أحياناً
        - ردود قصيرة ومباشرة
   
            """
        
        return system_prompt

    def chat_with_friend(self , message, conversation_history=[]):

        system_prompt = self.create_friendly_ai() 
        # بناء المحادثة مع الذاكرة
        messages = [{"role": "system", "content": system_prompt}]
        for msg in conversation_history[-10:]:  # آخر 10 رسائل فقط
            messages.append(msg)

        sql = sqlite3.connect('sql_data_base.db')
        cursor = sql.cursor()

        rows = cursor.execute("SELECT user, aura FROM Aura").fetchall()

        best_match = None
        best_score = 0
        best_answer = None

        for saved_q, saved_a in rows:
            similarity = fuzz.partial_ratio(message, saved_q)
            if similarity > best_score:
                best_score = similarity
                best_match = saved_q
                best_answer = saved_a

        if best_score > 70:
            fact = f"المستخدم قال قبل كدا: '{best_match}'، وكان ردك: '{best_answer}'. دلوقتي جاوب على '{message}' بنفس المعنى لكن بشكل مختلف."
            messages.append({"role": "system", "content": fact})
        else:
            messages.append({"role": "user", "content": message})

        response = client.chat.completions.create(
            messages=messages,
            model="llama-3.3-70b-versatile",
            temperature=0.9,
            max_tokens=200,
        )

        ai_response = response.choices[0].message.content

        # حفظ في قاعدة البيانات
        cursor.execute("INSERT INTO Aura (user, aura) VALUES (?, ?)", (message, ai_response))
        sql.commit()

        sql.close()
        return ai_response
    def main(self,query):
        """
        محادثة مع صاحبك الذكي أورا
        """
        conversation_history = []   

        while True:

            ai_response = self.chat_with_friend(query, conversation_history)
            print(f"🤖 {ai_response}")
            
            # حفظ المحادثة في الذاكرة
            conversation_history.append({"role": "user", "content": query})
            conversation_history.append({"role": "assistant", "content": ai_response})








