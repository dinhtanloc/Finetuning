import openai
import os
from dotenv import load_dotenv

load_dotenv()


def open_file(filepath):
    with open(filepath,'r',encoding='utf-8') as infile:
        return infile.read()
    
def save_file(filepath,content):
    with open(filepath,'a',encoding='utf-8') as outfile:
        outfile.write(content)

api_key = os.getenv('API_KEY')

openai.api_key = api_key

print(api_key)
# file_id = ''
module_name = 'gpt-3.5-turbo'
filepath="D:/test_gpt/conversation4.jsonl"
with open(filepath,'rb') as file:
    response = openai.File.create(
        file = file,
        purpose= 'fine-tune',
    )
job_id =response['id']
print(f'Fine tuning job uploaded successfully with ID {job_id}')