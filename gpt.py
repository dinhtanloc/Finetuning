import streamlit as st
import openai
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv('API_KEY')

# GPT, phiên bản cũ, pip install openai==0.28
# Khai báo API key của bạn ở đây
openai.api_key = api_key

def get_gpt_response(prompt):
    response = openai.ChatCompletion.create(
      model="your model",  # Bạn có thể thay đổi model tùy thuộc vào nhu cầu của bạn
      messages=[{"role": "system", "content": "You are cybersecurity specialist. Please answer any question concern about security problem!"}, {"role": "user", "content": prompt}],
      max_tokens=150
    )
    return response['choices'][0]['message']['content'].strip()


#GPT, phiên bản mới
from openai import OpenAI

client = OpenAI(
    api_key = os.getenv('API_KEY'),
)

# print(os.getenv('AI_key'))

def get_gpt_response(prompt):
    response = client.chat.completions.create(
      model="ft:gpt-3.5-turbo-0125:ueh::9DUn0U80",  
      messages=[{"role": "system", "content": "You are cybersecurity specialist. Please answer any question concern about security problem!"}, {"role": "user", "content": prompt}],
      max_tokens=150
    )
    return  response.choices[0].message.content





# Tiêu đề của chatbox
st.title("ChatGPT Streamlit Chatbox")

# Khung nhập văn bản để người dùng nhập câu hỏi
user_input = st.text_input("Bạn muốn nói gì?", "")

# Nếu có input từ người dùng, gửi nó đến ChatGPT và hiển thị phản hồi
if user_input:
    response = get_gpt_response(user_input)
    st.text_area("ChatGPT's response:", value=response, height=200, max_chars=150, key="response")

