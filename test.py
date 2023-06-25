from bardapi import Bard
import json

from main import response

with open('credentials.json','r') as f:
   file = json.load(f)
   token = file['token']

bard = Bard(token=token)
bard.get_answer("What is algorithm?")['content']
print(response)