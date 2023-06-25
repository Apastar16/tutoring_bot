import streamlit as st
from streamlit_chat import message
from bardapi import Bard
import json
with open('credentials.json','r')as f:
    file=json.load(f)
    token=file['token']


def generate_response(prompt):
    bard= Bard(token=token)
    response=bard.get_answer(prompt)['content']
    return response


def get_text():
    input_text=st.text_input("CN Bot:","Hey wassup?",key="input")
    return input_text
#Title of the streamlit app
st.title('Personal Tutoring Bot!')
changes ='''
<style>
url='https://images.unsplash.com/photo-1490730141103-6cac27aaab94?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=870&q=80'
[data-testid="atAppViewContainer"]
     {
     background-image:url('https://images.unsplash.com/photo-1490730141103-6cac27aaab94?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=870&q=80')
     background-size:cover;
     }
 </syle>"'''

st.markdown(changes,unsafe_allow_html=True)
print(st.session_state)
if 'generated' not in st.session_state:
    st.session_state['generated']=[]
if 'past' not in st.session_state:
    st.session_state['past']=[]
#Accepting user input
user_input = get_text()
if user_input:
    print(user_input)
    response = generate_response(user_input)
    print(response)
    st.session_state['past'].append(user_input)
    st.session_state['generated'].append(response)

if st.session_state['generated']:
  for i in range(len(st.session_state['generated'])-1,-1,-1):
      message(st.session_state['generated'][i],key=str(i))
      message(st.session_state['past'][i], key=str(i)+'_user',is_user=True)


