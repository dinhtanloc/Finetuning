import openai
from dotenv import load_dotenv
import os
load_dotenv()

def open_file(filepath):
    with open(filepath,'r',encoding='utf-8') as infile:
        return infile.read()
    
def save_file(filepath,content):
    with open(filepath,'a',encoding='utf-8') as outfile:
        outfile.write(content)

api_key = open_file('apikey3.txt')

openai.api_key = api_key

print(api_key)
file_id = os.getenv('file_id')
module_name = 'gpt-3.5-turbo'
response = openai.FineTuningJob.create(
    training_file = file_id,
    model= module_name,
)
# openai.FineTuningJob.create(
#     training_file="file-JNKdiQH3wl60mnzrdbtJeLTQ",
#     model="gpt-3.5-turbo",
#     n_epochs=1,
#     batch_size=128,
#     learning_rate_multiplier=0.05,
#    # classification_n_classes=194
# )

job_id =response['id']
print(f'Fine tuning job created successfully with ID {job_id}')