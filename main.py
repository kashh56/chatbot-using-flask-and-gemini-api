from flask import Flask, render_template, request
import google.generativeai as genai
import os
import pymysql
import json
from datetime import datetime

# connecting with sql local database for storing user query and model response
def connection():
    connect = pymysql.connect(
        user='root',
        host='localhost',
        database='my_database',
        password='root'
    )
    return connect



#use your own api key change the 'GOOGLE_API_KEY'
genai.configure(api_key=os.getenv('GOOGLE_API_KEY'))
model = genai.GenerativeModel('gemini-pro')

app = Flask(__name__)


@app.route('/', methods=['POST', 'GET'])
def chatbot():
    
    # connection call of database 
    connect = connection()
    cursor = connect.cursor()
    
    #chat history between model and user
    history = [
        {"role": "user", "parts": "Hello"},
        {"role": "model", "parts": "Great to meet you. What would you like to know?"},
    ]

    chat = model.start_chat(
        history=history
    )
    
    #collect user query from 'query'
    if request.method == 'POST':
       
        start_time=datetime.now()
       
        user_query = request.form.get('query')
        try:
            
            response = chat.send_message(user_query) 
            result_text = response.text
            
            end_time = datetime.now()
            status="completed"
            summary = chat.send_message('give a summary also') 
            result_text2 = summary.text
            chatsummary=result_text2

            sql_chats_table = """
INSERT INTO chats (UserID, StartTime, EndTime, Status, ChatSummary)
VALUES (%s, %s, %s, %s, %s)
"""
            cursor.execute(sql_chats_table, (1,start_time,end_time,status,chatsummary))
            connect.commit()
            

            chat_data = {
            "user_message": user_query,
            "model_response": result_text }
            
            chatid = 5
            #using json_dumps to convert chat data to json  
            chat_json = json.dumps(chat_data)
            sql_chat_history_table = 'INSERT INTO chat_history (chatid , MessageContent) VALUES (%s, %s)'
            cursor.execute(sql_chat_history_table, (chatid,chat_json))
            connect.commit()



        except genai.types.generation_types.StopCandidateException as e:
            result_text = f"Error: {e}"

        
        return render_template('index.html', results = result_text)
         
    else:
        return render_template('index.html')




if __name__ == '__main__':
    app.run(debug=True)
